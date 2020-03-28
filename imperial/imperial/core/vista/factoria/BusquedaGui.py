#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

class BusquedaGui(object):

    def __init__(self, parent=None, mapParam=None):
        self.parent = parent
        self.mapParam = mapParam
        self.dato = None
        
    def datoBuscado(self):
        return self.dato

    def setDatoBuscado(self, dato):
        self.dato = dato
    