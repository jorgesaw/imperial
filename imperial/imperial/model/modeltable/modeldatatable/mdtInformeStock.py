#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

NAME, CODE, MIN_STOCK, IDEAL_STOCK, STOCK \
            = range(5)

lstHeader = [NAME, CODE, MIN_STOCK, IDEAL_STOCK, STOCK]

lstTitHeader = ['Nombre', u'Código', 'Stock min.', 'Stock ideal', 'Stock']

class MdtInformeStock(object):
    u""""""

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 5

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == NAME:
                return _qc.QVariant(dato.name)
            elif column == CODE:
                return _qc.QVariant(dato.code)
            elif column == MIN_STOCK:
                return _qc.QVariant(dato.min_stock)
            elif column == IDEAL_STOCK:
                return _qc.QVariant(dato.ideal_stock)
            elif column == STOCK:
                return _qc.QVariant(dato.stock)
        
        elif role == _qc.Qt.TextAlignmentRole:
            if column == STOCK or column == MIN_STOCK or column == IDEAL_STOCK:
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        
        elif role == _qc.Qt.TextColorRole and column == STOCK:
            return _qc.QVariant(_qg.QColor(_qc.Qt.white))
        
        elif role == _qc.Qt.BackgroundColorRole:
            if dato.stock < dato.min_stock and column == STOCK:
                return _qc.QVariant(_qg.QColor(_qc.Qt.darkRed))
            elif dato.stock < dato.ideal_stock and dato.stock >= dato.min_stock and column == STOCK:
                return  _qc.QVariant(_qg.QColor(_qc.Qt.darkYellow))
        
        elif role == _qc.Qt.ToolTipRole:
            if column == NAME:
                return _qc.QVariant("<font color='#FF0000'>" + dato.name + "</font>")
            elif column == CODE:
                return _qc.QVariant(dato.code)
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