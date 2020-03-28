#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOQueryAlchemy import DAOQueryAlchemy
from imperial.model.models import VendedorExterno, Vendedor
from sqlalchemy.sql.expression import asc
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.operators import collate
import sqlalchemy

class DAOMovVentaProd(DAOQueryAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOMovVentaProd, self).__init__(cerrarSesion)
        
    def movVentaProdByFecha(self, mapParam):
        """Busca todos los movimientos de venta según la fecha
            pasada como parámetro.
           
        :return: Devuelve una tupla con objetos MovVentaProd.
        :rtype: tuple[MovVentaProd]"""
        
        mov = []
        try:
            mov = self.session.query(MovVentaProd).filter(MovVentaProd.fecha == \
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
        
    def movVentaProdByFechaVende(self, mapParam):
        """Busca todos los movimientos de venta según la fecha
            pasada como parámetro.
           
        :return: Devuelve una tupla con objetos MovVentaProd.
        :rtype: tuple[MovVentaProd]"""
        
        mov = None
        try:
            mov = self.session.query(MovVentaProd).filter(MovVentaProd.fecha == \
                mapParam['FECHA_MOV'])\
                .join(VendedorExterno).filter(VendedorExterno.id == mapParam['VENDEDOR'].id)\
                .one()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            mov = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return mov