#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals

class DataModelExtend(object):
    """Clase que maneja el uso de mensajes básicos para mostral al usuario."""
    
    MSG_ERROR_SAVE_DATO_REPETIDO, = range(1) 

    LST_MSG = [
            'Imposible guardar. Ya existe\nun dato con ese nombre.',
            ]    