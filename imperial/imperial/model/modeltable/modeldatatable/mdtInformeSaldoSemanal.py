#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model.modeltable.modeldatatable.mdtProduct import \
    ModeloDatosTablaProduct
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
                
class MDTInformeSaldoSemanal(object):
    u""""""
    
    NOMBRE_DATO, LUN, MAR, MIE, JUE, VIE, SAB, DOM, TOT = range(9)
    lstHeader = [NOMBRE_DATO, LUN, MAR, MIE, JUE, VIE, SAB, DOM, TOT]
    lstTitHeader = ['NOMBRE', 'Lunes', u'Martes', u'Miércoles', u'Jueves', 
                    u'Viernes', u'Sábado', u'Domingo', u'TOTAL']
    
    def __init__(self):
        self.tabla_reporte = None
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 9

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        row = index.row()
        column = index.column()
        
        filaDatos = self.tabla_reporte.datos[row]
        
        if role == _qc.Qt.DisplayRole:
            if column == MDTInformeSaldoSemanal.NOMBRE_DATO:
                return _qc.QVariant(filaDatos[0])
            elif column == MDTInformeSaldoSemanal.LUN:
                return _qc.QVariant(filaDatos[1])
            elif column == MDTInformeSaldoSemanal.MAR:
                return _qc.QVariant(filaDatos[2])
            elif column == MDTInformeSaldoSemanal.MIE:
                return _qc.QVariant(filaDatos[3])
            elif column == MDTInformeSaldoSemanal.JUE:
                return _qc.QVariant(filaDatos[4])
            elif column == MDTInformeSaldoSemanal.VIE:
                return _qc.QVariant(filaDatos[5])
            elif column == MDTInformeSaldoSemanal.SAB:
                return _qc.QVariant(filaDatos[6])
            elif column == MDTInformeSaldoSemanal.DOM:
                return _qc.QVariant(filaDatos[7])
            elif column == MDTInformeSaldoSemanal.TOT:
                return _qc.QVariant(filaDatos[8])
        elif role == _qc.Qt.TextAlignmentRole:
            if column > MDTInformeSaldoSemanal.NOMBRE_DATO:
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.TextColorRole:
            if column > MDTInformeSaldoSemanal.NOMBRE_DATO:
                if row < self.tabla_reporte.cant_ventas:
                    return _qc.QVariant(_qg.QColor(_qc.Qt.darkGreen))
                elif row > self.tabla_reporte.cant_ventas and \
                    row < self.tabla_reporte.cant_ventas + self.tabla_reporte.cant_egresos + 1:
                    return _qc.QVariant(_qg.QColor(_qc.Qt.darkRed))
        elif role == _qc.Qt.BackgroundColorRole:
            row = index.row()
            if row == self.tabla_reporte.cant_ventas:
                return _qc.QVariant(_qg.QColor(58, 216, 58))
            elif row == self.tabla_reporte.cant_ventas + self.tabla_reporte.cant_egresos + 1:
                return _qc.QVariant(_qg.QColor(216, 66, 58))
            elif row == self.tabla_reporte.cant_ventas + self.tabla_reporte.cant_egresos + 2:
                if self.tabla_reporte.datos[row][index.column()] >= 0:
                    return _qc.QVariant(_qg.QColor(58, 216, 58))
                return _qc.QVariant(_qg.QColor(216, 66, 58))
            return _qc.QVariant()
            #row = index.row()
            #if row % 2 == 0: # Si es par.
            #    return _qc.QVariant(_qg.QColor(_qc.Qt.darkGray))
            #else:
            #return QVariant(QColor(Qt.darkBlue))
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
            if section in MDTInformeSaldoSemanal.lstHeader:
                return _qc.QVariant(MDTInformeSaldoSemanal.lstTitHeader[section])
        return _qc.QVariant(int(section + 1))