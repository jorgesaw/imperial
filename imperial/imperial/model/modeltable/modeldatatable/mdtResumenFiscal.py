#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 02/5/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

FECHA_RF, PROM_VENTA_RF, CANT_PERS_RF, CAJA_ABAJO_RF, PROM_PERS_CAJA_ABAJO = range(4)

lstHeader = [PROM_VENTA_RF, CANT_PERS_RF, CAJA_ABAJO_RF, FECHA_RF, PROM_PERS_CAJA_ABAJO]

lstTitHeader = [u'Fecha', u'Prom. Venta Z', u'Cant. personas Z', u'Cant. personas abajo']

class ModeloDatosTablamdtResumenFiscal(object):
    u""""""

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 4

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == FECHA_RF:
                return _qc.QVariant(dato.fecha)
            elif column == PROM_VENTA_RF:
                return ((_qc.QString("%L1").\
                                     arg('$ {:.2f}'.format(dato.prom_venta))))
            elif column == CANT_PERS_RF:
                return _qc.QVariant(dato.cant_pers)
            elif column == CAJA_ABAJO_RF:
                return _qc.QVariant(dato.caja_abajo)
            elif column == PROM_PERS_CAJA_ABAJO:
                return _qc.QVariant(dato.caja_abajo)
            #elif column == TEU:
            #return QVariant(QString("%L1").arg(dato.teu))
        
        elif role == _qc.Qt.TextAlignmentRole:
            if column == PROM_VENTA_RF or column == CANT_PERS_RF or \
                        column == CANT_PERS_RF or column == PROM_PERS_CAJA_ABAJO:
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        
        elif role == _qc.Qt.BackgroundColorRole:
            row = index.row()
            if row % 2 == 0: # Si es par.
                return _qc.QVariant(_qg.QColor(_qc.Qt.darkGray))
            #else:
            #return QVariant(QColor(Qt.darkBlue))
            
        elif role == _qc.Qt.FontRole:
            font = _qg.QFont('Helvetica', 11, _qg.QFont.Bold)
            return _qc.QVariant(font)
        
        return _qc.QVariant()

    def setData(self, this, index, value, dato, role=_qc.Qt.EditRole):
            column = index.column()
            if column == FECHA_RF:
                dato.fecha = unicode(value)
            elif column == PROM_VENTA_RF:
                dato.prom_venta = unicode(value)
            elif column == CANT_PERS_RF:
                dato.cant_pers = unicode(value)
            elif column == CAJA_ABAJO_RF:
                dato.caja_abajo = value
            elif column == PROM_PERS_CAJA_ABAJO:
                dato.prom_pers_caja_abajo = value
            this.emit(_qc.SIGNAL("dataChanged(QModelIndex, QModelIndex)"),
                      index, index)
            return True

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