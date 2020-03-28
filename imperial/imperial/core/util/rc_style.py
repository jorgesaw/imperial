#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 12/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import logging
logger = logging.getLogger()

def cargarStyleSheet(f):
    """Carga un fichero de estilos si existe, sino devuelve una cadena vacía."""
    style = None
    
    if f:
        try:
            fh = open(f, 'r')
            style = fh.read()
        except Exception, e:
            logger.info('No se pudo cargar el archivo.', exc_info=True)
        finally:
            return style if style != None else ''