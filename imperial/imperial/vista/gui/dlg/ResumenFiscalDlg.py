#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 22/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.filterReturn import FilterReturn
from imperial.core.util import printer
from imperial.core.util.ManejaFechas import ManejaFechas
from imperial.model.informes.EditCalc import EditCalcResumenFiscal
from imperial.model.modeltable import tableModelResumenFiscal
from imperial.model.modeltable.tableModelResumenFiscal import \
    ResumenFiscalDelegate
from imperial.vista.gui.dlg.ui_dlgResumenFiscal import Ui_DlgResumenFiscal
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime
import os
import tempfile

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class ResumenFiscalDlg(_qg.QDialog, Ui_DlgResumenFiscal):
    u"""Diálogo."""
    
    def __init__(self, modelo=None, parent=None):
        super(ResumenFiscalDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        self.resumenTableView.setModel(modelo)

        self.resumenTableView.setItemDelegate(ResumenFiscalDelegate(self))
        self.modelo.tableView = self.resumenTableView
        
        newIndex = self.resumenTableView.model().index(0, 1)
        #self.saldosTableView.selectionModel().select(newIndex, _qc.QItemSelectionModel.Select)
        self.resumenTableView.setCurrentIndex(newIndex)
        
        if not MAC: 
            self.guardarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            self.cerrarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
                
        self.fechaDateEdit.setDate(datetime.date.today())
        
        self.filterReturn = FilterReturn()
        self.resumenTableView.installEventFilter(self.filterReturn)
        self.connect(self.resumenTableView, _qc.SIGNAL("enterPressed()"), 
                     self.cambiarFila)
        
        self.fechaDateEdit.installEventFilter(self.filterReturn)
        self.connect(self.fechaDateEdit, _qc.SIGNAL("enterPressed()"), 
                     self.resumenTableView.setFocus)
        
        self.guardarPushButton.clicked.connect(self.guardarDatos)
        self.fechaDateEdit.dateChanged.connect(self.buscarDatos)
        
        self.resumenTableView.horizontalHeader().setStretchLastSection(True)
        
        vHeaderResumen = self.resumenTableView.verticalHeader()
        vHeaderResumen.setResizeMode(_qg.QHeaderView.Fixed)
        vHeaderResumen.setDefaultSectionSize(24)
        
        self.setMinimumSize(600, 550)
        
        self.fechaDateEdit.setFocus()
        self.updateUi()
        
    def keyPressEvent(self, e):
        if e.key() == _qc.Qt.Key_Escape:
            e.ignore()
        else:
            _qg.QDialog.keyPressEvent(self, e)
            #e.accept()
        
    def cambiarFila(self):
        index = self.resumenTableView.currentIndex()
        next_index =  self.resumenTableView.model().index(index.row() + 1, index.column())
        
        if index.row() + 1 >= self.modelo.rowCount():
            next_index =  self.resumenTableView.model().index(0, index.column())
        
        self.resumenTableView.setCurrentIndex(next_index)
        
    @_qc.pyqtSlot()
    def on_cerrarPushButton_clicked(self):
        self.parentWidget().close()
        _qg.QDialog.accept(self)

    @_qc.pyqtSlot()
    def on_resumenPushButton_clicked(self):
        self.generarReporte()
        
    @_qc.pyqtSlot()
    def on_resumenBlancoPushButton_clicked(self):
        self.generarReporteEnBlanco()
 
    @_qc.pyqtSlot()       
    def guardarDatos(self):
        tit = u"Resumen fiscal"
        ok, msg = self.modelo.guardarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
        else:
            _qg.QMessageBox.information(self, tit, msg)
            
    @_qc.pyqtSlot("QDate")        
    def buscarDatos(self, fecha):
        tit = u"Resumen Fiscal"
        ok, msg = self.modelo.buscarDatosResumenes(self.data())
        
        if not ok:
            _qg.QMessageBox.information(self, tit, msg)
        
    def data(self):
        return [self.fechaDateEdit.date().toPyDate(),]
    
    def resetValues(self):
        self.limpiarTabla()
        self.updateUi()
        self.fechaDateEdit.setFocus()
        
    def limpiarTabla(self):
        self.modelo.limpiarValores()
        
    def resizeColumns(self, columns):
        for column in columns:
            self.resumenTableView.resizeColumnToContents(column)
            
    def generarReporteEnBlanco(self):
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        
        import tempfile
        file = tempfile.mktemp(".xls")
        open(file, "w")
        #file = os.curdir + variables.PATH_REPORTES + variables.FILE_REPORTE_SALDO
        
        lst_header, array_datos, lst_resaltados = self.modelo.datos2ArrayBlank()#self.modelo.datos2Array()
        
        edit = EditCalcResumenFiscal(file, array_datos, lst_header)
        edit.lst_resaltados = lst_resaltados
        edit.title = u'RESUMEN FISCAL | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate())
        edit.abrirArchivo()
        edit.crearHoja()
        #edit.setFooter(u'&F | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        edit.setFooter(u'')
        edit.setWidthCol((16 * 256, 18 * 256, 18 * 256, 18 * 256, 18 * 256))
        edit.escribirArchivo()
        edit.salvarArchivo()
        
        #os.startfile(edit.fileCalc)
        self.imprimirReporte(edit.fileCalc)
        _qg.QApplication.restoreOverrideCursor()
        
    def generarReporte(self):
        self.resumenPushButton.setEnabled(False)
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        
        file = tempfile.mktemp(".xls")
        open(file, "w")
        #file = os.curdir + variables.PATH_REPORTES + variables.FILE_REPORTE_SALDO
        
        lst_header, array_datos, lst_resaltados = self.modelo.datos2Array()
        
        edit = EditCalcResumenFiscal(file, array_datos, lst_header)
        edit.lst_resaltados = lst_resaltados
        edit.title = u'RESUMEN FISCAL | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate())
        edit.abrirArchivo()
        edit.crearHoja()
        #edit.setFooter(u'&F | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        edit.setFooter(u'')
        edit.setWidthCol((16 * 256, 18 * 256, 18 * 256, 18 * 256, 18 * 256))
        edit.escribirArchivo()
        edit.salvarArchivo()
        
        #os.startfile(edit.fileCalc)
        self.imprimirReporte(edit.fileCalc)
        _qg.QApplication.restoreOverrideCursor()
        self.resumenPushButton.setEnabled(True)
        
    def imprimirReporte(self, file):
        #os.startfile(file)
        printer.defaultPrinter(file)
        
    def updateUi(self):
        enable = True
        self.guardarPushButton.setEnabled(enable)
        #self.resizeColumns(tableModelResumenFiscal.lstHeader)