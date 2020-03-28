#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOQueryAlchemy import DAOQueryAlchemy
from imperial.model.models import ResumenFiscal
import sqlalchemy

class DAOResumenFiscal(DAOQueryAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOResumenFiscal, self).__init__(cerrarSesion)
        
    def getResumenFiscalByFecha(self, mapParam):
        """Busca todos los resúmenes fiscales según las iniciales del nombre 
            pasado como parámetro.No case sensitive.
           
        :return: Devuelve una tupla con todos los objetos ResumenFiscal.
        :rtype: tuple[ResumenFiscal]"""
        
        objects = []
        try:
            objects = self.session.query(ResumenFiscal).filter(ResumenFiscal.fecha >= \
                mapParam['FECHA_INICIO'], ResumenFiscal.fecha <= mapParam['FECHA_CIERRE']). \
                order_by(ResumenFiscal.fecha).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            objects = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects