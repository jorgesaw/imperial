#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 14/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import logging
import importlib

logger = logging.getLogger('import_class')

def import_class(cl):
    """Método que importa una clase dada una cadena del tipo: 
    'my_package.my_module.my_class'."""
    
    #print("CLASE:" + cl)
    #str_class = cl.split('.')[-1]
    #str_pkg_mod = cl[:- (len(str_class)+1)]
    #mod = importlib.import_module(str_pkg_mod)
    #return getattr(mod, str_class)
    return getattr(importlib.import_module(cl[:- (len(cl.split('.')[-1])+1)]), 
                   cl.split('.')[-1])