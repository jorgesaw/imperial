#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.util import variables
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import sys
sys.path.append('./')

class ModeloDatosTablaVendedor(object):
    u""""""

    NAME, EDITAR, ELIMINAR = range(3)

    lstHeader = [NAME, EDITAR, ELIMINAR]

    lstTitHeader = ['Nombre Vendedor', u'Editar', 'Eliminar']

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 3

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == ModeloDatosTablaVendedor.NAME:
                return _qc.QVariant(dato.nombre)
            elif column == ModeloDatosTablaVendedor.EDITAR:
                return _qc.QVariant(u'Editar')
            elif column == ModeloDatosTablaVendedor.ELIMINAR:
                return _qc.QVariant(u'Eliminar')
            
        elif role == _qc.Qt.DecorationRole:
            if column == ModeloDatosTablaVendedor.EDITAR:
                return _qg.QIcon(variables.ICON_PATH_EDIT)
            if column == ModeloDatosTablaVendedor.ELIMINAR:
                return _qg.QIcon(variables.ICON_PATH_REMOVE)
            
        elif role == _qc.Qt.TextAlignmentRole:
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.BackgroundColorRole:
            if index.row() % 2 == 0:
                return _qc.QVariant(_qg.QColor(58, 216, 58))
            return _qc.QVariant(_qg.QColor(155, 216, 155))
            #row = index.row()
            #if row % 2 == 0: # Si es par.
            #    return _qc.QVariant(_qg.QColor(143, 139, 102))
            #else:
            #return QVariant(QColor(Qt.darkBlue))
        elif role == _qc.Qt.ToolTipRole:
            if column == ModeloDatosTablaVendedor.NAME:
                return _qc.QVariant("<font color='#FF0000'>" + dato.nombre+ "</font>")
        return _qc.QVariant()

    def headerData(self, section, orientation, role=_qc.Qt.DisplayRole):
        if role == _qc.Qt.TextAlignmentRole:
            if orientation == _qc.Qt.Horizontal:
                return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
        if role != _qc.Qt.DisplayRole:
            return _qc.QVariant()
        if orientation == _qc.Qt.Horizontal:
            if section in ModeloDatosTablaVendedor.lstHeader:
                return _qc.QVariant(ModeloDatosTablaVendedor.lstTitHeader[section])
        return _qc.QVariant(int(section + 1))