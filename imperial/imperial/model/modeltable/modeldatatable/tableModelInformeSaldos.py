#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 25/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.modelotable.modeloTabla import ModeloTabla

class TMInformeSaldosSemanal(ModeloTabla):
    
    INF_SEMANAL = 0
    INF_MENSUAL = 1
    INF_PERSONALIZADO = 2
    
    def __init__(self, modelo, modeloDatosTabla, parent=None):
        super(TMInformeSaldosSemanal, self).__init__(modelo, modeloDatosTabla, parent)
        
        self.lstTipoInformes = [self.buscarDatosSemanal, self.buscarDatosMensual, 
                                self.buscarDatosPersonalizado]
        
    def buscarDatos(self, lstDatos):
        tipo_informe = lstDatos[0]
        return self.lstTipoInformes[tipo_informe](lstDatos)
        
    def buscarDatosSemanal(self, lstDatos):
        mapParam = {'informe': TMInformeSaldosSemanal.INF_SEMANAL}
        lstDatos = self.modelo.getListaDatos(mapParam)
    
    def buscarDatosMensual(self, lstDatos):
        mapParam = {'informe': TMInformeSaldosSemanal.INF_MENSUAL}
        lstDatos = self.modelo.getListaDatos(mapParam)
        
    def buscarDatosPersonalizado(self, lstDatos):
        mapParam = {'informe': TMInformeSaldosSemanal.INF_PERSONALIZADO}
        lstDatos = self.modelo.getListaDatos(mapParam)    
    