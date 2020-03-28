#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import sqlalchemy
import imperial.core.dao.alchemyUtil as alchemyUtil

u"""Módulo para mostrar como realizar un DAO para mascotas.
    :author: Jorge Adrián Gonzalez
    :version: 1.0.0"""

__docformat__ = "reestructuredtext"

__version__ = "1.0.0"

class DAOAlchemy(object):
    """Clase que realiza las transacciones con la base de datos."""
    
    def __init__(self, cerrarSesion=True):
        u"""Inicializador de la clase DAO.
            :param cerrarSesion: Boolean que indica si se cierra la sesión al realizar la transacción."""
        self.session = alchemyUtil.session()
        self.__cerrarSesion = cerrarSesion

    def insert(self, object):
        """Guarda los datos de un modelo, se necesita que el identificador se denomine 'id'

        :param object: Representa una objecto para insertar en la base de datos.
        :return: Un entero que representa el id del objecto guardado, sino devuleve -1.
        :rtype: int"""
        id = -1
        try:
            self.session.add(object)
            self.session.commit()
            id = object.id
            
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self.__cerrarSesion:
                self.session.close()
        return id

    def delete(self, object):
        """Elimina los datos de un modelo, se necesita que el identificador de denomine 'id'

        :param mascota: Representa una mascota.
        :return: Un entero que representa el id del modelo eliminado, si se produce
            un error devuleve -1, si la mascota no existe devuelve 0.
        :rtype: int"""
        id = object.id
        try:
            self.session.delete(object)
            self.session.commit()
            
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            id = -1
            print("Error!", e)
        finally:
            if self.__cerrarSesion:
                self.session.close()
        return id

    def update(self, object):
        """Modifica los datos de un modelo, se necesita que el identificador de denomine 'id'

        :param object: Representa una objecto para updatear.
        :return: Un entero que representa el id del objecto modificado, si se produce
            un error devuleve -1, si el objeto no existe devuelve 0.
        :rtype: int"""
        id = object.id
        try:
            self.session.merge(object)
            self.session.commit()
            
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            id = -1
            print("Error!", e)
        finally:
            if self.__cerrarSesion:
                self.session.close()
        return id

    def get(self, id, tipo):
        """Busca un objeto en la base de datos con el id ingresado.

        :param id: Representa el identificador del objeto.
        :return: Devuelve un objeto con el parámetro id, sino devuelve None."""
        object = None
        try:
            object = self.session.query(tipo).get(id)
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self.__cerrarSesion:
                self.session.close()
        return object

    def getAll(self, tipo):
        """Busca todos los objetos de un tipo guardados en la base de datos.
        
        :return: Devuelve una tupla con todos los objetos.
        :rtype: tuple[tipo]"""
        objects = []
        try:
            objects = self.session.query(tipo).all()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
            print("Error!", e)
        finally:
            if self.__cerrarSesion:
                self.session.close()
            return objects
    
    def cerrarSesion(self):
        self.session.close()

    def __str__(self):
        return DAOAlchemy.__name__
    