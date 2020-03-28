#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

NAME, CODE, PRICE, QUANTITY, SUBTOTAL= range(5)

lstHeader = [NAME, CODE, PRICE, QUANTITY, SUBTOTAL]

lstTitHeader = ['Nombre', u'Código', 'Precio', 'Cantidad', 'Subtotal']

class MDTMateTPVGui(object):
    u""""""

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 5

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == NAME:
                return _qc.QVariant(dato.product.name)
            elif column == CODE:
                return _qc.QVariant(dato.product.code)
            elif column == PRICE:
                return _qc.QVariant((_qc.QString("%L1").\
                                     arg('$ {:.2f}'.format(dato.product.price))))
            elif column == QUANTITY:
                return _qc.QVariant(dato.quantity)
            elif column == SUBTOTAL:
                return _qc.QVariant((_qc.QString("%L1").\
                                     arg('$ {:.2f}'.format(dato.calculate()))))
        
        elif role == _qc.Qt.TextAlignmentRole:
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        
        elif role == _qc.Qt.BackgroundColorRole:
            row = index.row()
            if row % 2 == 0: # Si es par.
                return _qc.QVariant(_qg.QColor(250, 230, 250))
            else:
                return _qc.QVariant(_qg.QColor(210, 230, 230))
                
        elif role == _qc.Qt.ToolTipRole:
            pass
        
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