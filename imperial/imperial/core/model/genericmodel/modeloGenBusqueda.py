#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.datamodel.dataModel import DataModel
from imperial.core.model.genericmodel.genericModel import Model

class ModeloGenBusqueda(Model):
    u"""Modelo para buscar datos filtrados en la base de datos."""
    
    def __init__(self, dao=None, dataClase=None, modeloDatos=None):
        super(ModeloGenBusqueda, self).__init__(dao, dataClase, modeloDatos)
        
    def getListaDatos(self, mapParam):    
        msg = DataModel.LST_MSG[DataModel.MSG_LIST_ERROR]
        datos = self.dao.getListaDatos(mapParam)
        
        if datos != None:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
            if len(datos) > 0:
                msg = DataModel.LST_MSG[DataModel.MSG_LIST]
            else:
                datos = None
            if mapParam.get('reverse'):
                datos.reverse()
        return (datos, msg)
    
    def datosByCol(self, mapParam):
        msg = DataModel.LST_MSG[DataModel.MSG_LIST_ERROR]
        datos = self.dao.datosByCol(mapParam)
        
        if datos != None:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
            if len(datos) > 0:
                msg = DataModel.LST_MSG[DataModel.MSG_LIST]
            else:
                datos = None
            if mapParam.get('reverse'):
                datos.reverse()
        return (datos, msg)