#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.util import variables
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import Workbook, easyxf
import tempfile
#import xlrd
#import xlutils

class EditCalc(object):
    u""""""
    
    STYLE = easyxf('font: name Arial, bold on, height 260; border: top thick, right thick, bottom thick, left thick;')
    
    STYLE_RESALTADO = easyxf('font: name Arial, bold on, height 400;'
                             'border: top thick, right thick, bottom thick, left thick;'
                             'pattern: pattern solid, fore_colour grey25')
    
    STYLE_HEADER = easyxf('font: name Arial, bold on, height 300;'
                          'align: horiz center; border: top thick, right thick, bottom thick, left thick;pattern: pattern solid, fore_colour grey25')
    
    STYLE_FOOTER = easyxf('font: name Arial, bold on, height 340;'
                          'align: horiz center;'
                          'border: top thick, right thick, bottom thick, left thick;'
                          'pattern: pattern solid, fore_colour grey25', 
                          num_format_str='DD-MM-YYYY')
        
    def __init__(self, fileCalc, lstData, lstHeader=None):
        self.fileCalc = fileCalc
        self.lstData = lstData
        self.lstHeader = lstHeader
        self.rb = None
        self.ws = None
        self.lst_resaltados = []
        self.init_x = 0; self.init_y = 0
        self.style_header = EditCalc.STYLE_HEADER
        self.basic_style = EditCalc.STYLE
        self.resaltado_style = EditCalc.STYLE_RESALTADO
        self.title = None
        
    def columnCount(self):
        return len(self.lstData[0])
    
    def rowCount(self):
        return len(self.lstData)
    
    def abrirArchivo(self):
        self.book = Workbook(encoding='utf-8')
        #self.rb = open_workbook(self.fileCalc, formatting_info=True, encoding='utf-8')
        #self.ws = copy(self.rb)
        
    def crearHoja(self, nombre='Hoja 1'):
        self.sheet = self.book.add_sheet('Hoja 1')
        
    def setWidthCol(self, lstWidth=None):
        if not (lstWidth or self.sheet):
            return
        
        for i, widthCol in enumerate(lstWidth):
            self.sheet.col(i).width = widthCol
            
    def setFooter(self, str_footer):
        self.sheet.footer_str = str_footer
        
    def escribirArchivo(self):
        #self.ws = copy(self.rb)
        #self.sheet = self.ws.get_sheet(0)
        #self.sheet = self.book.add_sheet('Hoja 1')
        
        #self.sheet.col(0).width = 1024 * 20
        #self.sheet.col(1).width = 256 * 20
        
        if self.lstHeader:
            self.escribirHeader()
            
        rowCount = self.rowCount()
        countColumn = self.columnCount()
        #print('CANT_ROW:', rowCount)
        #print('COLUMN_COUNT:', countColumn)
        
        for i in xrange(rowCount):
            for j in xrange(countColumn):
                dato = self.lstData[i][j]
                if not dato:
                    dato = ""
                #print('(x:{}, y:{}) {}'.format(self.init_x + i, self.init_y + j, dato))
                if i in self.lst_resaltados:
                    style = self.resaltado_style
                else:
                    style = self.basic_style
                    
                self.sheet.write(self.init_x + i, self.init_y + j, dato, style)
                
    def escribirHeader(self):
        if self.title:
            self.sheet.write_merge(0, 0, 0, 1, self.title, 
                    easyxf('font: name Arial, bold on, height 300; align: horiz center;'))#arriba, abajo, izquierfda, derecha.
            self.sheet.write(1, 0, "")
        
            self.init_x += 2
            
        countHeader = self.columnCount()
        for i in xrange(countHeader):
            self.sheet.write(self.init_x, i, self.lstHeader[i], self.style_header)
            
        self.init_x += 1
        
    def salvarArchivo(self):
        self.book.save(self.fileCalc)
        #self.ws.save(self.fileCalc)


class EditCalcVentaDiaria(EditCalc):
    
    def __init__(self, fileCalc, lstData, lstHeader=None):
        super(EditCalcVentaDiaria, self).__init__(fileCalc, lstData, lstHeader)
        
    def escribirArchivo(self):
        #self.ws = copy(self.rb)
        #self.sheet = self.ws.get_sheet(0)
        #self.sheet = self.book.add_sheet('Hoja 1')
        
        #self.sheet.col(0).width = 1024 * 20
        #self.sheet.col(1).width = 256 * 20
        
        if self.lstHeader:
            self.escribirHeader()
            
        rowCount = self.rowCount()
        countColumn = self.columnCount()
        #print('CANT_ROW:', rowCount)
        #print('COLUMN_COUNT:', countColumn)
        
        for i in xrange(rowCount):
            for j in xrange(countColumn):
                dato = self.lstData[i][j]
                if not dato:
                    dato = ""
                #print('(x:{}, y:{}) {}'.format(self.init_x + i, self.init_y + j, dato))
                if i in self.lst_resaltados:
                    style = variables.STYLE_TOTAL_VENTA_DIARIA
                else:
                    style = EditCalc.STYLE
                    
                self.sheet.write(self.init_x + i, self.init_y + j, dato, style)
                
    def escribirHeader(self):
        if self.title:
            self.sheet.write_merge(0, 0, 0, 11, self.title[0], 
                easyxf('font: name Arial, bold on, height 300;'))#arriba, abajo, izquierfda, derecha.
            
            self.sheet.write(1, 0, self.title[1], 
                easyxf('font: name Arial, bold on, height 300;'))#arriba, abajo, izquierfda, derecha.)
            
            self.sheet.write(2, 0, "")
        
            #self.init_x += 2
            self.init_x += len(self.title) + 1
        
        countHeader = self.columnCount()
        for i in xrange(countHeader):
            self.sheet.write(self.init_x, i, self.lstHeader[i], self.style_header)
            
        self.init_x += 1
                
class EditCalcResumenFiscal(EditCalc):
    
    def __init__(self, fileCalc, lstData, lstHeader=None):
        super(EditCalcResumenFiscal, self).__init__(fileCalc, lstData, lstHeader)
        self.style_header = variables.STYLE_HEADER_RESUMEN_FISCAL
        
    def escribirHeader(self):
        if self.title:
            self.sheet.write_merge(0, 0, 0, 4, self.title, 
                    easyxf('font: name Arial, bold on, height 300; align: horiz center;'))#arriba, abajo, izquierfda, derecha.
            self.sheet.write(1, 0, "")
        
            self.init_x += 2
        
        countHeader = self.columnCount()
        for i in xrange(countHeader):
            self.sheet.write(self.init_x, i, self.lstHeader[i], self.style_header)
            
        self.init_x += 1
        
    def escribirArchivo(self):
        
        if self.lstHeader:
            self.escribirHeader()
            
        rowCount = self.rowCount()
        countColumn = self.columnCount()
        
        for i in xrange(rowCount):
            for j in xrange(countColumn):
                dato = self.lstData[i][j]
                if not dato:
                    dato = ""
                #print('(x:{}, y:{}) {}'.format(self.init_x + i, self.init_y + j, dato))
                if i % 2 != 0 and j == 0: #Si la fila es impar y la columna es la fecha
                    style = variables.STYLE_ROW_IMPAR_RESUMEN_FISCAL
                else:
                    style = EditCalc.STYLE
                    
                self.sheet.write(self.init_x + i, self.init_y + j, dato, style)
                
class EditCalcCostoProd(EditCalc):

    def __init__(self, fileCalc, lstData, lstHeader=None):
        super(EditCalcCostoProd, self).__init__(fileCalc, lstData, lstHeader)
        
    def escribirArchivo(self):
        if self.lstHeader:
            self.escribirHeader()
            
        rowCount = len(self.lstData[0])
        countColumn = len(self.lstData[0][0])
        
        cant_row = 0

        for i in xrange(rowCount):
            for j in xrange(countColumn):
                dato = self.lstData[0][i][j]
                if not dato:
                    dato = ""
                #print('(x:{}, y:{}) {}'.format(self.init_x + i, self.init_y + j, dato))
                if i in self.lst_resaltados:
                    style = variables.STYLE_TOTAL_VENTA_DIARIA
                else:
                    style = EditCalc.STYLE
                    
                self.sheet.write(self.init_x + i, self.init_y + j, dato, style)
                cant_row = self.init_x + i
        
        self.sheet.write(cant_row + 1, 0, "")
        
        lst_tit = [u'Costo total ingrediente:', u'Gastos de producción:', 
                   u'Cantidad:', u'Costo x unidad:', u'Observaciones:']
        
        cant_row += 2
        
        #for i, tit in enumerate(lst_tit):
        #   dato = '{} $ {}'.format(tit, self.lstData[1][i])
        #   self.sheet.write(cant_row + i, 0 , dato, 
        #                    easyxf('font: name Arial, bold on, height 300;'))
        self.sheet.write(cant_row + 0, 0 , '{} $ {}'.format(lst_tit[0], self.lstData[1][0]), 
                            easyxf('font: name Arial, bold on, height 300;'))
        self.sheet.write(cant_row + 2, 0 , '{} $ {}'.format(lst_tit[1], self.lstData[1][1]), 
                            easyxf('font: name Arial, bold on, height 300;'))
        self.sheet.write(cant_row + 4, 0 , '{} {}'.format(lst_tit[2], self.lstData[1][2]), 
                            easyxf('font: name Arial, bold on, height 300;'))
        self.sheet.write(cant_row + 6, 0 , '{} $ {}'.format(lst_tit[3], self.lstData[1][3]), 
                            easyxf('font: name Arial, bold on, height 300;'))
        self.sheet.write(cant_row + 8, 0 , '{}'.format(lst_tit[4]), 
                            easyxf('font: name Arial, bold on, height 300, underline on;'))
        #self.sheet.write(cant_row + 5, 0 , self.formatearDesc(self.lstData[1][4]), 
        #                   easyxf('font: name Arial, bold on, height 180;'))
        
        self.formatearDesc(self.lstData[1][4], cant_row + 9)
        
    def formatearDesc(self, cadena, cant_row):
        max_total_char = 90
        
        parrafos = cadena.split('\n')

        for parrafo in parrafos:
            palabras = parrafo.split(' ')
            cadena_formateada = ''
            
            
            for palabra in palabras:
                linea_escrita = False
                
                if len(cadena_formateada + palabra) < max_total_char:
                    cadena_formateada += palabra
                    cadena_formateada += ' '
                else:
                    linea_escrita = True
                    cant_row += 1
                    self.sheet.write(cant_row, 0 , cadena_formateada, 
                            easyxf('font: name Arial, bold on, height 210;'))
                    cadena_formateada = ''
                    cadena_formateada += palabra
            
            if not linea_escrita:
                self.sheet.write(cant_row, 0 , cadena_formateada, 
                            easyxf('font: name Arial, bold on, height 210;'))
                cadena_formateada = ''
                cant_row += 1
            
            if len(cadena_formateada) > 0:#uPertenece al párrafo anterior.
                cant_row += 1
                self.sheet.write(cant_row, 0 , cadena_formateada, 
                        easyxf('font: name Arial, bold on, height 210;'))
                cant_row += 1
            
    def escribirHeader(self):
        if self.title:
            self.sheet.write_merge(0, 0, 0, 11, self.title[0], 
                easyxf('font: name Arial, bold on, height 300;'))#arriba, abajo, izquierfda, derecha.
            
            self.sheet.write(1, 0, self.title[1], 
                easyxf('font: name Arial, bold on, height 300;'))#arriba, abajo, izquierfda, derecha.)
            
            self.sheet.write(2, 0, "")
        
            #self.init_x += 2
            self.init_x += len(self.title) + 1
        
        countHeader = len(self.lstData[0][0])
        for i in xrange(countHeader):
            self.sheet.write(self.init_x, i, self.lstHeader[i], self.style_header)
            
        self.init_x += 1