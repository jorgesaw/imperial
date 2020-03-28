#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 22/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.filterReturn import FilterReturn
from imperial.vista.gui.dlg.ui_dlgInformesSaldos import Ui_DlgInformesSaldos
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class InformesSaldoDlg(_qg.QDialog, Ui_DlgInformesSaldos):
    u"""Diálogo."""
    
    def __init__(self, modelo=None, parent=None):
        super(InformesSaldoDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        
        self.semanaTableView.setModel(self.modelo)
        self.desdeFechaDateEdit.setDate(datetime.date.today())
        self.modelo.buscarDatosSaldos(self.data())
        
        self.desdeFechaDateEdit.dateChanged.connect(self.buscarDatos)

    @_qc.pyqtSlot("QDate")        
    def buscarDatos(self, fecha):
        tit = u"Infome saldos"
        ok, msg = self.modelo.buscarDatosSaldos(self.data())
        if not ok:
            _qg.QMessageBox.information(self, tit, msg)
            
    def data(self):
        return [self.desdeFechaDateEdit.date().toPyDate(),]