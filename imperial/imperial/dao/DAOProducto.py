#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.model.models import Product, Category, PrecioProd
from sqlalchemy.sql.expression import asc
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.operators import collate
from sqlalchemy.orm import lazyload, noload
import sqlalchemy


class DAOProducto(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOProducto, self).__init__(cerrarSesion)
        
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
        
    def getAllByStockIdealMin(self):
        """Busca todos los productos cuyo stock sea menor que el stock ideal.
        
        :return: Devuelve una tupla con objetos Product.
        :rtype: tuple[tipo]"""
        
        objects = []
        try:
            pass
            #objects = self.session.query(Product).filter(\
            #               Product.stock < Product.ideal_stock).\
            #              order_by(Product.stock).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    def getPoductByCode(self, code, tipo):
        u"""Busca un objeto en la base de datos con el código ingresado.

        :param code: Representa el identificador del objeto.
        :param tipo: No es necesario porque el tipo es Product. Se mantiene
            por cuestiones de compatibilidad con el código ya existente.
        
        :return: Devuelve un producto con el parámetro code, sino devuelve None."""
        from imperial.model.models import Product, Category
        prod = None
        try:
            pass
            #prod = self.session.query(Product).filter(Product.code == code).one()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return prod
        
    def datosByCol(self, mapParam):
        objects = []
        try:
            objects = self.session.query(Product).filter(\
                           Product.name == mapParam['COL']).\
                          order_by(asc(collate(Product.name, 'NOCASE'))).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    def getListaDatos(self, mapParam):
        """Busca todos los productos según las iniciales del nombre pasado como parámetro.
           No case sensitive.
           
        :return: Devuelve una tupla con todos los objetos Producto.
        :rtype: tuple[Product]"""
        
        objects = []
        try:
            objects = self.session.query(Product).filter(Product.name.like(
                mapParam['DATO_BUSQUEDA'] + '%')). \
                order_by(Product.name).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            objects = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    def getProductosByCategoria(self, mapParam):
        """Busca todos los productos según las iniciales del nombre pasado como parámetro.
           No case sensitive.
           
        :return: Devuelve una tupla con todos los objetos Producto.
        :rtype: tuple[Product]"""
        
        objects = []
        try:
            if mapParam.get('activo'):
                objects = self.session.query(Product).\
                    filter(Product.categoria == mapParam['categoria'], 
                    Product.activo==True).\
                    order_by(asc(collate(Product.name, 'NOCASE'))).all()
            else:
                objects = self.session.query(Product).\
                    filter(Product.categoria == mapParam['categoria']).\
                    order_by(asc(collate(Product.name, 'NOCASE'))).all()
                #order_by(asc(func.lower(Product.name))).all()
                #join(Category).filter(Category.id == mapParam['categoria']).\
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
            objects = self.session.query(tipo).filter(Product.activo==True)\
            .order_by(asc(collate(Product.name, 'NOCASE'))).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
        
    
    def getAllLazy(self):
        """Busca todos los objetos de un tipo guardados en la base de datos.
        
        :return: Devuelve una tupla con todos los objetos.
        :rtype: tuple[tipo]"""
        
        objects = []
        try:
            objects = self.session.query(Product)\
            .options(noload(Product.colPrecioProd))\
            .order_by(asc(collate(Product.name, 'NOCASE'))).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects