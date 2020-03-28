#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import sys
sys.path.append('./')

NAME, = range(1)

lstHeader = [NAME,]

lstTitHeader = ['Rubro',]

class ModeloDatosTablaCategory(object):
    u""""""

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 1

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == NAME:
                return _qc.QVariant(dato.name)
        elif role == _qc.Qt.TextAlignmentRole:
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.BackgroundColorRole:
            row = index.row()
            if row % 2 == 0: # Si es par.
                return _qc.QVariant(_qg.QColor(_qc.Qt.darkGray))
            #else:
            #return QVariant(QColor(Qt.darkBlue))
        elif role == _qc.Qt.ToolTipRole:
            if column == NAME:
                return _qc.QVariant("<font color='#FF0000'>" + dato.name + "</font>")
        return _qc.QVariant()

    def headerData(self, section, orientation, role=_qc.Qt.DisplayRole):
        if role == _qc.Qt.TextAlignmentRole:
            if orientation == _qc.Qt.Horizontal:
                return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
        if role != _qc.Qt.DisplayRole:
            return _qc.QVariant()
        if orientation == _qc.Qt.Horizontal:
            if section in lstHeader:
                return _qc.QVariant(lstTitHeader[section])
        return _qc.QVariant(int(section + 1))