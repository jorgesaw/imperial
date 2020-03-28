#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from DAOAlchemy import DAOAlchemy

u"""Módulo para mostrar como realizar un DAO para mascotas.
    :author: Jorge Adrián Gonzalez
    :version: 1.0.0"""

__docformat__ = "reestructuredtext"

__version__ = "1.0.0"

class DAOQueryAlchemy(DAOAlchemy):
    """Clase que realiza las transacciones con la base de datos."""
    
    def __init__(self, cerrarSesion=True):
        u"""Inicializador de la clase DAOQuery.
            :param cerrarSesion: Boolean que indica si se cierra la sesión al realizar la transacción."""
        super(DAOQueryAlchemy, self).__init__(cerrarSesion)

    def insertMasivo(self, objects):
        """Guarda los datos de un modelo, se necesita que el identificador se denomine 'id'

        :param object: Representa una objecto para insertar en la base de datos.
        :return: Un entero 1 que representa que los datos se guardaron correctamente, sino devuleve -1.
        :rtype: int"""
        retorno = 1
        
        try:
            n = len(objects)
            for i in xrange(n):
                self.session.add(objects[i])
                if i % 100 == 0:
                    self.session.flush()
            #for object in objects:
            #   self.session.add(object)
            self.session.commit()
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
                retorno = -1
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return retorno

    def deleteMasivo(self, objects):
        """Elimina los datos de un modelo, se necesita que el identificador de denomine 'id'

        :param object: Representa un objeto.
        :return: Un entero que representa el id del modelo eliminado, si se produce
            un error devuleve -1, si la mascota no existe devuelve 0.
        :rtype: int"""
        retorno = 1
        try:
            for object in objects:
                self.session.delete(object)
                
            self.session.commit()
            
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
                retorno = -1
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return retorno

    def updateMasivo(self, objects):
        """Modifica los datos de un modelo, se necesita que el identificador de denomine 'id'

        :param object: Representa una objecto para updatear.
        :return: Un entero que representa el id del objecto modificado, si se produce
            un error devuelve -1, si el objeto no existe devuelve 0.
        :rtype: int"""
        retorno = 1
        try:
            for object in objects:
                self.session.merge(object)
            self.session.commit()
            
        except sqlalchemy.exc.DBAPIError, e:
            if self.session is not None:
                self.session.rollback()
                retorno = -1
            print("Error!", e)
        finally:
            if self._DAOAlchemy__cerrarSesion:
                self.session.close()
            return retorno
