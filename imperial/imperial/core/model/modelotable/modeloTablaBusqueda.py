#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.modelotable.modeloTabla import ModeloTabla

class ModeloTablaBusqueda(ModeloTabla):
    u"""Modelo para manejar los datos de forma tabular."""
    
    def __init__(self, modelo, modeloDatosTabla):
        super(ModeloTablaBusqueda, self).__init__(modelo, modeloDatosTabla)
        self.filaSeleccionada = -1
        
    def listarDatosBuscados(self, mapParam):
        retorno = 0
        datos, msg = self.modelo.getListaDatos(mapParam)
        if datos:
            self.datos = []
            self.datos = datos
            retorno = 1 # uHaydatos para mostrar.
            
        return (retorno > 0, msg) 

    def setFilaSeleccionada(self, fila):
        self.filaSeleccionada = fila
        
    def datosByCol(self, cadena_busqueda):
        self.datos_busqueda, msg = self.modelo.datosByCol({'COL': cadena_busqueda})
        
        return (self.datos_busqueda != None, msg)
        