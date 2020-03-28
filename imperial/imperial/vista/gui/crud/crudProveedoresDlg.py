#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.vista.crud.CRUD import CRUD
from imperial.model.modeltable.delegate.delegate import ProveedorDelegate
from imperial.vista.gui.dlg.EditProveedorDlg import EditProveedorDlg
from imperial.vista.gui.dlg.NewProveedorDlg import NewProveedorDlg
import PyQt4.QtCore as _qc

class CrudProveedoresDlg(CRUD):
    u"""Dialogo CRUD de rubros."""

    def __init__(self, modelo, parent=None):
        super(CrudProveedoresDlg, self).__init__(modelo, parent)

        self.datosTableView.setItemDelegate(ProveedorDelegate())
        self.updateUi()
        #CRUD.resizeColumns(self, (ModeloDatosCiudad.NOMBRE, ModeloDatosCiudad.COD_POSTAL,
        #ModeloDatosCiudad.DDN, ModeloDatosCiudad.PROVINCIA))
        self.datosTableView.setStyleSheet('background-color: rgb(153, 153, 80);')
        
        #self.datosTableView.horizontalHeader().setResizeMode(_qg.QHeaderView.Stretch)
        self.datosTableView.horizontalHeader().setStretchLastSection(True)
        self.setMinimumSize(1000, 480)
        
        self.ciudadesLabel.setText('PROVEEDORES')
        self.setWindowTitle("CRUD Proveedores")
        CRUD.listData(self)

    @_qc.pyqtSlot()
    def on_newPushButton_clicked(self):
        addDlg = NewProveedorDlg()
        CRUD.addData(self, addDlg)
        self.modelo.sortByColumn()

    @_qc.pyqtSlot()
    def on_editPushButton_clicked(self):
        editDlg = EditProveedorDlg()
        CRUD.editData(self, editDlg)
        self.modelo.sortByColumn()
        
    @_qc.pyqtSlot()
    def on_listPushButton_clicked(self):
        CRUD.listData(self)

    @_qc.pyqtSlot()
    def on_searchPushButton_clicked(self):
        from imperial.vista import factoria
        CRUD.searchData(self, factoria.SEARCH_PROVEEDORES)

    def updateUi(self):
        CRUD.updateUi(self)