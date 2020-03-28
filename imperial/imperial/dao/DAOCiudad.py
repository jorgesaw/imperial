#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.model.models import Ciudad
import sqlalchemy

class DAOCiudad(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOCiudad, self).__init__(cerrarSesion)

    def getListaDatos(self, mapParam):
        """Busca todos las ciudades según las iniciales del nombre pasado como parámetro.
           No case sensitive.
           
        :return: Devuelve una tupla con todos los objetos Ciudad.
        :rtype: tuple[Ciudad]"""
        
        objects = []
        try:
            objects = self.session.query(Ciudad).filter(Ciudad.nomCiudad.like(
                mapParam['DATO_BUSQUEDA'] + '%')). \
                order_by(Ciudad.nomCiudad).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            objects = None
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return objects
