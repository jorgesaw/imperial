'''
Created on 24/07/2015

@author: jorgesaw
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.listmodel.datosListModel import DatosListModel
from imperial.core.util.ManejaFechas import ManejaFechas
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DatosListModelProd(DatosListModel):
    u"""Modelo para manejar los datos que se pueden agregar a un
        combo o una lista"""

    def __init__(self, modeloDatos, seleccionar=True):
        super(DatosListModelProd, self).__init__(modeloDatos, seleccionar)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or \
           not (0 <= index.row() <= len(self.datos)):
            return QVariant()
        dato = self.datos[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if (isinstance(dato, str)):
                return QVariant(unicode(dato))
            else:
                value = '{}'.format(dato.__str__())
                if dato.colCostosProd:
                    if len(list(dato.colCostosProd)) > 0:
                        value = '{} - ({})'.format(dato.__str__(), 
                                ManejaFechas.date2Str(dato.colCostosProd[len(dato.colCostosProd) - 1].fecha_ingreso))
                    
                return QVariant(value)
        
        return QVariant()