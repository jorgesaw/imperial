#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.model.models import CostoProd, Product
from sqlalchemy.sql.expression import desc, asc
import sqlalchemy

class DAOCostosProd(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOCostosProd, self).__init__(cerrarSesion)
        
    def getCostosByFechaProd(self, lstDatos):
        u"""Busca un objetos costo según fecha y producto.
        
        :return: Devuelve un objeto.
        :rtype: CostoProd"""
        
        costo = None
        try:
            costo = self.session.query(CostoProd).filter(CostoProd.fecha_ingreso==lstDatos[0]). \
                    join(Product).filter(Product.id == lstDatos[1].id).one()
            self.session.commit()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return costo
        
    def getCostosByProdUltimaFecha(self, lstDatos):
        u"""Busca objetos costo según fecha y producto.
        
        :return: Devuelve un objeto.
        :rtype: CostoProd"""
        
        costos = []
        try:
            costos = self.session.query(CostoProd).\
            join(Product).distinct(Product.id).order_by(asc(Product.name), desc(CostoProd.fecha_ingreso))\
            .all()
            self.session.commit()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            costos = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return costos
        
    def getAllProducts(self, tipo=Product):
        """Busca todos los objetos de un tipo guardados en la base de datos.
        
        :return: Devuelve una tupla con todos los objetos.
        :rtype: tuple[tipo]"""
        objects = []
        try:
            objects = self.session.query(tipo).order_by(Product.name).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects