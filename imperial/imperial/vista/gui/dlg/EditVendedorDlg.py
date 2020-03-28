#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model import models
from imperial.vista.gui.dlg.NewVendedorDlg import NewVendedorDlg
import PyQt4.QtGui as _qg

class EditVendedorDlg(NewVendedorDlg):
    u"""Diálogo para editar los datos de un rubro."""
    
    def __init__(self, modelo=None, parent=None):
        super(EditVendedorDlg, self).__init__(modelo, parent)

        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Editar")
        
        self.setWindowTitle(u'Editar vendedor')
        
    def setData(self, listaData):
        self.lineVendedor.setText(str(listaData[models.NOMBRE_VEND]))
        self.checkVendedor.setChecked(listaData[models.ES_VENDEDOR])