#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from imperial.vista.gui.dlg import ui_dlgProgressFile
import PyQt4
import datetime

class ProgressFileDlg(QDialog,
                      ui_dlgProgressFile.Ui_DlgProgressFile):
    u"""Diálogo para buscar una ciudad específica."""
    def __init__(self, parent=None):
        super(ProgressFileDlg, self).__init__(parent)

        #Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.setWindowTitle(u'..::Copia de seguridad::..')
        #self.modelo.restaurarDb()

    @pyqtSignature("int")
    def on_fileProgressBar_valueChanged(self, value):
        self.fileProgressBar.setValue(value)