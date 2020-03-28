#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.vista.gui.dlg.NewProductDlg import NewProductDlg
import PyQt4.QtGui as _qg
from imperial.model import models

class EditProductDlg(NewProductDlg):
    u"""Diálogo para editar los datos de una producto."""
    
    def __init__(self, modelo=None, parent=None):
        super(EditProductDlg, self).__init__(modelo, parent)

        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Editar")
        
        self.setWindowTitle(u'Editar producto')
        
    def setData(self, listaData):
        self.lineNombre.setText(unicode(listaData[models.NAME]))
        #self.lineCod.setText(listaData[models.CODE])
        
        #self.lineCodExt.setText('')
        #if listaData[models.EXT_CODE] != None:
         #   self.lineCodExt.setText(str(listaData[models.EXT_CODE]))

        self.dSpinBoxPrecio.setValue(listaData[models.PRICE])
        #self.dSpinBoxPrecioCompra.setValue(listaData[models.BUY_PRICE])
        #self.spinStock.setValue(listaData[models.STOCK])
        #self.spinStockMin.setValue(listaData[models.MIN_STOCK])
        #self.spinStockIdeal.setValue(listaData[models.IDEAL_STOCK])
        
        self.lineDesc.setText(unicode(listaData[models.DESCRIPTION]))
        self.categoria = listaData[models.CATEGORIA_PROD]
        self.comboRubros.setCurrentIndex(listaData[models.CATEGORIA_PROD] - 1)
        #self.category = listaData[models.CATEGORY]
        
        #rows = self.comboRubro.model().rowCount()
        #for index in range(rows):
         #   categoryCombo = str(self.comboRubro.model().getData(index))
          #  if self.category.name == categoryCombo:
           #     self.comboRubro.setCurrentIndex(index)
            #    break