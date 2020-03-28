#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 22/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model.models import Category
from imperial.vista.gui.dlg.ui_dlgNuevoRubro import Ui_DlgNuevoRubro
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
from imperial.dao.DAOCategory import DAOCategory

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class NewCategoryDlg(_qg.QDialog, Ui_DlgNuevoRubro):
    u"""Diálogo para agregar un nuevo rubro."""
    
    def __init__(self, modelo=None, parent=None):
        super(NewCategoryDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Agregar")
        self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setText("&Cancelar")
        
        if not MAC: 
            self.buttonBox.button(_qg.QDialogButtonBox.Ok).setFocusPolicy(_qc.Qt.NoFocus)
            self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setFocusPolicy(_qc.Qt.NoFocus)
                
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_lineRubro_textEdited(self, text):
        self.updateUi()
        
    def data(self):
        return [unicode(self.lineRubro.text()),]
        
    def accept(self):
        if self.modelo:
            self.guardarDatos()
        else:
            _qg.QDialog.accept(self)
        
    def guardarDatos(self):
        tit = u"Nuevo Rubro"
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
        enable = not (self.lineRubro.text().isEmpty())
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(enable)