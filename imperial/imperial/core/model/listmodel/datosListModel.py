#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from imperial.core.util.ManejaFechas import ManejaFechas

class DatosListModel(QAbstractListModel):
    u"""Modelo para manejar los datos que se pueden agregar a un
        combo o una lista"""

    def __init__(self, modeloDatos, seleccionar=True):
        super(DatosListModel, self).__init__()

        self.seleccionar = seleccionar
        self.setModel(modeloDatos)

    def setModel(self, modeloDatos):
        self.datos = []
        self.datos = modeloDatos
        if self.seleccionar:
            self.datos.insert(0, "Seleccionar")
        
    def rowCount(self, index=QModelIndex()):
        return len(self.datos)

    def columnCount(self, index=QModelIndex()):
        return 1

    def getData(self, index):
        return self.datos[index]

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or \
           not (0 <= index.row() <= len(self.datos)):
            return QVariant()
        dato = self.datos[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if (isinstance(dato, str)):
                return QVariant(unicode(dato))
            else:   
                return QVariant(dato.__str__())
        
        return QVariant()