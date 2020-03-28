#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOQueryAlchemy import DAOQueryAlchemy
from imperial.model.models import VendedorExterno, Vendedor, Venta, VentaProd
from sqlalchemy.orm import noload
import sqlalchemy

class DAOVenta(DAOQueryAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOVenta, self).__init__(cerrarSesion)
        
    def ventasByFecha(self, mapParam):
        """Busca todos los movimientos de venta según la fecha
            pasada como parámetro.
           
        :return: Devuelve una tupla con objetos MovVentaProd.
        :rtype: tuple[MovVentaProd]"""
        
        mov = []
        try:
            mov = self.session.query(Venta).filter(Venta.fecha == \
                mapParam['FECHA_MOV'])\
                .join(Vendedor)\
                .order_by(Vendedor.nombre).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            mov = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return mov
        
    def ventaByFechaVendedor(self, mapParam):
        """Busca todos los movimientos de venta según la fecha
            pasada como parámetro.
           
        :return: Devuelve una tupla con objetos MovVentaProd.
        :rtype: tuple[MovVentaProd]"""
        
        venta = None
        try:
            venta = self.session.query(Venta).filter(Venta.fecha == \
                mapParam['FECHA_MOV'])\
                .join(VendedorExterno).filter(VendedorExterno.id == mapParam['VENDEDOR'].id)\
                .options(noload(Venta.colVentasProd)).one()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            venta = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return venta
    
    def ventaByFechaVendedorNotLazy(self, mapParam):
        """Busca todos los movimientos de venta según la fecha
            pasada como parámetro.
           
        :return: Devuelve una tupla con objetos MovVentaProd.
        :rtype: tuple[MovVentaProd]"""
        
        venta = None
        try:
            venta = self.session.query(Venta).filter(Venta.fecha == \
                mapParam['FECHA_MOV'])\
                .join(VendedorExterno).filter(VendedorExterno.id == mapParam['VENDEDOR'].id)\
                .one()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            venta = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return venta
            
    
    def ventaProdByVenta(self, mapParam):
        """Busca todos los movimientos de venta según la fecha
            pasada como parámetro.
           
        :return: Devuelve una tupla con objetos MovVentaProd.
        :rtype: tuple[MovVentaProd]"""
        
        lstVentasProd = None
        try:
            lstVentasProd = self.session.query(VentaProd)\
                .join(Venta).filter(Venta.id == mapParam['ID_VENTA'])\
                .all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            lstVentasProd = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return lstVentasProd