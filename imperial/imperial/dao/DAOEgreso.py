#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.model.models import Egreso
from sqlalchemy.sql.expression import asc
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.operators import collate
import sqlalchemy

class DAOEgreso(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOEgreso, self).__init__(cerrarSesion)
        
    def delete(self, object):
        """Elimina los datos de un modelo, pero en realidad lo que hace es
        modificar la variable activo de True a False.

        :param producto: Representa una mascota.
        :return: Un entero que representa el id del modelo eliminado, si se produce
            un error devuleve -1, si la mascota no existe devuelve 0.
        :rtype: int"""
        
        object.activo = False
        
        id = self.update(object)
        
        return id
        
    def getListaDatos(self, mapParam):
        """Busca todos los productos según las iniciales del nombre pasado como parámetro.
           No case sensitive.
           
        :return: Devuelve una tupla con todos los objetos Egreso.
        :rtype: tuple[Egreso]"""
        
        objects = []
        try:
            objects = self.session.query(Egreso).filter(Egreso.nombre.like(
                mapParam['DATO_BUSQUEDA'] + '%')). \
                order_by(Egreso.nombre).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            objects = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    def datosByCol(self, mapParam):
        objects = []
        try:
            objects = self.session.query(Egreso).filter(\
                           Egreso.nombre == mapParam['COL']).\
                          order_by(asc(collate(Egreso.nombre, 'NOCASE'))).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    def getAll(self, tipo):
        """Busca todos los objetos de un tipo guardados en la base de datos.
        
        :return: Devuelve una tupla con todos los objetos.
        :rtype: tuple[tipo]"""
        from imperial.model.models import Egreso
        objects = []
        try:
            objects = self.session.query(tipo)\
            .order_by(asc(collate(Egreso.nombre, 'NOCASE'))).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects