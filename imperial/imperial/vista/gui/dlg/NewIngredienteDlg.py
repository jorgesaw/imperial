#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model.datamodel.dataModelExtend import DataModelExtend
from imperial.model.models import Ingrediente
from imperial.vista.gui.dlg.ui_dlgNuevoIngrediente import Ui_DlgNuevoIngrediente
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class NewIngredienteDlg(_qg.QDialog, Ui_DlgNuevoIngrediente):
    def __init__(self, modelo=None, parent=None):
        u"""Diálogo para agregar un nuevo ingrediente."""
        super(NewIngredienteDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.modelo = modelo
        
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Agregar")
        self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setText("&Cancelar")
        
        self.dsPrecio.setLocale(_qc.QLocale('QLatin1Char'))
        
        #if not MAC: 
        #   self.buttonBox.button(_qg.QDialogButtonBox.Ok).setFocusPolicy(_qc.Qt.NoFocus)
        #  self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setFocusPolicy(_qc.Qt.NoFocus)
        self.cant_unidad = Ingrediente.CANT_UNIDAD_KG_LTS #Se pesa en gramos/cm3.
        
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_lineIngred_textEdited(self, text):
        self.updateUi()
        
    @_qc.pyqtSlot(float)
    def on_dsPrecio_valueChanged(self, value):
        self.updateUi()
        
    @_qc.pyqtSlot()
    def on_radioOtros_clicked(self):
        self.habilitarRadios(False)
        
    @_qc.pyqtSlot()
    def on_radioKg_clicked(self):
        self.habilitarRadios(True)
        self.checkGrmsCm3(True)
        
    @_qc.pyqtSlot()
    def on_radioLts_clicked(self):
        self.habilitarRadios(True)
        self.checkGrmsCm3(True)
        
    #@_qc.pyqtSlot()
    #def on_radioKgLts_clicked(self):
    #   self.cant_unidad = Ingrediente.CANT_UNIDAD_KG_LTS_X1
        
    #@_qc.pyqtSlot()
    #def on_radioGrmsCm3_clicked(self):
    #   self.cant_unidad = Ingrediente.CANT_UNIDAD_KG_LTS
        
    def habilitarRadios(self, b):
        self.radioKgLts.setEnabled(b)
        self.radioGrmsCm3.setEnabled(b)
    
    def checkGrmsCm3(self, b):
        #self.cant_unidad = Ingrediente.CANT_UNIDAD_KG_LTS_X1 #uPesa por kg/l
        #if b:
        #   self.cant_unidad = Ingrediente.CANT_UNIDAD_KG_LTS #uPesa por grms/cm3
            
        self.radioGrmsCm3.setChecked(b)
        self.radioKgLts.setChecked(not b)
        
    def data(self):
        u"""Los datos a pasar son:
        NOMBRE_INGREDIENTE: STRING
        PRECIO_INGREDIENTE: FLOAT
        UNIDAD: kg, lts, otros
        CANT_UNIDAD: Si es otros pasamos el numero de unidades de spinBoxCantidad, 
        si es kg o lts especificamos si vamos a tomar el peso en sub_unidades de 
        gramos/cm3, o bien en unidades de kg/lts. 
        Tener en cuenta que esto último se utiliza para ingresar las unidades en la 
        ventana de costo. La harina se ingresa por kg. En cambio la sal por grms.
        
        Valores:
        UNIDAD_KG = 0
        UNIDAD_LTS = 1
        UNIDAD_OTROS = 2
        
        CANT_UNIDAD_KG_LTS = -1
        CANT_UNIDAD_KG_LTS_X1 = 0
    
        LST_UNIDADES = [u'Kg.', u'Lts.', u'Unidades']
        LST_MULTIPLO_UND = ['grs.', 'cm3', 'und.']
        LST_CANT_UNIDADADES = [1000, 1] Equivalencias por kilo/litro o gramo/cm3.
        """
        
        datos = [unicode(self.lineIngred.text()), 
                self.dsPrecio.value(), ]
                
        valor_unidad = Ingrediente.UNIDAD_KG
        self.cant_unidad = Ingrediente.CANT_UNIDAD_KG_LTS
        
        if self.radioOtros.isChecked():
            valor_unidad = Ingrediente.UNIDAD_OTROS
            self.cant_unidad = self.spinBoxCantidad.value()
        else:
            if self.radioLts.isChecked():
                valor_unidad = Ingrediente.UNIDAD_LTS
            if self.radioKgLts.isEnabled() and self.radioKgLts.isChecked():
                self.cant_unidad = Ingrediente.CANT_UNIDAD_KG_LTS_X1

        datos.append(valor_unidad)
        datos.append(self.cant_unidad)
            
        return datos
                    
        
    def accept(self):
    #    if self.modelo.datosByCol(unicode(self.lineIngred.text()))[0]:
     #       _qg.QMessageBox.warning(self, "Agregar datos", 
      #                              DataModelExtend.LST_MSG[DataModelExtend.MSG_ERROR_SAVE_DATO_REPETIDO])
       #     self.lineIngred.setFocus()
        #else:
        _qg.QDialog.accept(self)
            
    def guardarDatos(self):
        tit = u"Nuevo Ingrediente"
        ok, msg = self.modelo.guardarDatos(self.data())
        if ok:
            _qg.QMessageBox.information(self, tit, msg)
            self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(False)
            self.resetValues()
        else:
            _qg.QMessageBox.information(self, tit, msg)
        
    def resetValues(self):
        self.lineIngred.clear()
        self.dsPrecio.setValue(0.0)
        self.spinBoxCantidad.setValue(1)
        self.radioKg.setChecked(True)
        
    def updateUi(self):
        enable = not (self.lineIngred.text().isEmpty() or \
                      self.dsPrecio.value() == 0)
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(enable)