#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtGui as _qg
from imperial.model import models
from imperial.vista.gui.dlg.NewEgresoDlg import NewEgresoDlg

class EditEgresoDlg(NewEgresoDlg):
    u"""Diálogo para editar los datos de un rubro."""
    
    def __init__(self, modelo=None, parent=None):
        super(EditEgresoDlg, self).__init__(modelo, parent)

        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Editar")
        
        self.setWindowTitle(u'Editar egreso')
        
    def setData(self, listaData):
        self.lineRubro.setText(str(listaData[models.NAME]))