#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from imperial.model.models import Category
from imperial.util import variables
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
                
class ModeloDatosTablaProduct(object):
    u""""""
    
    NAME, PRICE, DESCRIPTION, RUBRO, EDITAR, ELIMINAR = range(6)
    lstHeader = [NAME, PRICE, DESCRIPTION, RUBRO, EDITAR, ELIMINAR]
    lstTitHeader = ['Nombre', 'Precio ($)', u'Descripción', u'Rubro', u'Editar', 'Eliminar']
    
    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 6

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == ModeloDatosTablaProduct.NAME:
                return _qc.QVariant(dato.name)
            #elif column == CODE:
             #   return _qc.QVariant(dato.code)
            #elif column == EXT_CODE:
             #   return _qc.QVariant(dato.external_code)
            elif column == ModeloDatosTablaProduct.PRICE:
                precio = 0.0
                if len(dato.colPrecioProd) > 0:#uToma el último precio ingresado.
                    precio = dato.colPrecioProd[len(dato.colPrecioProd) - 1].precio
                return _qc.QVariant((_qc.QString("%L1").\
                                     arg('{:.2f}'.format(precio))))
            elif column == ModeloDatosTablaProduct.DESCRIPTION:
                return _qc.QVariant(dato.description)
            elif column == ModeloDatosTablaProduct.RUBRO:
                return _qc.QVariant(Category.lstRubros[dato.categoria - 1])
            elif column == ModeloDatosTablaProduct.EDITAR:
                return _qc.QVariant('Editar')
            elif column == ModeloDatosTablaProduct.ELIMINAR:
                return _qc.QVariant('Eliminar')
            
        elif role == _qc.Qt.DecorationRole:
            if column == ModeloDatosTablaProduct.EDITAR:
                return _qg.QIcon(variables.ICON_PATH_EDIT)
            if column == ModeloDatosTablaProduct.ELIMINAR:
                return _qg.QIcon(variables.ICON_PATH_REMOVE)
            
        elif role == _qc.Qt.TextAlignmentRole:
            if column == ModeloDatosTablaProduct.PRICE:
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        
        elif role == _qc.Qt.BackgroundColorRole:
            if index.row() % 2 == 0:
                return _qc.QVariant(_qg.QColor(58, 216, 58))
            return _qc.QVariant(_qg.QColor(155, 216, 155))
        
        elif role == _qc.Qt.ToolTipRole:
            if column == ModeloDatosTablaProduct.NAME:
                return _qc.QVariant("<font color='#FF0000'>" + dato.name + "</font>")
            #elif column == CODE:
            #   return _qc.QVariant(dato.code)
        return _qc.QVariant()

    def headerData(self, section, orientation, role=_qc.Qt.DisplayRole):
        if role == _qc.Qt.TextAlignmentRole:
            if orientation == _qc.Qt.Horizontal:
                return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
        if role != _qc.Qt.DisplayRole:
            return _qc.QVariant()
        if orientation == _qc.Qt.Horizontal:
            if section in ModeloDatosTablaProduct.lstHeader:
                return _qc.QVariant(ModeloDatosTablaProduct.lstTitHeader[section])
        return _qc.QVariant(int(section + 1))