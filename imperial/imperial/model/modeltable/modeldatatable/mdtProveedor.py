#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
                
class ModeloDatosTablaProveedor(object):
    u""""""

    NAME_PROV, NAME_VENDEDOR_PROV, TELEFONO, CELULAR, EMAIL, FECHA_ALTA, DIRECCION, \
        PISO_DEPTO, BARRIO, CIUDAD, PROVINCIA, EDITAR, ELIMINAR, DETALLE = range(14)

    lstHeader = [NAME_PROV, NAME_VENDEDOR_PROV, TELEFONO, CELULAR]
    
    lstHeaderProv = [NAME_PROV, NAME_VENDEDOR_PROV, TELEFONO, CELULAR, EMAIL, FECHA_ALTA, DIRECCION, \
        PISO_DEPTO,  BARRIO, CIUDAD, PROVINCIA, EDITAR, ELIMINAR, DETALLE]
             
    lstTitHeader = [u'Proveedor', u'Vendedor', u'Teléfono', u'Celular', u'Email', u'Fecha Alta', u'Dirección', 
        u'Piso - Depto.', u'Barrio', u'Ciudad', u'Provincia', u'Editar', 'Eliminar', 'Detalle']

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 14

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == ModeloDatosTablaProveedor.NAME_PROV:
                return _qc.QVariant(dato.nombre)
            if column == ModeloDatosTablaProveedor.NAME_VENDEDOR_PROV:
                if dato.vendedorProv:
                    return _qc.QVariant(dato.vendedorProv.nombre)
                else:
                    return _qc.QVariant()
            elif column == ModeloDatosTablaProveedor.TELEFONO:
                return _qc.QVariant(dato.telefono)
            elif column == ModeloDatosTablaProveedor.CELULAR:
                return _qc.QVariant(dato.celular)
            elif column == ModeloDatosTablaProveedor.EMAIL:
                return _qc.QVariant(dato.email)
            elif column == ModeloDatosTablaProveedor.FECHA_ALTA:
                return _qc.QVariant(dato.fecha_alta)
            elif column == ModeloDatosTablaProveedor.DIRECCION:
                return _qc.QVariant(dato.direccion.calle + " " + dato.direccion.altura)
            elif column == ModeloDatosTablaProveedor.PISO_DEPTO:
                return _qc.QVariant(unicode(dato.direccion.piso) + " " + dato.direccion.depto)
            elif column == ModeloDatosTablaProveedor.BARRIO:
                return _qc.QVariant(dato.direccion.barrio)
            elif column == ModeloDatosTablaProveedor.CIUDAD:
                if dato.ciudad:
                    return _qc.QVariant(dato.ciudad.nomCiudad)
                else:
                    return _qc.QVariant()
            elif column == ModeloDatosTablaProveedor.PROVINCIA:
                if dato.ciudad and dato.ciudad.provincia:                    
                    return _qc.QVariant(dato.ciudad.provincia.nombre)
                else:
                    return _qc.QVariant()
            #elif column == DESCRIPTION:
            #   return _qc.QVariant(dato.description)
            elif column == ModeloDatosTablaProveedor.EDITAR:
                return _qc.QVariant('Editar')
            elif column == ModeloDatosTablaProveedor.ELIMINAR:
                return _qc.QVariant('Eliminar')
            elif column == ModeloDatosTablaProveedor.DETALLE:
                return _qc.QVariant('Detalle')
            
        elif role == _qc.Qt.DecorationRole:
            if column == ModeloDatosTablaProveedor.EDITAR:
                return _qg.QIcon(':/printer.png')
            if column == ModeloDatosTablaProveedor.ELIMINAR:
                return _qg.QIcon(':/persona.png')
            if column == ModeloDatosTablaProveedor.DETALLE:
                return _qg.QIcon(':/favicon.png')
            
        elif role == _qc.Qt.TextAlignmentRole:
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.BackgroundColorRole:
            if index.row() % 2 == 0:
                return _qc.QVariant(_qg.QColor(58, 216, 58))
            return _qc.QVariant(_qg.QColor(155, 216, 155))
        elif role == _qc.Qt.ToolTipRole:
            if column == ModeloDatosTablaProveedor.NAME_PROV:
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
            if section in ModeloDatosTablaProveedor.lstHeaderProv:
                return _qc.QVariant(ModeloDatosTablaProveedor.lstTitHeader[section])
        return _qc.QVariant(int(section + 1))