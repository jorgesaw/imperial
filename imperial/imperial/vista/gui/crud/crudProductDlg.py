#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.Actions import createAction, addActions
from imperial.core.gui.MsgBox import MsgBox
from imperial.core.vista.crud.CRUD import CRUD
from imperial.model import models
from imperial.model.modeltable.delegate.delegate import ProductoDelegate
from imperial.model.modeltable.modeldatatable.mdtProduct import \
    ModeloDatosTablaProduct
from imperial.vista.gui.dlg.EditProductDlg import EditProductDlg
from imperial.vista.gui.dlg.NewProductDlg import NewProductDlg
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

class CrudProductDlg(CRUD):
    u"""Dialogo CRUD de productos."""

    def __init__(self, modelo, parent=None):
        super(CrudProductDlg, self).__init__(modelo, parent)

        #self.datosTableView.setItemDelegate(CiudadesDelegate())
        self.datosTableView.setItemDelegate(ProductoDelegate(self))
        self.datosTableView.setStyleSheet('background-color: rgb(153, 153, 80);')
        #CRUD.resizeColumns(self, (ModeloDatosCiudad.NOMBRE, ModeloDatosCiudad.COD_POSTAL,
        #ModeloDatosCiudad.DDN, ModeloDatosCiudad.PROVINCIA))
        
        #self.datosTableView.horizontalHeader().setResizeMode(_qg.QHeaderView.Stretch)
        
        
        lst_width_col = [360, 70, 270, 60, 70, 70]
        for i, width in enumerate(lst_width_col):
            self.datosTableView.setColumnWidth(i, width)
        
        self.datosTableView.horizontalHeader().setStretchLastSection(True)
        self.setMinimumSize(990, 550)
        
        self.editAction = createAction(self, "&Edit", slot=self.on_editPushButton_clicked,
                                       shortcut=_qg.QKeySequence("Ctrl+E"), signal="triggered()")
        self.removeAction = createAction(self, "&Remove", slot=self.on_delPushButton_clicked,
                                         shortcut=_qg.QKeySequence("Del"), signal="triggered()")
        
        addActions(None, self, (self.editAction, self.removeAction))
        
        self.updateUi()
        self.ciudadesLabel.setText('PRODUCTOS')
        self.setWindowTitle("CRUD Productos")
        CRUD.listData(self)
        self.modelo.sortByColumn()
    
    def on_datosTableView_clicked(self, index):
        if index.column() == ModeloDatosTablaProduct.EDITAR:
            self.on_editPushButton_clicked()
        elif index.column() == ModeloDatosTablaProduct.ELIMINAR:
            self.on_delPushButton_clicked()

    @_qc.pyqtSlot()
    def on_newPushButton_clicked(self):
        addDlg = NewProductDlg(self.modelo)
        CRUD.addData(self, addDlg)
        self.modelo.sortByColumn()

    @_qc.pyqtSlot()
    def on_editPushButton_clicked(self):
        editDlg = EditProductDlg(self.modelo)
        #Comprobar si existe un precio guardado en la fecha seleccionada.
        index = self.datosTableView.currentIndex()
        if not index.isValid():
            _qg.QMessageBox.information(self, "Editar Datos",
                               u"Por favor seleccione una fila de la tabla para editar.")
            return
        row = index.row()
        lstData = self.modelo.datosModelo(row)
        editDlg.setData(lstData)
        editDlg.updateUi()
        r = editDlg.exec_()
        if r:
            lstDatos = editDlg.data()
            pos_precio = self.modelo.getPrecioByFechaHoy(row, models.PRECIO_PRODUCTO)
            if pos_precio != -1: #uYa existe un precio en el día de la fecha
                if not MsgBox.okToContinue(self, 'Actualizar precio', 
                                    'En la base de datos ya existe un precio con la\n' +
                                    'fecha de hoy para ese producto.\n' +
                                    '¿Desea actualizarlo?'):
                    return
                lstDatos += [False, pos_precio] #uActualizar el precio
            else:
                lstDatos += [True, pos_precio]#Agrega uno nuevo
            ok, msg = self.modelo.editRows(index, lstDatos)
            _qg.QMessageBox.information(self, "Editar Datos", msg)
        #CRUD.editData(self, editDlg)
        self.modelo.sortByColumn()

    @_qc.pyqtSlot()
    def on_listPushButton_clicked(self):
        CRUD.listData(self)

    @_qc.pyqtSlot()
    def on_searchPushButton_clicked(self):
        from imperial.vista import factoria
        CRUD.searchData(self, factoria.SEARCH_PROD)

    def updateUi(self):
        CRUD.updateUi(self)