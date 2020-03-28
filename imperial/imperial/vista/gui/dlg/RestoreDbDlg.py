#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4

import ui_dlgRestoreDb

class RestoreDbDlg(QDialog,
                      ui_dlgRestoreDb.Ui_DlgRestoreDb):
    u"""Diálogo para buscar una ciudad específica."""
    def __init__(self, parent=None):
        super(RestoreDbDlg, self).__init__(parent)

        #Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.updateUi()

    @pyqtSignature("")
    def on_restorePushButton_clicked(self):
        QDialog.accept(self)

    def data(self):
        return [unicode(self.copiasListWidget.currentItem().text()),]

    def setDatosItems(self, listaDatos):
        self.copiasListWidget.addItems(listaDatos)
        
    def updateUi(self):
        pass