#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 03/04/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.datamodel.dataModel import DataModel
from imperial.dao.DAOSaldos import DAOSaldos
from imperial.model import models
from imperial.model.models import Vendedor, Egreso, Venta, MovEgreso, \
    Ingrediente, MovCostoIngred, CostoProd
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

NOMBRE, CANT, UND, PRECIO_INGRED, COSTO = range(5)

lstHeader = [NOMBRE, CANT, UND, PRECIO_INGRED, COSTO]

lstTitHeader = ['INGREDIENTE', 'CANT.', 'UND.', u'PRECIO INGRED.', 'COSTO']

class TableModelCostosProd(_qc.QAbstractTableModel):
    u""""""
    
    def __init__(self, modelo=None):
        super(TableModelCostosProd, self).__init__()
        
        self.modelo = modelo
        self.datos = []
        self.dao = None
        self.costoProd = None
        
        self.dicDatos = {}
        
        self.vista = None
        self.datosNuevos = True #Controla si los datos on para guardar o actualizar.
        
        self.lstSaldos = []
        
        self.getDatos()
        self.dataChanged[_qc.QModelIndex, _qc.QModelIndex].connect(self.cambiarTotales)
        
    def setDatos(self, lstDatos):
        self.datos = []
        self.datos = lstDatos
        self.reset()
        
    def filaDato(self, row):
        return self.datos[row]

    def clear(self):
        self.datos = []
        self.reset()
        
    def isDatos(self):
        return len(self.datos) > 0
    
    def isDatosCosto(self):
        return self.costoProd != None
    
    def rowCount(self, index=_qc.QModelIndex()):
        return len(self.datos)

    def columnCount(self, index=_qc.QModelIndex()):
        return 5
    
    def cerrarSesionDAO(self):
        self.modelo.cerrarSesionDAO()
    
    def limpiarValores(self):
        #for lstValores in self.datos:
        #   lstValores[1] = 0.0
        self.datos = []
        self.costoProd = None
        self.reset()
    
    def getDatos(self):
        self.datosIngred = self.modelo.dao.getAll(Ingrediente) 
        self.lstIngred = []
        
        for ingrediente in self.datosIngred:
            ingrediente.precioActivo()
            self.lstIngred.append(ingrediente.nombre)
        
        #self.lstIngred = [dato.nombre for dato in self.datosIngred]
    
        
    @_qc.pyqtSlot("QModelIndex, QModelIndex")        
    def cambiarTotales(self, index=None, index2=None):
        mov = self.datos[index.row()]
        mov.calcular()
        #mov.total = mov.cant/1000* mov.ingrediente.colPrecioIngred[0].precio
        #print('::::::::::::::::')
        self.calcularDatosCosto()
        self.reset()
        
    def crearDatos(self, lstDatos):
        fecha = lstDatos[0]
        prod = lstDatos[4]
        colMovCostoIngred = []
        
        if self.datosNuevos:#EuEs la primera vez que se crea un costo para este producto.
                #uY el costo ya fué creado en el método buscarDatos.
            colMovCostoIngred = self.datos
        else:#Creamos uno nuevo porque ya existen otros.
            self.modelo.dao.cerrarSesion()
            
            for movCostoAnterior in self.datos:
                nuevoMovCostoIngred = movCostoAnterior.copy()
                nuevoMovCostoIngred.ingredienteStr = nuevoMovCostoIngred.ingrediente.nombre
                colMovCostoIngred.append(nuevoMovCostoIngred)
                
            self.costoProd = CostoProd(prod, fecha)
            self.datos = colMovCostoIngred             
        
        self.datosNuevos=True
        self.costoProd.colMovCostoIngred = colMovCostoIngred
        
        self.costoProd.gastos = lstDatos[models.GASTOS_COSTO_X]
        self.costoProd.cant = lstDatos[models.CANTIDAD_PROD_X]
        self.costoProd.desc = lstDatos[models.DESC_COSTO_X]
        
    def guardarDatos(self, lstDatos):
        if self.datosNuevos:
            msg = DataModel.LST_MSG[DataModel.MSG_SAVE]
            
            retorno = self.modelo.dao.insert(self.costoProd)
            
            if retorno <= 0:
                msg = DataModel.LST_MSG[DataModel.MSG_NOT_SAVE]
            else:
                self.datosNuevos = False
            
            return (retorno > 0, msg)
        return self.actualizarDatos(lstDatos)
        
    def calcularDatosCosto(self):
        self.costoProd.calcular()
        
        self.vista.setTotalCosto(self.costoProd.total)
        
    def getTotalCostoProd(self):
        self.costoProd.calcular()
        return self.costoProd.total
    
    def addIngrediente(self):
        mov = MovCostoIngred(self.datosIngred[0], 0)
        mov.ingredienteStr = self.datosIngred[0].nombre
        
        self.insertRowInTable(mov, self.rowCount())
    
    def removeRows(self, position, rows=1, index=_qc.QModelIndex()):
        #dato = self.datos[position]
        #retorno, msg = self.modelo.eliminarDato(dato)
        retorno = 1
        msg = ''
        
        if retorno > 0:
            self.costoProd.delMovCosto(position)
            self.removeRowsTabla(position, rows)
            
        return (retorno > 0, msg)
    
    def removeRowsTabla(self, position, rows):
        self.beginRemoveRows(_qc.QModelIndex(), position,
                        position + rows - 1)
        self.datos = self.datos[:position] + \
                        self.datos[position + rows:]
        self.endRemoveRows()
        
    def actualizarDatos(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_EDIT]
        
        self.costoProd.gastos = lstDatos[models.GASTOS_COSTO_X]
        self.costoProd.cant = lstDatos[models.CANTIDAD_PROD_X]
        self.costoProd.desc = lstDatos[models.DESC_COSTO_X]
        retorno = self.modelo.dao.update(self.costoProd)
        
        if retorno <= 0:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_EDIT]
        
        return (retorno > 0, msg)
                
    def buscarDatos(self, lstDatos):
        self.datos = []
        msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
        ok = False
        
        fecha = lstDatos[0]
        prod = lstDatos[4]
        
        self.costoProd = self.modelo.dao.getCostosByFechaProd([fecha, prod])
        
        if self.costoProd:
            self.datosNuevos = False
            msg = DataModel.LST_MSG[DataModel.MSG_LIST]
            ok = True
            self.calcularDatosCosto() #Muestra el costo total y le avisa a la vista que muestre el costo.
            self.mostrarDatosCosto(fecha) #Actualiza los atributos calculables que no se guardan en la DB.
            self.vista.setData([self.costoProd.gastos, self.costoProd.cant, 
                                self.costoProd.desc])
        else:
            self.costoProd = CostoProd(prod, fecha)
            self.datosNuevos = True
            
        self.datos = self.costoProd.colMovCostoIngred
        
        self.calcularDatosCosto()
        
        self.reset()
        
        return (ok, msg)
    
    def mostrarDatosCosto(self, fecha):
        for mov in self.costoProd.colMovCostoIngred:
            mov.ingredienteStr = mov.ingrediente.nombre
            mov.setPrecioUnitario(fecha)
            mov.calcular()
            
    def getAllProducts(self):
        lstProductos = self.modelo.dao.getAllProducts()
        return lstProductos
    
    def datos2Array(self, costo_x_unidad):
        from imperial.model.modeltable import tableModelCostosProd
        
        lst_resaltados = []
        lst_datos_tabla = []
        
        for mov_costo_ingred in self.datos:
            lst_dato_row = [mov_costo_ingred.ingredienteStr[:36], 
                            mov_costo_ingred.cant]
            
            cant = mov_costo_ingred.ingrediente.cantUnidad
            cadena = ''
            if cant > Ingrediente.CANT_UNIDAD_KG_LTS_X1:
                cadena = '{} ({})'.format(Ingrediente.LST_UNIDADES[mov_costo_ingred.ingrediente.unidad], cant)
            else:
                cant_unidad = Ingrediente.LST_MULTIPLO_UND[mov_costo_ingred.ingrediente.unidad] #uMido por submúltiplo.
                if cant == Ingrediente.CANT_UNIDAD_KG_LTS_X1: #u Si se mide por múltiplo.
                    cant_unidad = Ingrediente.LST_UNIDADES[mov_costo_ingred.ingrediente.unidad]
                
                cadena = '{} ({})'.format(Ingrediente.LST_CANT_UNIDADADES[cant + 1], 
                            cant_unidad)
            
            lst_dato_row.append(cadena)
            lst_dato_row.append(mov_costo_ingred.ingrediente.precio)
            lst_dato_row.append(mov_costo_ingred.costo)
            
            lst_datos_tabla.append(lst_dato_row)
        
        lst_datos_extras = [self.costoProd.total, self.costoProd.gastos, 
                            self.costoProd.cant, costo_x_unidad, 
                            self.costoProd.desc]
        
        lstDatos = [lst_datos_tabla, lst_datos_extras]

        return (['INGREDIENTE', 'CANT.', 'UND.', u'PREC ING', 'COSTO'], 
                lstDatos, lst_resaltados)
    
            
    def insertRowInTable(self, dato, position, rows=1, index=_qc.QModelIndex()):
        self.beginInsertRows(_qc.QModelIndex(), position,
                        position + rows - 1)
        for row in range(rows):
            self.datos.insert(position + row,
                        dato)
        self.endInsertRows()
    
    def insertRows(self, position, rows=1, index=_qc.QModelIndex()):
        self.beginInsertRows(_qc.QModelIndex(), position,
                             position + rows - 1)
        for row in range(rows):
            self.datos.insert(position + row, 0)
        self.endInsertRows()
        return True
    
    def data(self, index, role=_qc.Qt.DisplayRole):
        if not index.isValid() or \
           not (0 <= index.row() <= len(self.datos)):
            return _qc.QVariant()
        dato = self.datos[index.row()]
        column = index.column()
        if role == _qc.Qt.DisplayRole:
            if column == NOMBRE:
                #return _qc.QVariant(dato.ingrediente)
                return _qc.QVariant(dato.ingredienteStr)
            if column == CANT:
                return _qc.QVariant(dato.cant)
            #if column == UND_USADA:
            #   und = Ingrediente.LST_MULTIPLO_UND[dato.ingrediente.unidad]
            #  if dato.ingrediente.cantUnidad == Ingrediente.CANT_UNIDAD_KG_LTS_X1:
            #     und = Ingrediente.LST_UNIDADES[dato.ingrediente.cantUnidad + 1]
            #  return _qc.QVariant(und)
            if column == UND:
                cant = dato.ingrediente.cantUnidad
                cadena = ''
                if cant > Ingrediente.CANT_UNIDAD_KG_LTS_X1:
                    cadena = '{} ({})'.format(Ingrediente.LST_UNIDADES[dato.ingrediente.unidad], cant)
                else:
                    cant_unidad = Ingrediente.LST_MULTIPLO_UND[dato.ingrediente.unidad] #uMido por submúltiplo.
                    if cant == Ingrediente.CANT_UNIDAD_KG_LTS_X1: #u Si se mide por múltiplo.
                        cant_unidad = Ingrediente.LST_UNIDADES[dato.ingrediente.unidad]
                    
                    cadena = '{} ({})'.format(Ingrediente.LST_CANT_UNIDADADES[cant + 1], 
                                cant_unidad)
                return _qc.QVariant(cadena)
            if column == PRECIO_INGRED:
                return _qc.QVariant(dato.ingrediente.precio)
            if column == COSTO:
                return _qc.QVariant(dato.costo)
                #return QVariant(QString("%L1").arg(numero, 5, 10, QChar('0')))
                #return QVariant(QString("%L1").arg(numero))
        elif role == _qc.Qt.TextAlignmentRole:
            if column in(PRECIO_INGRED, COSTO):
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.TextColorRole and column == CANT:
            pass
            #decena = int(str(numero)[-2:] if len(str(numero)) >=2 else str(numero))
            #if decena < 1 or decena > 90:
             #   return _qc.QVariant(_qg.QColor(_qc.Qt.darkRed))
            #else:
             #   return _qc.QVariant(_qg.QColor(_qc.Qt.green))
             
        elif role == _qc.Qt.BackgroundColorRole:
            if index.row() % 2 == 0:
                return _qc.QVariant(_qg.QColor(58, 216, 58))
            return _qc.QVariant(_qg.QColor(155, 216, 155))
                
        return _qc.QVariant()
    
    def setData(self, index, value, role=_qc.Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.datos):
            dato = self.datos[index.row()]
            column = index.column()
            if column == CANT:
                #value, ok = value.toInt()
                #if ok:
                    #self.datos[index.row()] = value
                dato.cant = value
            elif column == NOMBRE:
                #dato.ingrediente = value.toString()
                dato.ingredienteStr = value.toString()
                for ingred in self.datosIngred:
                    if ingred.nombre == dato.ingredienteStr:
                        dato.setIngrediente(ingred)
            self.emit(_qc.SIGNAL("dataChanged(QModelIndex, QModelIndex)"),
                      index, index)
            return True
        return False
    
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
    
    def flags(self, index):
        if not index.isValid():
            return _qc.Qt.ItemIsEnabled
        column = index.column()
        if column in (NOMBRE, CANT):
            return _qc.Qt.ItemFlags(_qc.QAbstractTableModel.flags(self, index) |
                            _qc.Qt.ItemIsEditable)
        else:
            return _qc.Qt.ItemIsEnabled
        
    def lstIngredientes(self):
        return (Ingrediente('Sal', '100'), 
                Ingrediente('Harina', '230'), 
                Ingrediente('Aceite', '60'), 
                Ingrediente('Azúcar', '77'), 
                Ingrediente('Colorante', '100'), 
                )

class CostosProdDelegate(_qg.QItemDelegate):
    def __init__(self, parent=None):
        super(CostosProdDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == CANT:
            dSpin = _qg.QDoubleSpinBox(parent)
            dSpin.setRange(0.00, 999999.99)
            dSpin.setSingleStep(1)
            #dSpin.setPrefix("")
            dSpin.setValue(0.00)
            dSpin.setAlignment(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter)
            return dSpin
        elif index.column() == NOMBRE:
            combobox = _qg.QComboBox(parent)
            combobox.addItems(sorted(index.model().lstIngred))
            combobox.setEditable(False)
            return combobox
        else:
            return _qg.QItemDelegate.createEditor(self, parent, option,
                    index)
            
    def setEditorData(self, editor, index):
        text = index.model().data(index, _qc.Qt.DisplayRole).toString()
        if index.column() == CANT:
            value = text.toInt()[0]
            editor.setValue(value)
            #model.setData(index, _qc.QVariant(editor.text()))
        elif index.column() ==  NOMBRE:
            i = editor.findText(text)
            if i == -1:
                i=0
            editor.setCurrentIndex(i)
        else:
            _qg.QItemDelegate.setEditorData(self, editor, index)
            
    def setModelData(self, editor, model, index):
        if index.column() == CANT:
            #model.setData(index, QVariant(editor.value()))
            model.setData(index, editor.value())
        elif index.column() == NOMBRE:
            model.setData(index, _qc.QVariant(editor.currentText()))
        else:
            _qg.QItemDelegate.setModelData(self, editor, model, index)

    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (_qg.QDoubleSpinBox)):
            self.emit(_qc.SIGNAL("commitData(QWidget*)"), editor)
            self.emit(_qc.SIGNAL("closeEditor(QWidget*)"), editor)