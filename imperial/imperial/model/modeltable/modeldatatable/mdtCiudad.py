#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12/07/2014

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

NOMBRE, COD_POSTAL, DDN, PROVINCIA = range(4)

lstHeader = [NOMBRE, COD_POSTAL, DDN, PROVINCIA]

lstTitHeader = [u'Ciudad', u'Cod. Postal', u'DDN', u'Provincia']

class ModeloDatosTablaCiudad(object):
    u""""""

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 4

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == NOMBRE:
                return _qc.QVariant(dato.nomCiudad)
            elif column == COD_POSTAL:
                return _qc.QVariant(dato.codPostal)
            elif column == DDN:
                return _qc.QVariant(dato.DDN)
            elif column == PROVINCIA:
                return _qc.QVariant(dato.provincia.nombre)
            #elif column == TEU:
            #return QVariant(QString("%L1").arg(dato.teu))
        elif role == _qc.Qt.TextAlignmentRole:
            if column == COD_POSTAL or column == DDN:
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.BackgroundColorRole:
            row = index.row()
            if row % 2 == 0: # Si es par.
                return _qc.QVariant(_qg.QColor(_qc.Qt.darkGray))
            #else:
            #return QVariant(QColor(Qt.darkBlue))
        elif role == _qc.Qt.ToolTipRole:
            if column == NOMBRE:
                return _qc.QVariant("<font color='#FF0000'>" + dato.nombre + "</font>")
            elif column == COD_POSTAL:
                return _qc.QVariant(dato.codPostal)
            elif column == DDN:
                return _qc.QVariant(dato.DDN)
            elif column == PROVINCIA:
                return _qc.QVariant(dato.provincia.nombre)
        return _qc.QVariant()

    def setData(self, this, index, value, dato, role=_qc.Qt.EditRole):
            column = index.column()
            if column == NOMBRE:
                dato.nombre = unicode(value)
            elif column == COD_POSTAL:
                dato.codPostal = unicode(value)
            elif column == DDN:
                dato.DDN = unicode(value)
            elif column == PROVINCIA:
                dato.provincia = value
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