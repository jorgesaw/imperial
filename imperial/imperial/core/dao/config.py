#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""Módulo para leer archivo de configuración de una conexión a la base de datos."""

__docformat__ = "reestructuredtext"

__version__ = "1.0.0"

class ConfigDataMalFormadoError(Exception):
    u"""Clase excepción que se lanza cuando el archivo de configuración
        no tiene los datos bien formados."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

def cargarConfig():
    u"""Función que carga y valida el archivo de configuración
        para una conexión a la base de datos.
        :return: Un string que representa la cadena de conexión a la base de datos.
        :rtype: string"""
    fConfig = None
    completo = None
    try:
        fConfig = open('config.txt', 'r')
        completo = fConfig.read()
    except IOError, e:
        print(e)
    finally:
        if fConfig:
            fConfig.close()
        
    lineas = completo.split('\n')
    datos = [linea.split('=', 1) for linea in lineas] 
    dic_datos = dict(datos)

    keys = ["motor", "user", "pass", "url", "port", "db"] 
    for i in range(6):
        if not dic_datos.has_key(keys[i]):
            raise ConfigDataMalFormadoError, (unicode("Los datos del archivo config estan malformados: Linea " \
                                                 + str(i + 1) + "."))
    motor = dic_datos['motor'].strip() + '://'
    userPass = dic_datos['user'].strip() + ':' + dic_datos['pass'].strip() \
            if len(dic_datos['user'].strip()) > 0 and len(dic_datos['pass'].strip()) > 0 else ''
    url = '@' + dic_datos['url'].strip() if len(dic_datos['url'].strip()) > 0 else ''
    port = ':' + dic_datos['port'].strip() if len(dic_datos['port'].strip()) > 0 else ''        
    db = '/' + dic_datos['db'].strip()
    return motor + userPass + url + port + db
