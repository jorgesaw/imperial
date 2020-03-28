#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 22/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.filterReturn import FilterReturn
from imperial.core.util.ManejaFechas import ManejaFechas
from imperial.model.informes.EditCalc import EditCalc
from imperial.model.modeltable import tableModelSaldoDiario
from imperial.model.modeltable.tableModelSaldoDiario import SaldoDiarioDelegate
from imperial.util import variables
from imperial.core.util import printer
import tempfile
from imperial.vista.gui.dlg.ui_dlgSaldoDiario import Ui_DlgSaldoDiario
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime
import os

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class SaldoDiarioDlg(_qg.QDialog, Ui_DlgSaldoDiario):
    u"""Diálogo."""
    
    def __init__(self, modelo=None, parent=None):
        super(SaldoDiarioDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        self.saldosTableView.setModel(modelo)
        self.saldosTableView.setItemDelegate(SaldoDiarioDelegate(self))
        self.modelo.tableView = self.saldosTableView
        
        #if not MAC: 
            #self.nuevoPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            #self.guardarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            #self.buscarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            #self.actualizarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            #self.cerrarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            
        self.saldosTableView.setColumnWidth(0, 330)
        for i in range(3):
            self.saldosTableView.setColumnWidth(i + 1, 100)
                
        self.fechaDateEdit.setDate(datetime.date.today())
        self.fechaDateEdit.dateChanged.connect(self.buscarDatos)
        self.pushButtonImprimir.clicked.connect(self.generarReporte)
        self.pushButtonImprimirBlanco.clicked.connect(self.generarReporteEnBlanco)
        
        self.filterReturn = FilterReturn()
        self.saldosTableView.installEventFilter(self.filterReturn)
        self.connect(self.saldosTableView, _qc.SIGNAL("enterPressed()"), 
                     self.cambiarFila)
        
        filterReturnFecha = FilterReturn()
        self.fechaDateEdit.installEventFilter(filterReturnFecha)
        self.connect(self.fechaDateEdit, _qc.SIGNAL("enterPressed()"), 
                     self.saldosTableView.setFocus)
        
        
        self.guardarPushButton.clicked.connect(self.guardarDatos)
        #self.buscarPushButton.clicked.connect(self.buscarDatos)
        #self.nuevoPushButton.clicked.connect(self.limpiarTabla)
        #self.actualizarPushButton.clicked.connect(self.actualizarDatos)
        
        self.fechaDateEdit.setFocus()
        self.setTitFecha(self.fechaDateEdit.date())
        #self.actualizarPushButton.setEnabled(False)
        
        #self.datosTableView.horizontalHeader().setResizeMode(_qg.QHeaderView.Stretch)
        self.saldosTableView.horizontalHeader().setStretchLastSection(True)
        
        vHeaderSaldos = self.saldosTableView.verticalHeader()
        vHeaderSaldos.setResizeMode(_qg.QHeaderView.Fixed)
        vHeaderSaldos.setDefaultSectionSize(24)
        
        #self.setSizePolicy(_qg.QSizePolicy.Expanding, _qg.QSizePolicy.Expanding)
        self.setMinimumSize(690, 550)
        #self.setMinimumWidth(690)
        
        
        #self.saldosTableView.setFocus()
        
        idx =  self.saldosTableView.model().index(0, 1)
        #self.saldosTableView.selectionModel().select(newIndex, _qc.QItemSelectionModel.Select)
        self.saldosTableView.setSelectionBehavior(_qg.QTableView.SelectRows)
        self.saldosTableView.setCurrentIndex(idx)
        
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        self.modelo.buscarDatos(self.data())
        _qg.QApplication.restoreOverrideCursor()
        
        self.updateUi()
        
    def keyPressEvent(self, e):
        if e.key() == _qc.Qt.Key_Escape:
            e.ignore()
        else:
            _qg.QDialog.keyPressEvent(self, e)
            #e.accept()
        
    def setTitFecha(self, fecha):
        self.setWindowTitle(u"Saldo diario - " + ManejaFechas.date2Str(fecha.toPyDate()))
        
    def cambiarFila(self):
        index = self.saldosTableView.currentIndex()
        next_index =  self.saldosTableView.model().index(index.row() + 1, index.column())
        
        if index.row() + 1 >= self.modelo.rowCount():
            next_index =  self.saldosTableView.model().index(0, index.column())
        
        self.saldosTableView.setCurrentIndex(next_index)
        
    @_qc.pyqtSlot()
    def on_cerrarPushButton_clicked(self):
        self.parentWidget().close()
        _qg.QDialog.accept(self)
 
    @_qc.pyqtSlot()       
    def guardarDatos(self):
        tit = u"Saldo diario"
        ok, msg = self.modelo.guardarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
            #self.modelo.limpiarValores()
        else:
            _qg.QMessageBox.information(self, tit, msg)
    
    @_qc.pyqtSlot()                
    def actualizarDatos(self):
        tit = u"Saldo diario"
        ok, msg = self.modelo.actualizarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
            #self.modelo.limpiarValores()
        else:
            _qg.QMessageBox.information(self, tit, msg)
            
    @_qc.pyqtSlot("QDate")        
    def buscarDatos(self, fecha):
        tit = u"Saldo diario"
        self.setTitFecha(fecha)
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        ok, msg = self.modelo.buscarDatos(self.data())
        _qg.QApplication.restoreOverrideCursor()
        #if ok:
        #   self.actualizarPushButton.setEnabled(ok)
        #else:
        #   _qg.QMessageBox.information(self, tit, msg)
        _qg.QMessageBox.information(self, tit, msg)
        
    def generarReporteEnBlanco(self):
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        
        import tempfile
        file = tempfile.mktemp(".xls")
        open(file, "w")
        #file = os.curdir + variables.PATH_REPORTES + variables.FILE_REPORTE_SALDO
        
        lst_header, array_datos, lst_resaltados = self.modelo.datos2ArrayBlank()#self.modelo.datos2Array()
        
        edit = EditCalc(file, array_datos, lst_header)
        edit.lst_resaltados = lst_resaltados
        edit.title = u'SALDO DIARIO | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate())
        edit.abrirArchivo()
        edit.crearHoja()
        edit.setFooter(u'')
        #edit.setFooter(u'Saldo diario | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        edit.setWidthCol((80 * 256, 16 * 256))
        edit.escribirArchivo()
        edit.salvarArchivo()
        
        #os.startfile(edit.fileCalc)
        self.imprimirReporte(edit.fileCalc)
        _qg.QApplication.restoreOverrideCursor()
        
    def generarReporte(self):
        self.pushButtonImprimir.setEnabled(False)
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        
        file = tempfile.mktemp(".xls")
        open(file, "w")
        #file = os.curdir + variables.PATH_REPORTES + variables.FILE_REPORTE_SALDO
        
        lst_header, array_datos, lst_resaltados = self.modelo.datos2Array()
        
        edit = EditCalc(file, array_datos, lst_header)
        edit.lst_resaltados = lst_resaltados
        edit.title = u'SALDO DIARIO | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate())
        edit.abrirArchivo()
        edit.crearHoja()
        edit.setFooter(u'')
        #edit.setFooter(u'&F | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        #edit.setFooter(u'Saldo diario | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        edit.setWidthCol((80 * 256, 16 * 256))
        edit.escribirArchivo()
        edit.salvarArchivo()
        
        #os.startfile(edit.fileCalc)
        self.imprimirReporte(edit.fileCalc)
        _qg.QApplication.restoreOverrideCursor()
        self.pushButtonImprimir.setEnabled(True)
        
    def imprimirReporte(self, file):
        #os.startfile(file)
        printer.defaultPrinter(file)
            
    def setFechaSorteo(self, fechaSorteo):
        self.fechaDateEdit.setDate(fechaSorteo)
        
    def closeEvent(self, event):
        self.modelo.cerrarSesionDAO()
        
    def data(self):
        return [self.fechaDateEdit.date().toPyDate(),]
    
    def resetValues(self):
        #self.fechaDateEdit.setDateTime(datetime.today())
        self.limpiarTabla()
        self.updateUi()
        self.fechaDateEdit.setFocus()
        
    def limpiarTabla(self):
        self.actualizarPushButton.setEnabled(False)
        self.modelo.limpiarValores()
        
    def resizeColumns(self, columns):
        for column in columns:
            self.saldosTableView.resizeColumnToContents(column)
        
    def updateUi(self):
        pass
        #enable = not (self.tipoLot is None)
        #enable = True
        #self.guardarPushButton.setEnabled(enable)
        #self.actualizarPushButton.setEnabled(not enable)
        #self.resizeColumns(tableModelSaldoDiario.lstHeader)