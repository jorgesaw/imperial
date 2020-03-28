#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.vista.factoria.ventanasGui import VentanasGui
from imperial.vista import factoria

class MostrarVentanaGui(VentanasGui):
    u"""Clase factoría para crear gui de CRUD genérico."""
    
    def __init__(self, tipo, parent=None, mapParam=None):
        super(MostrarVentanaGui, self).__init__(parent, mapParam)
        self.tipo = tipo
        
    def prepararVentana(self):
        dicDatos = factoria.getDicConfigClases(self.tipo)
        
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
            
        ventana = dicDatos.get('ventana')(modeloTabla, 
                                            self._parent)
        ventana.move(0, 0)
        return ventana
    
    def tipoDlg(self):
        raise "Método sin implementar."