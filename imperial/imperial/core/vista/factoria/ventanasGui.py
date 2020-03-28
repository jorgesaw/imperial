#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals

class VentanasGui(object):
    
    def __init__(self, parent=None, mapParam=None):
        self._parent = parent
        self._mapParam = mapParam
        self.__ol = None

    def prepararVentana(self):
        raise 'No yet implemented.'

    def tipo(self):
        raise 'No yet implemented.'