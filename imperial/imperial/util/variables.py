#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from xlwt import easyxf

PATH_REPORTES = '\\REPORTES\\'

FILE_REPORTE_SALDO = 'reporte_saldo_diario.xls'
FILE_REPORTE_VENTA_DIARIA = 'reporte_venta_diaria.xls'

ICON_PATH_EDIT = ':/edit.png'
ICON_PATH_REMOVE = ':/remove.png'
ICON_PATH_PLANILLA = ':/planillas.png'
ICON_PATH_PRODUCTOS = ':/productos.png'
ICON_PATH_INGREDIENTES = ':/ingredientes.png'
ICON_PATH_VENTAS = ':/ventas.png'
ICON_PATH_RESUMEN = ':/resumen.png'
ICON_PATH_COSTOS = ':/costos.png'

LST_HEADER_REPORTE_SALDO = (u'NOMBRE', u'TOTAL')
LST_HEADER_VENTA_DIARIA = (u'PRODUCTO', u'C1', u'C2', u'C3', u'C4', u'C5', u'C6', 
                           u'T. CARGA', u'DEVOL', u'NETO', u'P. VENTA', u'T. VENTAS')

STYLE_VENTA_DIARIA = easyxf('font: name Arial, bold on, height 180; border: top thick, right thick, bottom thick, left thick;')
STYLE_HEADER_VENTA_DIARIA = easyxf('font: name Arial, bold on, height 205;'
        'align: horiz center; border: top thick, right thick, bottom thick, left thick;pattern: pattern solid, fore_colour grey25')

STYLE_TOTAL_VENTA_DIARIA = easyxf('font: name Arial, bold on, height 260;'
                             'border: top thick, right thick, bottom thick, left thick;'
                             'pattern: pattern solid, fore_colour grey50')

STYLE_HEADER_RESUMEN_FISCAL = easyxf('font: name Arial, bold on, height 210;'
        'align: horiz center; border: top thick, right thick, bottom thick, left thick;pattern: pattern solid, fore_colour grey25')

STYLE_ROW_IMPAR_RESUMEN_FISCAL = easyxf('font: name Arial, bold on, height 260;'
                             'border: top thick, right thick, bottom thick, left thick;'
                             'pattern: pattern solid, fore_colour grey25')