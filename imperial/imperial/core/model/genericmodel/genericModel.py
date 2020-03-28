#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 06/07/2014

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.datamodel.dataModel import DataModel

class Model(object):
    '''
    Modelo genérico para manejo de datos vinculados a una base de datos.
    '''

    def __init__(self, dao=None, dataClase=None, modeloDatos=None):
        self.modeloDatos = modeloDatos
        self.dao = dao
        self.dataClase = dataClase
        
    def tipoDato(self):
        return type(self.dataClase)
    
    def cerrarSesionDAO(self):
        self.dao.cerrarSesion()
    
    def guardarDatos(self, lstDatos):
        #dato = self.modeloDatos.creaObjeto(lstDatos)
        dato = self.dataClase.data2Object(lstDatos)
        
        return self.guardarDato(dato)
    
    def guardarDato(self, dato):
        msg = DataModel.LST_MSG[DataModel.MSG_SAVE]
        
        retorno = self.dao.insert(dato)
        if retorno <= 0:
            dato = None
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_SAVE]
        
        return (dato, msg)
    
    def eliminarDato(self, dato):
        msg = DataModel.LST_MSG[DataModel.MSG_NOT_DELETE]
        #msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_DELETE)
        retorno = self.dao.delete(dato)
        
        if retorno > 0:
            msg = DataModel.LST_MSG[DataModel.MSG_DELETE]
            #msg = self.modeloDatos.msg(ModeloDatos.MSG_DELETE)
            
        return (retorno, msg)
    
    def actualizarDatos(self, datoUpdate, lstDatos):
        #msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_EDIT)
        
        #self.modeloDatos.editObject(datoUpdate, lstDatos)
        self.dataClase.editObject(datoUpdate, lstDatos)
        #retorno = self.dao.update(datoUpdate)
        #if retorno > 0:
        #   msg = self.modeloDatos.msg(ModeloDatos.MSG_EDIT)
            
        #return (retorno > 0, msg)
        return self.actualizarDato(datoUpdate)
    
    def actualizarDato(self, datoUpdate):
        msg = DataModel.LST_MSG[DataModel.MSG_NOT_EDIT]
        #msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_EDIT)
        
        retorno = self.dao.update(datoUpdate)
        if retorno > 0:
            msg = DataModel.LST_MSG[DataModel.MSG_EDIT]
            #msg = self.modeloDatos.msg(ModeloDatos.MSG_EDIT)
            
        return (retorno > 0, msg)
    
    def getDato(self, id):
        msg = DataModel.LST_MSG[DataModel.MSG_NOT_GET_DATO]
        #msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_EDIT)
        
        retorno = self.dao.get(id, self.dataClase.type())
        if retorno > 0:
            msg = DataModel.LST_MSG[DataModel.MSG_GET_DATO]
            #msg = self.modeloDatos.msg(ModeloDatos.MSG_EDIT)
            
        return (retorno > 0, msg)
    
    def listarDatos(self, reverse=False):
        msg = DataModel.LST_MSG[DataModel.MSG_LIST_ERROR]
        #msg = self.modeloDatos.msg(ModeloDatos.MSG_LIST_ERROR)
        #datos = list(self.dao.getAll(self.modeloDatos.tipo()))
        datos = list(self.dao.getAll(self.dataClase.type()))
        
        if type(datos) == list:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
            #msg = self.modeloDatos.msg(ModeloDatos.MSG_NOT_LIST)
            if len(datos) > 0:
                msg = DataModel.LST_MSG[DataModel.MSG_LIST]
                #msg = self.modeloDatos.msg(ModeloDatos.MSG_LIST)
                if reverse:
                    datos.reverse()
            else:
                datos = None
        return (datos, msg)
    
    def datosModelo(self, dato):
        #return self.modeloDatos.datosObjeto(dato)
        return self.dataClase.object2Data(dato)