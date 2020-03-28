#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 01/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.filterReturn import FilterReturn
from imperial.vista.gui.dlg import ui_dlgBusquedaGenerica
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class BusquedaGenericaDlg(_qg.QDialog,
                       ui_dlgBusquedaGenerica.Ui_DlgBusquedaGenerica):
    u"""Diálogo para buscar datos genéricos."""
    
    def __init__(self, modelo, parent=None):
        super(BusquedaGenericaDlg, self).__init__(parent)
        
        #Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)

        if not MAC: 
            self.buscarPushButton.setFocusPolicy(_qc.Qt.NoFocus)
            
        self.modelo = modelo
        self.busquedaTableView.setModel(self.modelo)
        #self.busquedaTableView.setAlternatingRowColors(True)
        self.busquedaTableView.setSelectionMode(_qg.QTableView.SingleSelection)
        self.busquedaTableView.setSelectionBehavior(_qg.QTableView.SelectRows)
        self.buscarPushButton.setDefault(True)
        
        self.busquedaTableView.doubleClicked[_qc.QModelIndex].connect(self.seleccionarDato)
        
        self.filterReturn = FilterReturn()
        self.busquedaTableView.installEventFilter(self.filterReturn)
        self.connect(self.busquedaTableView, _qc.SIGNAL("enterPressed()"), 
                     self.seleccionarDato)
        
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_busquedaLineEdit_textEdited(self, text):
        self.updateUi()


    @_qc.pyqtSlot("QModelIndex") 
    def seleccionarDato(self, index=None):
        if index:
            self.modelo.setFilaSeleccionada(index.row())
        else:
            self.modelo.setFilaSeleccionada(self.busquedaTableView.currentIndex().row())
            print("I love Qt")
        _qg.QDialog.accept(self)
        
    @_qc.pyqtSlot()
    def on_buscarPushButton_clicked(self):
        self.buscarDato()
        
    def buscarDato(self):
        ok, msg = self.modelo.listarDatosBuscados(
                {'DATO_BUSQUEDA': unicode(self.busquedaLineEdit.text())})
        if ok:
            self.modelo.updateTable()
        else:
            _qg.QMessageBox.information(self, "Listar Datos",
                msg)
        self.updateUi()
        return ok
    
    def updateUi(self):
        enable = not self.busquedaLineEdit.text().isEmpty()
        self.buscarPushButton.setEnabled(enable)