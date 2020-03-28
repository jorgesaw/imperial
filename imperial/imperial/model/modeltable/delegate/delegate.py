#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 24/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model.modeltable.modeldatatable.mdtEgreso import \
    ModeloDatosTablaEgreso
from imperial.model.modeltable.modeldatatable.mdtIngrediente import \
    ModeloDatosTablaIngred
from imperial.model.modeltable.modeldatatable.mdtProveedor import \
    ModeloDatosTablaProveedor
from imperial.model.modeltable.modeldatatable.mdtVendedor import \
    ModeloDatosTablaVendedor
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

class ProductoDelegate(_qg.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(ProductoDelegate, self).__init__(parent)
        
    def paint(self, painter, option, index):
        color = _qg.QColor(103, 103, 103)
        option.palette.setColor(_qg.QPalette.Highlight, color)
        
        _qg.QStyledItemDelegate.paint(self, painter, option, index)


class IngredienteDelegate(_qg.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(IngredienteDelegate, self).__init__(parent)
        
    def paint(self, painter, option, index):
        color = _qg.QColor(103, 103, 103)
        option.palette.setColor(_qg.QPalette.Highlight, color)
        
        _qg.QStyledItemDelegate.paint(self, painter, option, index)

    def sizeHint(self, option, index):
        fm = option.fontMetrics

        text = index.model().data(index).toString()
        document = _qg.QTextDocument()
        document.setDefaultFont(option.font)
        document.setHtml(text)
        if index.column() == ModeloDatosTablaIngred.NOM_INGRED:
            return _qc.QSize(document.idealWidth() + 230, fm.height())
        if index.column() == ModeloDatosTablaIngred.PRECIO_INGRED:
            return _qc.QSize(document.idealWidth() + 50, fm.height())
        if index.column() == ModeloDatosTablaIngred.UNIDAD_INGRED:
            return _qc.QSize(document.idealWidth() + 50, fm.height())
        if index.column() == ModeloDatosTablaIngred.CANT_UNIDAD_INGRED:
            return _qc.QSize(document.idealWidth() + 50, fm.height())
        
class EgresoDelegate(_qg.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(EgresoDelegate, self).__init__(parent)
        
    def paint(self, painter, option, index):
        color = _qg.QColor(103, 103, 103)
        option.palette.setColor(_qg.QPalette.Highlight, color)
        
        _qg.QStyledItemDelegate.paint(self, painter, option, index)

    def sizeHint(self, option, index):
        fm = option.fontMetrics

        text = index.model().data(index).toString()
        document = _qg.QTextDocument()
        document.setDefaultFont(option.font)
        document.setHtml(text)
        if index.column() == ModeloDatosTablaEgreso.NAME:
            return _qc.QSize(document.idealWidth() + 350, fm.height())
        
class ProveedorDelegate(_qg.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(ProveedorDelegate, self).__init__(parent)
        
    def paint(self, painter, option, index):
        color = _qg.QColor(103, 103, 103)
        option.palette.setColor(_qg.QPalette.Highlight, color)
        
        _qg.QStyledItemDelegate.paint(self, painter, option, index)

    def sizeHint(self, option, index):
        fm = option.fontMetrics

        text = index.model().data(index).toString()
        document = _qg.QTextDocument()
        document.setDefaultFont(option.font)
        document.setHtml(text)
        if index.column() == ModeloDatosTablaProveedor.NAME_PROV:
            return _qc.QSize(document.idealWidth() + 130, fm.height())
        if index.column() == ModeloDatosTablaProveedor.NAME_VENDEDOR_PROV:
            return _qc.QSize(document.idealWidth() + 130, fm.height())
        if index.column() == ModeloDatosTablaProveedor.TELEFONO:
            return _qc.QSize(document.idealWidth() + 50, fm.height())
        if index.column() == ModeloDatosTablaProveedor.CELULAR:
            return _qc.QSize(document.idealWidth() + 50, fm.height())
        
    
class VendedorDelegate(_qg.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(VendedorDelegate, self).__init__(parent)
        
    def paint(self, painter, option, index):
        color = _qg.QColor(103, 103, 103)
        option.palette.setColor(_qg.QPalette.Highlight, color)
        
        _qg.QStyledItemDelegate.paint(self, painter, option, index)

    def sizeHint(self, option, index):
        fm = option.fontMetrics

        text = index.model().data(index).toString()
        document = _qg.QTextDocument()
        document.setDefaultFont(option.font)
        document.setHtml(text)
        if index.column() == ModeloDatosTablaVendedor.NAME:
            return _qc.QSize(document.idealWidth() + 350, fm.height())