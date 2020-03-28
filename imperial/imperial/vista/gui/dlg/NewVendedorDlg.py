#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 22/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model.datamodel.dataModelExtend import DataModelExtend
from imperial.model.models import Vendedor
from imperial.vista.gui.dlg.ui_dlgNuevoVendedor import Ui_DlgNuevoVendedor
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class NewVendedorDlg(_qg.QDialog, Ui_DlgNuevoVendedor):
    u"""Diálogo para agregar un nuevo vendedor."""
    
    def __init__(self, modelo=None, parent=None):
        super(NewVendedorDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Agregar")
        self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setText("&Cancelar")
        
        #if not MAC: 
         #   self.buttonBox.button(_qg.QDialogButtonBox.Ok).setFocusPolicy(_qc.Qt.NoFocus)
          #  self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setFocusPolicy(_qc.Qt.NoFocus)
          
        self.lblRubro.setText('Vendedor')
        self.setWindowTitle('Nuevo vendedor:')
                
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_lineVendedor_textEdited(self, text):
        self.updateUi()
        
    def data(self):
        return [unicode(self.lineVendedor.text()), self.checkVendedor.isChecked()]
        
    def accept(self):
        if self.modelo.datosByCol(unicode(self.lineVendedor.text()))[0]:
            _qg.QMessageBox.warning(self, "Agregar datos", 
                                    DataModelExtend.LST_MSG[DataModelExtend.MSG_ERROR_SAVE_DATO_REPETIDO])
            self.lineVendedor.setFocus()
        else:
            _qg.QDialog.accept(self)
        
    def guardarDatos(self):
        tit = u"Nuevo Vendedor"
        ok, msg = self.modelo.guardarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
            self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(False)
            self.resetValues()
        else:
            _qg.QMessageBox.information(self, tit, msg)
        
    def resetValues(self):
        self.lineRubro.clear()
        
    def updateUi(self):
        enable = not (self.lineVendedor.text().isEmpty())
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(enable)