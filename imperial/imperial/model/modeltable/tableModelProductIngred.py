#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 31/05/2015

@author: jorgesaw
'''
from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.modelotable.modeloTabla import ModeloTabla
from imperial.model import models
import datetime

class TableModelProductIngred(ModeloTabla):
    
    def __init__(self, modelo, modeloDatosTabla, parent=None):
        super(TableModelProductIngred, self).__init__(modelo, modeloDatosTabla, parent=None)
        
    def getPrecioByFechaHoy(self, row, tipo):
        dato = self.filaDato(row)
        
        if tipo == models.PRECIO_PRODUCTO:
            coleccion = dato.colPrecioProd
        elif tipo == models.PRECIO_INGREDIENTE:
            coleccion = dato.colPrecioIngred
            
        return self.buscarDatoByFecha(coleccion)
        
    def buscarDatoByFecha(self, colDatosPrecio):
        lenDatos = len(colDatosPrecio)
        hoy = datetime.date.today()
        
        for i in xrange(lenDatos):
            if colDatosPrecio[i].fecha_ingreso == hoy:
                return i
        return -1
    
    def datosByCol(self, cadena_busqueda):
        self.datos_busqueda, msg = self.modelo.datosByCol({'COL': cadena_busqueda})
        
        return (self.datos_busqueda != None, msg)