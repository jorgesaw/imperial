#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 06/07/2014

@author: jorgesaw
'''

import sys
sys.path.append('./')

from PyQt4.QtCore import (Qt, QAbstractTableModel, QModelIndex, QVariant)

class ModeloTabla(QAbstractTableModel):
    u"""Modelo para manejar los datos de forma tabular."""
    
    def __init__(self, modelo, modeloDatosTabla, parent=None):
        super(ModeloTabla, self).__init__(parent)

        self.datos = []
        self.modeloDatosTabla = modeloDatosTabla
        self.modelo = modelo

    def filaDato(self, row):
        return self.datos[row]

    def clear(self):
        self.datos = []
        self.reset()
        
    def updateTable(self):
        self.reset()

    def isDatos(self):
        return len(self.datos) > 0
    
    def setDatos(self, datos):
        self.datos = datos
        
    def cerrarSesionDAO(self):
        self.modelo.cerrarSesionDAO()
        
    def sortByColumn(self, col=-1):
        if len(self.datos) > 1:
            self.datos.sort()
            self.reset()
        
    def insertRows(self, position, lstDatos, rows=1, index=QModelIndex()):
        dato, msg = self.modelo.guardarDatos(lstDatos)
        if dato:
            self.beginInsertRows(QModelIndex(), position,
                        position + rows - 1)
            for row in range(rows):
                self.datos.insert(position + row,
                            dato)
            self.endInsertRows()
        return (dato is not None, msg)
    
    def insertRowInTable(self, dato, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position,
                        position + rows - 1)
        for row in range(rows):
            self.datos.insert(position + row,
                        dato)
        self.endInsertRows()
            
    def removeRows(self, position, rows=1, index=QModelIndex()):
        dato = self.datos[position]
        retorno, msg = self.modelo.eliminarDato(dato)
        
        if retorno > 0:
            self.removeRowsTabla(position, rows)
            
        return (retorno > 0, msg)

    def insertRowsTabla(self, position, datos):
        rows = len(datos)
        
        self.beginInsertRows(QModelIndex(), position,
                        position + rows - 1)
        for row in range(rows):
            self.datos.insert(position + row,
                        datos[row])
        self.endInsertRows()
        
    def removeRowsTabla(self, position, rows):
        self.beginRemoveRows(QModelIndex(), position,
                        position + rows - 1)
        self.datos = self.datos[:position] + \
                        self.datos[position + rows:]
        self.endRemoveRows()
            
    def editRows(self, index, lstDatos):
        row = index.row()
        datoUpdate = self.datos[row]
        
        retorno, msg = self.modelo.actualizarDatos(datoUpdate, lstDatos)
        
        return (retorno > 0, msg)
        
    def listData(self, reverse=False):
        retorno = 0
        datos, msg = self.modelo.listarDatos(reverse)
        if datos:
            self.datos = []
            self.datos = datos
            retorno = 1 # uHaydatos para mostrar.
            
        return (retorno > 0, msg) 

    def datosModelo(self, row):
        return self.modelo.datosModelo(self.datos[row])

    def rowCount(self, index=QModelIndex()):
        return len(self.datos)

    def columnCount(self, index=QModelIndex()):
        return self.modeloDatosTabla.columnCount()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or \
           not (0 <= index.row() <= len(self.datos)):
            return QVariant()
        dato = self.datos[index.row()]
        return self.modeloDatosTabla.data(index, dato, role)

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.datos):
            dato = self.datos[index.row()]
            return self.modeloDatosTabla.setData(self, index, value, dato, role)
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        return self.modeloDatosTabla.headerData(section, orientation, role)
    
    def flags(self, index=None):
        if index.isValid():
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable
    