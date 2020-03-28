#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.model.models import Product, SaldoDiario
import sqlalchemy

class DAOSaldos(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOSaldos, self).__init__(cerrarSesion)
        
    def getSaldoByFecha(self, fecha):
        u"""Busca objetos saldos según la fecha.
        
        :return: Devuelve un objeto.
        :rtype: Venta"""
        
        saldo = None
        try:
            saldo = self.session.query(SaldoDiario).filter(SaldoDiario.fecha_saldo==fecha). \
                        one()
            self.session.commit()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return saldo
        
    def getSaldosByFecha(self, lstDatos):
        u"""Busca objetos saldos según la fecha.
        
        :return: Devuelve un objeto.
        :rtype: Venta"""
        saldos = []
        try:
            saldos = self.session.query(lstDatos[0]).filter(lstDatos[0].fecha==lstDatos[1]). \
                        all()
            self.session.commit()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return saldos
        
    def saldosEntreFechas(self, mapParam):
        
        saldos = []
        try:
            saldos = self.session.query(SaldoDiario).filter(
                        SaldoDiario.fecha_saldo>=mapParam['INICIO'], 
                        SaldoDiario.fecha_saldo<=mapParam['CIERRE']). \
                        all()
            self.session.commit()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return saldos
        
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