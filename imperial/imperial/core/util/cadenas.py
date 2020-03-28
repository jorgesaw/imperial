#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

#Lista de carcteres inválidos para usar en el nombre de un fichero. 
EXCLUIDOS_WIN = ('/', '\\', ':', '*', '?', '"', '<', '>', '|')

def limpiarCaracteres(cadena, lstExcluidos=EXCLUIDOS_WIN, reemplazo='_'):
    u"""Función que reemplaza los caracteres a excluir por otro carácter a elegir."""
    for car in lstExcluidos:
        cadena = cadena.replace(car, reemplazo)
    return cadena

FORBIDDEN_CHARACTERS = ('\n', '\t', '\r')
def printable(text):
    #not the fastet way but..
    for c in FORBIDDEN_CHARACTERS:
        text = text.replace(c, ' ')
    return text

#cadena = "Taxi :/D>riv\\er"
#print cadena

#cadenaLimpiada = limpiarCaracteres(cadena)
#print cadenaLimpiada #Taxi __D_riv_er

#cadenaLimpiada = limpiarCaracteres(cadena, reemplazo='')
#print cadenaLimpiada #Taxi Driver