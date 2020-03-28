#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 22/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.filterReturn import FilterReturn
from imperial.core.model.listmodel.datosListModel import DatosListModel
from imperial.core.util import printer
from imperial.core.util.ManejaFechas import ManejaFechas
from imperial.dao.DAOVendedor import DAOVendedor
from imperial.model.informes.EditCalc import EditCalc, EditCalcVentaDiaria
from imperial.model.models import VendedorExterno
from imperial.model.modeltable.modeldatatable import tmVentaDiariaVariedades
from imperial.model.modeltable.modeldatatable.tmVentaDiariaVariedades import \
    VentaDiariaVariedadesDelegate
from imperial.util import variables
from imperial.vista.gui.dlg.ui_dlgVentaDiaria import Ui_DlgVentaDiaria
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime
import os

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class VentaDiariaDlg(_qg.QDialog, Ui_DlgVentaDiaria):
    u"""Diálogo."""
    
    def __init__(self, modelo=None, parent=None):
        super(VentaDiariaDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.vendedorExt = None
        self.modelo = modelo
        self.modelo.ventana = self
        
        #delegate = VentaDiariaVariedadesDelegate(self)
        delegateVarios = VentaDiariaVariedadesDelegate(self)
        delegatePan = VentaDiariaVariedadesDelegate(self)
        #delegate.modelo = modelo
        #delegate.ventana = self
        
        #self.ventaVariosTableView.setModel(modelo)
        #self.ventaPanesTableView.setModel(modelo)
        self.ventaVariosTableView.setModel(self.modelo.modeloVarios)
        self.ventaPanesTableView.setModel(self.modelo.modeloPan)
        
        self.ventaVariosTableView.setItemDelegate(delegateVarios)
        self.ventaPanesTableView.setItemDelegate(delegatePan)
        self.ventaVariosTableView.setSelectionBehavior(_qg.QTableView.SelectRows)
        self.ventaPanesTableView.setSelectionBehavior(_qg.QTableView.SelectRows)
        #fuente = _qg.QFont("Arial", 25)
        
        self.pushButtonImprimir.clicked.connect(self.generarReporte)
        
        self.ventaVariosTableView.setMinimumHeight(450)
        self.ventaVariosTableView.setSizePolicy(_qg.QSizePolicy.Expanding, _qg.QSizePolicy.Expanding)
        #self.ventaVariosTableView.setFont(fuente)
        #self.datosTableView.horizontalHeader().setResizeMode(_qg.QHeaderView.Stretch)
        self.ventaVariosTableView.horizontalHeader().setStretchLastSection(True)
        self.ventaPanesTableView.horizontalHeader().setStretchLastSection(True)
        
        for tableview in (self.ventaVariosTableView, self.ventaPanesTableView):
            tableview.setColumnWidth(0, 260)
            for i in xrange(6):
                tableview.setColumnWidth(i + 1, 50)
            tableview.setColumnWidth(7, 75)
            tableview.setColumnWidth(8, 85) 
            for i in xrange(3):
                tableview.setColumnWidth(9 + i, 77)
                
        vHeaderVarios = self.ventaVariosTableView.verticalHeader()
        vHeaderVarios.setResizeMode(_qg.QHeaderView.Fixed)
        vHeaderVarios.setDefaultSectionSize(24)
        
        vHeaderPan = self.ventaPanesTableView.verticalHeader()
        vHeaderPan.setResizeMode(_qg.QHeaderView.Fixed)
        vHeaderPan.setDefaultSectionSize(24)
        
        self.setMinimumSize(995, 350)
        #self.setMinimumWidth(995)
        
        #for tableView in (self.ventaVariosTableView, self.ventaPanesTableView):
            #tableView.setItemDelegate(delegate)
            #self.modelo.tableView = tableView
        
            #newIndex = tableView.model().index(0, 1)
            #self.saldosTableView.selectionModel().select(newIndex, _qc.QItemSelectionModel.Select)
            #tableView.setCurrentIndex(newIndex)
            
        self.filterReturn2 = FilterReturn()
        self.ventaPanesTableView.installEventFilter(self.filterReturn2)
        self.connect(self.ventaPanesTableView, _qc.SIGNAL("enterPressed()"), 
                         self.cambiarFilaPan)
        
        #if not MAC: 
        #   self.guardarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
        #    self.cerrarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            
        self.lstLabelTotales = [self.lblTotVarios, self.lblTotPan, self.lblTotal]
        self.lstTotales = [0.0, 0.0, 0.0]
                
        self.fechaDateEdit.setDate(datetime.date.today())
        
        self.filterReturn3 = FilterReturn()
        self.fechaDateEdit.installEventFilter(self.filterReturn3)
        self.connect(self.fechaDateEdit, _qc.SIGNAL("enterPressed()"), 
                     self.ventaVariosTableView.setFocus)
        
        self.guardarPushButton.clicked.connect(self.guardarDatos)
        
        #self.fechaDateEdit.setFocus()
        
        self.setTitFecha(self.fechaDateEdit.date())
        self.fechaDateEdit.dateChanged.connect(self.buscarDatos)
        
        self.filterReturn = FilterReturn()
        self.ventaVariosTableView.installEventFilter(self.filterReturn)
        self.connect(self.ventaVariosTableView, _qc.SIGNAL("enterPressed()"), 
                     self.cambiarFilaVarios)
        
        self.cambiarTotales()
        self.setVendedoresExternos()
        #self.modelo.buscarDatosVentas(self.data())
        self.ventaVariosTableView.setFocus()
        self.ventaVariosTableView.selectionModel().setCurrentIndex(
                        self.ventaVariosTableView.model().index(0,1), 
                                       _qg.QItemSelectionModel.Toggle)
        
        #self.layout().setSizeConstraint(_qc.Qt.SetFixedSize)
        
        #self.generarReporte()
        self.updateUi()
        
    def keyPressEvent(self, e):
        if e.key() == _qc.Qt.Key_Escape:
            e.ignore()
        else:
            _qg.QDialog.keyPressEvent(self, e)
            #e.accept()
        
    @_qc.pyqtSlot(int)
    def on_vendedoresComboBox_currentIndexChanged(self, index):
        if index >= 0:
            self.vendedorExt = self.vendedoresComboBox. \
                            model().getData(index)
        print("BUSCAR A");
        self.buscarDatos(self.fechaDateEdit.date())
        print("BUSCAR D");
        self.updateUi()
        
        
    def avisarCambiosDatos(self, categoria, total):
        self.lstTotales[categoria - 1] = total
        self.lstTotales[2] = self.lstTotales[0] + self.lstTotales[1]
        self.cambiarTotales()
        
    def cambiarTotales(self):
        for i in range(len(self.lstLabelTotales)):
            self.lstLabelTotales[i].setText('$ ' + unicode(self.lstTotales[i]))

        
    def setTitFecha(self, fecha):
        self.setWindowTitle(u"Venta diaria - " + ManejaFechas.date2Str(fecha.toPyDate()))
        
    @_qc.pyqtSlot()
    def on_cerrarPushButton_clicked(self):
        self.parentWidget().close()
        _qg.QDialog.accept(self)

    @_qc.pyqtSlot()
    def cambiarFilaVarios(self):
        index = self.ventaVariosTableView.currentIndex()
        next_index =  self.ventaVariosTableView.model().index(index.row() + 1, index.column())
        
        if index.row() + 1 >= self.modelo.modeloVarios.rowCount():
            next_index =  self.ventaVariosTableView.model().index(0, index.column())
        
        self.ventaVariosTableView.setCurrentIndex(next_index)
        
    @_qc.pyqtSlot()
    def cambiarFilaPan(self):
        index = self.ventaPanesTableView.currentIndex()
        next_index =  self.ventaPanesTableView.model().index(index.row() + 1, index.column())
        
        if index.row() + 1 >= self.modelo.modeloPan.rowCount():
            next_index =  self.ventaPanesTableView.model().index(0, index.column())
        
        self.ventaPanesTableView.setCurrentIndex(next_index)
        
 
    @_qc.pyqtSlot()       
    def guardarDatos(self):
        tit = u"Venta diaria"
        ok, msg = self.modelo.guardarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
            self.ventaVariosTableView.scrollToTop()
            self.ventaPanesTableView.scrollToTop()
            self.ventaVariosTableView.setFocus()
            self.ventaVariosTableView.selectionModel().setCurrentIndex(
                        self.ventaVariosTableView.model().index(0,1), 
                                       _qg.QItemSelectionModel.Toggle)
            #self.ventaVariosTableView.selectionModel().setCurrentIndex(
            #           self.ventaVariosTableView.model().index(0,1), 
            #                   _qg.QItemSelectionModel.SelectCurrent)
        else:
            _qg.QMessageBox.information(self, tit, msg)
            
    def closeEvent(self, event):
        self.modelo.cerrarSesionDAO()
            
    @_qc.pyqtSlot("QDate")        
    def buscarDatos(self, fecha=None):
        tit = u"Venta diaria" #+ fecha
        self.setTitFecha(fecha)
        
        for label in self.lstLabelTotales:
            label.setText('$ 0.0')
        #ok, msg = self.modelo.buscarDatosVentas(self.data())
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        ok, msg = self.modelo.buscarDatosVentas(self.data())
        _qg.QApplication.restoreOverrideCursor()
        self.updateUi()
        if not ok:
            _qg.QMessageBox.information(self, tit, msg)
            
    def generarReporte(self):
        self.pushButtonImprimir.setEnabled(False)
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        import tempfile
        file = tempfile.mktemp(".xls")
        open(file, "w")
        #file = os.curdir + variables.PATH_REPORTES + variables.FILE_REPORTE_VENTA_DIARIA
        
        lst_header, array_datos, lst_resaltados = self.modelo.datos2Array()#self.modelo.datos2Array()
        
        edit = EditCalcVentaDiaria(file, array_datos, lst_header)
        edit.lst_resaltados = lst_resaltados
        edit.title = [u'VENTA DIARIA | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()), 
                      u'VENDEDOR: ' + self.vendedorExt.__str__()]
        
        edit.style_header = variables.STYLE_HEADER_VENTA_DIARIA
        edit.basic_style = variables.STYLE_VENTA_DIARIA
        
        edit.abrirArchivo()
        edit.crearHoja()
        edit.sheet.portrait = False
        edit.setFooter(u'')
        #edit.setFooter(u'&F | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        #edit.setFooter(u'Venta diaria | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        edit.setWidthCol((50 * 256, 
                          7 * 256, 7 * 256, 7 * 256, 7 * 256, 7 * 256, 7 * 256,
                          9 * 256, 9 * 256, 9 * 256, 10 * 256))
        edit.escribirArchivo()
        edit.salvarArchivo()
        
        #os.startfile(edit.fileCalc)
        
        self.imprimirReporte(edit.fileCalc)
        
        _qg.QApplication.restoreOverrideCursor()
        self.pushButtonImprimir.setEnabled(True)
        
    def imprimirReporte(self, file):
        #os.startfile(file)
        printer.defaultPrinter(file)
        
    def data(self):
        return [self.fechaDateEdit.date().toPyDate(), self.vendedorExt]
    
    def resetValues(self):
        self.limpiarTabla()
        self.updateUi()
        self.fechaDateEdit.setFocus()
        
    def limpiarTabla(self):
        self.modelo.limpiarValores()
        
    def setVendedoresExternos(self):
        dao = DAOVendedor(False)
        lstVendedoresExt = dao.getAll(VendedorExterno)
        modeloVendedoresExt = DatosListModel(lstVendedoresExt, False) \
                                if len(lstVendedoresExt) > 0 else None
        self.vendedoresComboBox.setModel(modeloVendedoresExt)
        self.vendedorExt = self.vendedoresComboBox. \
                model().getData(0)
                
    def resizeColumns(self, columns):
        for column in columns:
            self.ventaVariosTableView.resizeColumnToContents(column)
            self.ventaPanesTableView.resizeColumnToContents(column)
            
    def showVentana(self, msg):
        _qg.QMessageBox.information(None, "Devoluciones", msg)
        
    def updateUi(self):
        pass
        #enable = True
        #self.guardarPushButton.setEnabled(enable)
        #self.resizeColumns([tmVentaDiariaVariedades.NOM_PROD, 
         #           tmVentaDiariaVariedades.CARGA_1, tmVentaDiariaVariedades.CARGA_2, 
          #          tmVentaDiariaVariedades.CARGA_3, tmVentaDiariaVariedades.CARGA_4, 
           #         tmVentaDiariaVariedades.CARGA_5, tmVentaDiariaVariedades.CARGA_6, 
            #        tmVentaDiariaVariedades.TOTAL_CANT, tmVentaDiariaVariedades.DEVOL, 
             #       tmVentaDiariaVariedades.TOT_NETO_CANT, 
              #      tmVentaDiariaVariedades.PRECIO_VENTA, 
               #     tmVentaDiariaVariedades.TOT_VENTA])