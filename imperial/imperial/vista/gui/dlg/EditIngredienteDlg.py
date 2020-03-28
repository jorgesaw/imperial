#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model import models
from imperial.vista.gui.dlg.NewIngredienteDlg import NewIngredienteDlg
import PyQt4.QtGui as _qg
from imperial.model.models import Ingrediente

class EditIngredienteDlg(NewIngredienteDlg):
    u"""Diálogo para editar los datos de un ingrediente."""
    
    def __init__(self, modelo=None, parent=None):
        super(EditIngredienteDlg, self).__init__(modelo, parent)

        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Editar")
        
        self.setWindowTitle(u'Editar ingrediente')
        
    def setData(self, listaData):
        self.lineIngred.setText(unicode(listaData[models.NOM_INGRED]))
        self.dsPrecio.setValue(listaData[models.PRECIO_INGREDIENTE])
        radios = (self.radioKg, self.radioLts, self.radioOtros)
        
        radios[listaData[models.UNIDAD_INGRED]].setChecked(True)
        
        unidad_otros = (listaData[models.UNIDAD_INGRED] == Ingrediente.UNIDAD_OTROS)
        cant_unidad = listaData[models.CANT_UNIDAD_INGRED]
        
        self.habilitarRadios(not unidad_otros)
        
        if unidad_otros:
            self.spinBoxCantidad.setValue(cant_unidad)
        else:
            self.checkGrmsCm3(cant_unidad == Ingrediente.CANT_UNIDAD_KG_LTS)