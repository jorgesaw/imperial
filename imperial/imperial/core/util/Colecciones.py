#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 13/03/2013

@author: jorgesaw
'''

class Colecciones(object):

    @staticmethod
    def binarySearch(datos, elemBusqueda):
        datos.sort()
        inferior = 0
        superior = len(datos) - 1
        medio = (inferior + superior + 1) / 2
        ubicacion = -1

        while inferior <= superior and ubicacion == -1:
            if elemBusqueda == datos[medio]:
                ubicacion = medio
            elif elemBusqueda < datos[medio]:
                superior = medio -1
            else:
                inferior = medio + 1
            medio = (inferior + superior + 1) / 2

        return ubicacion
