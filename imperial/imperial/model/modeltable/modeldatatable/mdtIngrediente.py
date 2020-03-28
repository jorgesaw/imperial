#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model.models import Ingrediente
from imperial.util import variables
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

class ModeloDatosTablaIngred(object):
    u""""""
    
    NOM_INGRED, PRECIO_INGRED, UNIDAD_INGRED, CANT_UNIDAD_INGRED, EDITAR, ELIMINAR  = range(6)

    lstHeader = [NOM_INGRED, PRECIO_INGRED, UNIDAD_INGRED, CANT_UNIDAD_INGRED, EDITAR, ELIMINAR]

    lstTitHeader = [u'Ingrediente', u'Precio ($)', u'Unidad', u'Cantidad x Unidad', u'Editar', 'Eliminar']

    def __init__(self):
        pass
    
    def columnCount(self, index=_qc.QModelIndex()):
        return 6

    def data(self, index, dato, role=_qc.Qt.DisplayRole):
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == ModeloDatosTablaIngred.NOM_INGRED:
                return _qc.QVariant(dato.nombre)
            if column == ModeloDatosTablaIngred.PRECIO_INGRED:
                precio = 0.0
                if len(dato.colPrecioIngred) > 0:
                    precio = dato.colPrecioIngred[len(dato.colPrecioIngred) - 1].precio
                return _qc.QVariant((_qc.QString("%L1").\
                                     arg('{:.2f}'.format(precio))))
            if column == ModeloDatosTablaIngred.UNIDAD_INGRED:
                return _qc.QVariant(Ingrediente.LST_UNIDADES[dato.unidad])
            if column == ModeloDatosTablaIngred.CANT_UNIDAD_INGRED:
                if dato.cantUnidad > 0:
                    return _qc.QVariant(unicode(dato.cantUnidad) + \
                                " " + Ingrediente.LST_MULTIPLO_UND[dato.unidad])
                else:
                    cant = unicode(Ingrediente.LST_CANT_UNIDADADES[dato.cantUnidad + 1])
                    if dato.cantUnidad == 0:
                        unidad = Ingrediente.LST_UNIDADES[dato.unidad]
                    else:
                        unidad = Ingrediente.LST_MULTIPLO_UND[dato.unidad]
                    return _qc.QVariant(cant + unidad)
                    #return _qc.QVariant(unicode(Ingrediente.CANT_UNIDAD_KG_LTS) + \
                    #           " " + Ingrediente.LST_MULTIPLO_UND[dato.unidad])
            elif column == ModeloDatosTablaIngred.EDITAR:
                return _qc.QVariant('Editar')
            elif column == ModeloDatosTablaIngred.ELIMINAR:
                return _qc.QVariant('Eliminar')
            
        elif role == _qc.Qt.DecorationRole:
            if column == ModeloDatosTablaIngred.EDITAR:
                return _qg.QIcon(variables.ICON_PATH_EDIT)
            if column == ModeloDatosTablaIngred.ELIMINAR:
                return _qg.QIcon(variables.ICON_PATH_REMOVE)
            
        elif role == _qc.Qt.TextAlignmentRole:
            if column in (ModeloDatosTablaIngred.PRECIO_INGRED, 
                          ModeloDatosTablaIngred.UNIDAD_INGRED, 
                          ModeloDatosTablaIngred.CANT_UNIDAD_INGRED):
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
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
            if column == ModeloDatosTablaIngred.NOM_INGRED:
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
            if section in ModeloDatosTablaIngred.lstHeader:
                return _qc.QVariant(ModeloDatosTablaIngred.lstTitHeader[section])
        return _qc.QVariant(int(section + 1))