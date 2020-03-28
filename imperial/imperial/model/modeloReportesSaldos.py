#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 31/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.datamodel.dataModel import DataModel
from imperial.core.model.genericmodel.genericModel import Model

class ModeloReportesSaldos(Model):
    
    def __init__(self, dao=None, dataClase=None, modeloDatos=None):
        super(ModeloReportesSaldos, self).__init__(dao, dataClase, modeloDatos)
        
    def saldosEntreFechas(self, mapParam):
        msg = DataModel.LST_MSG[DataModel.MSG_LIST_ERROR]
        
        datos = list(self.dao.saldosEntreFechas(mapParam))
        
        if type(datos) == list:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
            if len(datos) > 0:
                msg = DataModel.LST_MSG[DataModel.MSG_LIST]
            else:
                datos = None
                
        return (datos, msg)