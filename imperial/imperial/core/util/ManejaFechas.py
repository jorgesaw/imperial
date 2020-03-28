#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 20/01/2015

@author: jorgesaw
'''

import sys
sys.path.append('./')
import datetime 

class ManejaFechas(object):
    u"""Clase que permite simplificar las funciones principales del paquete datetime."""
    
    formatoFecha = "%d-%m-%Y"
    formatoHora = "%H:%M:%S"
    
    @staticmethod
    def fechaActual():
        return datetime.date.today().strftime(ManejaFechas.formatoFecha)
        
    @staticmethod
    def horaActual():
        return datetime.datetime.today().strftime(ManejaFechas.formatoHora)
        
    @staticmethod    
    def sumarFechasDias(fecha, numDias):
        diasSumar = datetime.timedelta(days=numDias)
        return fecha + diasSumar
    
    @staticmethod    
    def restarFechasDias(fecha, numDias):
        return ManejaFechas.sumarFechasDias(fecha, -1 * numDias)
    
    @staticmethod    
    def diasDiferencia(fechaInicial, fechaFinal):
        return fechaFinal.toordinal() - fechaInicial.toordinal()
        return (fechaFinal - fechaInicial).days
    
    @staticmethod    
    def str2Date(cadenaFecha, formatoFecha=formatoFecha):
        #Agrega las horas, minutos y segundos
        #return datetime.datetime.strptime(cadenaFecha, formatoFecha)
        return datetime.datetime.strptime(cadenaFecha, formatoFecha).date()

    @staticmethod    
    def date2Str(fecha, formatoFecha=formatoFecha):
        return fecha.strftime(formatoFecha)