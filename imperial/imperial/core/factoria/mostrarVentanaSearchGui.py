#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.vista.factoria.BusquedaGui import BusquedaGui

class MostrarVentanaSearchGui(BusquedaGui):
    u"""Clase factoría para crear gui de búsqueda genérico."""
    
    def __init__(self, tipo, parent=None, mapParam=None):
        super(MostrarVentanaSearchGui, self).__init__(parent, mapParam)
        self.tipo = tipo
        
        self.setDatoBuscado(self.prepararVentana())
        
    def prepararVentana(self):
        from imperial.vista import factoria
        dicDatos = factoria.getDicConfigClasesSearch(self.tipo)
        
        claseModelo = dicDatos.get('clase_modelo')
        dao = dicDatos.get('dao')(False)
        modelo = dicDatos.get('modelo')(dao, claseModelo)
    
        modeloDatosTabla = None    
        mt = dicDatos.get('modelo_tabla')
    
        if mt:
            mdt = dicDatos.get('modelo_datos_tabla')
            
            if mdt:
                modeloDatosTabla = mdt()
                modeloTabla = mt(modelo, modeloDatosTabla)
            else:
                modeloTabla = mt(modelo)
            
        else:
            modeloTabla = modelo
            
        busqDlg = dicDatos.get('ventana')(modeloTabla, 
                                            self.parent)
        
        ok = True
        if self.mapParam:
            ok = not self.mapParam.get('carga_previa')
            
            if self.mapParam.get('texto'):
                busqDlg.busquedaLineEdit.setText(self.mapParam.get('texto'))
                busqDlg.on_busquedaLineEdit_textEdited(self.mapParam.get('texto'))
                ok = busqDlg.buscarDato()
        if ok:
            r = busqDlg.exec_()
            if r: # uEligió algún dato.
                return modeloTabla.filaDato(modeloTabla.filaSeleccionada)
            return None
        return None
    
    def tipoDlg(self):
        raise "Método sin implementar."