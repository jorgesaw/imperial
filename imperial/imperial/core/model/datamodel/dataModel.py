#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals

class DataModel(object):
    """Clase que maneja el uso de mensajes básicos para mostral al usuario."""
    
    MSG_SAVE, MSG_NOT_SAVE, \
    MSG_DELETE, MSG_NOT_DELETE, \
    MSG_EDIT, MSG_NOT_EDIT, \
    MSG_GET_DATO, MSG_NOT_GET_DATO, \
    MSG_LIST_ERROR, MSG_NOT_LIST, MSG_LIST \
         = range(11) 

    LST_MSG = [
            'Datos guardados con éxito.',
            'No se pudieron guardar los datos.', 
            'Datos eliminados con éxito.',
            'No se pudieron eliminar los datos.', 
            'Datos actualizados con éxito.',
            'No se pudieron actualizar los datos.',
            'Dato encontrado en la base de datos.', 
            'No se encontraron los datos en la base de datos.', 
            'Ocurrió un error al listar los datos solicitados.',
            'No hay datos para mostrar.', 
            'Datos listados con éxito.'
            ]    