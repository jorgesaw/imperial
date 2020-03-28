#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.model.models import Product, Proveedor
from sqlalchemy.sql.expression import asc
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.operators import collate
import sqlalchemy

class DAOProveedor(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOProveedor, self).__init__(cerrarSesion)
            
    def getListaDatos(self, mapParam):
        """Busca todos los productos según las iniciales del nombre pasado como parámetro.
           No case sensitive.
           
        :return: Devuelve una tupla con todos los objetos Proveedor.
        :rtype: tuple[Proveedor]"""
        
        objects = []
        try:
            objects = self.session.query(Proveedor).filter(Proveedor.nombre.like(
                mapParam['DATO_BUSQUEDA'] + '%')). \
                order_by(Proveedor.nombre).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            objects = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    def getAll(self, tipo):
        """Busca todos los objetos de un tipo guardados en la base de datos.
        
        :return: Devuelve una tupla con todos los objetos.
        :rtype: tuple[tipo]"""
        
        objects = []
        try:
            objects = self.session.query(tipo)\
            .order_by(asc(collate(Proveedor.nombre, 'NOCASE'))).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects