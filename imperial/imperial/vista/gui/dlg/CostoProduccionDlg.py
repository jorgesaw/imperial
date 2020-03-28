#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 06/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.filterReturn import FilterReturn
from imperial.core.model.listmodel.datosListModel import DatosListModel
from imperial.core.util import printer
from imperial.core.util.ManejaFechas import ManejaFechas
from imperial.dao.DAOProducto import DAOProducto
from imperial.model.informes.EditCalc import EditCalcCostoProd
from imperial.model.listmodel.datosListModel import DatosListModelProd
from imperial.model.models import Product
from imperial.model.modeltable.tableModelCostosProd import CostosProdDelegate
from imperial.vista.gui.dlg.ui_dlgCostoProduccion import Ui_DlgCostoProduccion
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime
import os
import tempfile

class CostoProduccionDlg(_qg.QDialog, Ui_DlgCostoProduccion):
    def __init__(self, modelo=None, parent=None):
        u"""Diálogo para manejar costos de producción por producto."""
        
        super(CostoProduccionDlg, self).__init__(parent)
        
        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        self.producto = None
        
        self.tableViewIngredientes.setModel(modelo)
        self.tableViewIngredientes.setItemDelegate(CostosProdDelegate(self))
        self.modelo.tableView = self.tableViewIngredientes
        
        self.tableViewIngredientes.horizontalHeader().setStretchLastSection(True)
        
        lstWidthTablaIngred = (280, 70, 70, 90, 60)
        for i, width in enumerate(lstWidthTablaIngred):
            self.tableViewIngredientes.setColumnWidth(i, width)
            
        self.listViewCostosProd.setMaximumWidth(350)
        
        #uLe pasamos la vista para avisar de cambios en la tabla.
        self.modelo.vista = self
        
        self.fechaCosto.setDate(datetime.date.today())
        self.fecha_costo = datetime.date.today()
        
        newIndex = self.tableViewIngredientes.model().index(0, 1)
        #self.saldosTableView.selectionModel().select(newIndex, _qc.QItemSelectionModel.Select)
        self.tableViewIngredientes.setCurrentIndex(newIndex)
        
        self.cadena_sin_costos = u'Sin calculo de costos'
        
        self.filterReturn = FilterReturn()
        self.tableViewIngredientes.installEventFilter(self.filterReturn)
        self.connect(self.tableViewIngredientes, _qc.SIGNAL("enterPressed()"), 
                     self.cambiarFila)
        
        #self.fechaDateEdit.installEventFilter(self.filterReturn)
        #self.connect(self.fechaDateEdit, _qc.SIGNAL("enterPressed()"), 
        #            self.tableViewIngredientes.setFocus)
        
        self.agregarLstProductos()
        
        #self.fechaCosto.dateChanged.connect(self.cambiarProducto)
        
        self.listViewProductos.clicked.connect(self.cambiarProducto)
        #self.listViewCostosProd.clicked.connect(self.cambiarCostoxProd)
        self.NuevoPushButton.clicked.connect(self.guardarNuevoCosto)
        
        self.btnGrabarDatos.clicked.connect(self.guardarDatos)
        self.btnAddIngrediente.clicked.connect(self.addIngrediente)
        self.btnDelIngrediente.clicked.connect(self.delIngrediente)
        self.lineEditGastosPro.textEdited.connect(self.mostrarTotal)
        self.lineEditCant.textEdited.connect(self.mostrarTotal)
        self.btnImprimir.clicked.connect(self.generarReporte)
        
        self.tableViewIngredientes.horizontalHeader().setStretchLastSection(True)
        self.setMinimumWidth(950)
        #self.setMinimumHeight(600)
        
        self.limpiarTextos()
        self.updateUi()
        
    def keyPressEvent(self, e):
        if e.key() == _qc.Qt.Key_Escape:
            e.ignore()
        else:
            _qg.QDialog.keyPressEvent(self, e)
            #e.accept()
            
    def cambiarCostoxProd(self):
        self.NuevoPushButton.setEnabled(True)
        
        tit = u"Costo producción"
        #Busco la fecha del último costo en la lista de costos
        #ultima_actualizacion = self.listViewCostosProd.model().getData(0).__str__()
        ultima_actualizacion = self.listViewCostosProd.model().getData(
                                self.listViewCostosProd.currentIndex().row()).__str__()
        if unicode(ultima_actualizacion) == unicode(self.cadena_sin_costos):
            _qg.QMessageBox.information(self, tit, u'No hay datos para mostrar.')
            self.NuevoPushButton.setEnabled(True)
            return
        
        self.fecha_costo = ManejaFechas.str2Date(ultima_actualizacion, '%Y-%m-%d')
        
        if self.fecha_costo == datetime.date.today():
            self.NuevoPushButton.setEnabled(False)
        
        self.buscarDatos()
        
    def setTotalCosto(self, costo):
        self.lineEditCostoIngredientes.setText('{}'.format(costo))
        self.mostrarTotal('')
        
    @_qc.pyqtSlot()
    def on_btnCerrar_clicked(self):
        self.parentWidget().close()
        _qg.QDialog.accept(self)
        
    @_qc.pyqtSlot("QString")
    def mostrarTotal(self, cadena=None):
        self.totalCosto = 0
    
        if not self.lineEditGastosPro.text().isEmpty():
            gasto = self.lineEditGastosPro.text()
            gasto = gasto.replace(',', '.')
            costoProd = float(gasto)
            if not self.lineEditCant.text().isEmpty():
                if float(self.lineEditCant.text()) > 0:
                    cant = float(self.lineEditCant.text())
                    
                    self.totalCosto = round((self.modelo.getTotalCostoProd() + costoProd) /\
                                   cant, 2)
        
        self.lineEditTotal.setText('{}'.format(self.totalCosto))
                
    
    @_qc.pyqtSlot()       
    def cambiarProducto(self):
        if self.listViewProductos.currentIndex().row() != -1:
            self.resetValues()
            self.buscarDatos()
    
    @_qc.pyqtSlot()
    def delIngrediente(self):
        index = self.tableViewIngredientes.currentIndex()
        if not index.isValid():
            _qg.QMessageBox.information(self, "Eliminar Datos",
                               u"Por favor seleccione una fila de la tabla para eliminar.")
            return
        row = index.row()
        if _qg.QMessageBox.question(self, "Eliminar Datos",
                                u"¿Desea eliminar el ingrediente seleccionado?\n",
                                _qg.QMessageBox.Yes|_qg.QMessageBox.No) == _qg.QMessageBox.No:
            return
        ok, msg = self.modelo.removeRows(row)
        #_qg.QMessageBox.information(self, "Eliminar datos", msg)
        
    @_qc.pyqtSlot()
    def addIngrediente(self):
        self.modelo.addIngrediente()
        
    def agregarLstProductos(self):
        #dao = DAOProducto()
        lstProductos = self.modelo.getAllProducts()
        
        modeloProductos = DatosListModelProd(lstProductos, False) if len(lstProductos) > 0 \
                         else None
        
        self.listViewProductos.setModel(modeloProductos)
        
        self.agregarCostosxProd(lstProductos[0].colCostosProd)
        
    def agregarCostosxProd(self, lstCostosxProd):
        if len(lstCostosxProd) > 0:
            lstModeloCostosxProd = []

            for costo in lstCostosxProd:
                lstModeloCostosxProd.append(costo.fecha_ingreso)
                lstModeloCostosxProd.sort()
                modeloCostosxProd = DatosListModel(lstModeloCostosxProd, False)
        else:
            modeloCostosxProd = DatosListModel([self.cadena_sin_costos,], False)
        
        self.listViewCostosProd.setModel(modeloCostosxProd)
        
    def closeEvent(self, event):
        self.modelo.cerrarSesionDAO()
                
    def cambiarFila(self):
        index = self.tableViewIngredientes.currentIndex()
        next_index =  self.tableViewIngredientes.model().index(index.row() + 1, index.column())
        
        if index.row() + 1 >= self.modelo.rowCount():
            next_index =  self.tableViewIngredientes.model().index(0, index.column())
        
        self.tableViewIngredientes.setCurrentIndex(next_index)
    
    @_qc.pyqtSlot()    
    def guardarNuevoCosto(self):
        self.fecha_costo = datetime.date.today()
        #self.modelo.datosNuevos = True
        self.modelo.crearDatos(self.data())
        
        tit = u"Costo producción"
        ok, msg = self.modelo.guardarDatos(self.data())
        
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
        else:
            _qg.QMessageBox.information(self, tit, msg)
        
    @_qc.pyqtSlot()
    def guardarDatos(self):
        tit = u"Costo producción"
        ok, msg = self.modelo.guardarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
        else:
            _qg.QMessageBox.information(self, tit, msg)
            
    @_qc.pyqtSlot("QDate")        
    def buscarDatos(self):
        self.NuevoPushButton.setEnabled(True)
        
        tit = u"Costo producción"
        
        #Muestro la lista de costos x producto si existen.
        self.agregarCostosxProd(self.data()[4].colCostosProd)
        self.listViewCostosProd.selectionModel().setCurrentIndex(
                                    self.listViewCostosProd.model().index(0, 0), 
                                       _qg.QItemSelectionModel.Toggle)
        
        if self.listViewCostosProd.currentIndex().isValid():
            ultima_actualizacion = self.listViewCostosProd.model().getData(
                                self.listViewCostosProd.currentIndex().row()).__str__()
            
            if ultima_actualizacion != self.cadena_sin_costos:
                if ManejaFechas.str2Date(ultima_actualizacion, '%Y-%m-%d') == datetime.date.today():
                    self.NuevoPushButton.setEnabled(False)
            
        ok, msg = self.modelo.buscarDatos(self.data())
        
        if ok:
            self.btnGrabarDatos.setEnabled(True)
        else:
            _qg.QMessageBox.information(self, tit, msg)
            self.btnGrabarDatos.setEnabled(False)
        
        self.updateUi()
        
    @_qc.pyqtSlot()       
    def nuevoCosto(self):
        self.resetValues()
        
    def data(self):
        return [self.fecha_costo, #self.fechaCosto.date().toPyDate(), 
                
                float(self.lineEditGastosPro.text()) if not \
                        self.lineEditGastosPro.text().isEmpty() else 0.0, 
                
                float(self.lineEditCant.text()) if not \
                        self.lineEditCant.text().isEmpty() else 0, 
                
                unicode(self.plainTEDesc.document().toPlainText()), 
                
                self.listViewProductos.model().getData(
                    self.listViewProductos.currentIndex().row())]
        
    def setData(self, lstDatos):
        self.lineEditGastosPro.setText('{}'.format(lstDatos[0]))
        self.lineEditCant.setText('{}'.format(lstDatos[1]))
        self.plainTEDesc.document().setPlainText(lstDatos[2])
        self.mostrarTotal('')
        
    def generarReporte(self):
        self.btnImprimir.setEnabled(False)
        _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
        
        file = tempfile.mktemp(".xls")
        open(file, "w")
        #file = os.curdir + variables.PATH_REPORTES + variables.FILE_REPORTE_SALDO
        
        lst_header, array_datos, lst_resaltados = self.modelo.datos2Array(self.totalCosto)
        
        edit = EditCalcCostoProd(file, array_datos, lst_header)
        edit.lst_resaltados = lst_resaltados
        edit.title = [u'COSTO DE PRODUCCIÓN | ' + ManejaFechas.date2Str(self.fecha_costo), 
                      u'PRODUCTO: ' + self.listViewProductos.model().getData(
                            self.listViewProductos.currentIndex().row()).__str__()]
        edit.abrirArchivo()
        edit.crearHoja()
        #edit.setFooter(u'&F | ' + ManejaFechas.date2Str(self.fechaDateEdit.date().toPyDate()))
        edit.setFooter(u'')
        edit.setWidthCol((42 * 256, 9 * 256, 12 * 256, 14 * 256, 12 * 256))
        edit.escribirArchivo()
        edit.salvarArchivo()
        
        #os.startfile(edit.fileCalc)
        self.imprimirReporte(edit.fileCalc)
        _qg.QApplication.restoreOverrideCursor()
        self.btnImprimir.setEnabled(True)
        
    def imprimirReporte(self, file):
        #os.startfile(file)
        printer.defaultPrinter(file)
    
    def resetValues(self):
        self.limpiarTabla()
        self.limpiarTextos()
        self.updateUi()
        self.fechaCosto.setFocus()
        
    def limpiarTextos(self):
        self.lineEditCostoIngredientes.setText('0.0')
        self.lineEditGastosPro.setText('0.0')
        self.lineEditCant.setText('0.0')
        self.lineEditTotal.setText('0.0')
        self.plainTEDesc.clear()
        
    def limpiarTabla(self):
        self.modelo.limpiarValores()
        
    def updateUi(self):
        enable = True#self.modelo.isDatosCosto()
        self.btnAddIngrediente.setEnabled(enable)
        self.btnDelIngrediente.setEnabled(enable)
        #self.btnGrabarDatos.setEnabled(enable)