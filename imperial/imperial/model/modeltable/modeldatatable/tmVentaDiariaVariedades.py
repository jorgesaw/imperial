#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 03/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.MsgBox import MsgBox
from imperial.core.model.datamodel.dataModel import DataModel
from imperial.dao.DAOProducto import DAOProducto
from imperial.model.models import VentaProd
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime

NOM_PROD, CARGA_1, CARGA_2, CARGA_3, \
CARGA_4, CARGA_5, CARGA_6, TOTAL_CANT, DEVOL, TOT_NETO_CANT, \
PRECIO_VENTA, TOT_VENTA = range(12)

lstHeader = [NOM_PROD, CARGA_1, CARGA_2, CARGA_3, 
CARGA_4, CARGA_5, CARGA_6, TOTAL_CANT, DEVOL, TOT_NETO_CANT, 
PRECIO_VENTA, TOT_VENTA]

lstTitHeader = [u'Producto', u'Carga 1', u'Carga 2', u'Carga 3',
                u'Carga 4', u'Carga 5', u'Carga 6', u'Tot. carga', u'Devoluciones', 
                u'Cant. Neta', u'Precio venta', u'Tot. Ventas']

class TMVentaDiariaVariedades(_qc.QAbstractTableModel):
    u""""""
    
    def __init__(self, modelo=None):
        super(TMVentaDiariaVariedades, self).__init__()
        
        self.modelo = modelo
        self.datos = []
        self.dao = None
        self.modeloPadre = None
        self.categoria = 0
        
        self.dicDatos = {}
        
        #self.getDatos(datetime.date.today(), 1)
    
        self.tableView = None
        self.datosNuevos = True #Controla si los datos son para guardar o actualizar.
        self.dataChanged[_qc.QModelIndex, _qc.QModelIndex].connect(self.cambiarTotales)
        #self.connect(self, _qc.SIGNAL('CAMBIOS()'), self.cambios)
        
        self.mov_venta_prod = None
        
        self.ventana = None
        self.total_ventas = 0.0
        
    def totalVentas(self):
        self.total_ventas = 0.0
        for ventaProd in self.datos:
            self.total_ventas = self.total_ventas + ventaProd.costo
            
        return self.total_ventas    
    @_qc.pyqtSlot("QModelIndex, QModelIndex")
    def cambiarTotales(self, index=None, index2=None):
        #total = 0.0
        #for dato in self.datos:
         #   tot = dato.cant_inicial
          #  for i in range(VentaProd.CANT_CARGAS):
           #     tot = tot + dato.colCargaProd[i].cant
            #dato.tot_venta = tot
            #print('DATO_PRECIO:', dato.producto.price)
            #print('DATO_TOT_VENTA:', dato.tot_venta)
            #print('DATO_DEVOLUCIONES:', dato.devoluciones)
            #print('TOT_DATO:', dato.producto.price * (dato.tot_venta - dato.devoluciones))
            
            #total = total + dato.producto.precio * (dato.tot_venta - dato.devoluciones)
            #print('TOTAL:', total)
            
        ventaProd = self.datos[index.row()]
        ventaProd.totVentas()
        ventaProd.cantNeta()
        ventaProd.calcular()
        
        #self.reset()
        #self.mov_venta_prod.calcular()
        
        #self.ventana.cambiarTotales([self.total, self.total, 2 * self.total])
        
        self.modeloPadre.avisarCambioDatos(self.categoria)
        
    def actualizarTotalDatos(self, fecha):
        for ventaProd in self.datos:
            ventaProd.setPrecioUnitario(fecha)
            ventaProd.totVentas()
            ventaProd.cantNeta()
            ventaProd.calcular()
            
    def actualizarPrecioProd(self, fecha):
        for ventaProd in self.datos:
            ventaProd.setPrecioUnitario(fecha)
    
    def filaDato(self, row):
        return self.datos[row]

    def clear(self):
        self.datos = []
        self.reset()

    def rowCount(self, index=_qc.QModelIndex()):
        return len(list(self.datos))

    def columnCount(self, index=_qc.QModelIndex()):
        return 12
    
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
            if column == NOM_PROD:
                return _qc.QVariant(dato.producto.name)
            if column == CARGA_1:
                return _qc.QVariant(dato.colCargaProd[0].cant)
            if column == CARGA_2:
                return _qc.QVariant(dato.colCargaProd[1].cant)
            if column == CARGA_3:
                return _qc.QVariant(dato.colCargaProd[2].cant)
            if column == CARGA_4:
                return _qc.QVariant(dato.colCargaProd[3].cant)
            if column == CARGA_5:
                return _qc.QVariant(dato.colCargaProd[4].cant)
            if column == CARGA_6:
                return _qc.QVariant(dato.colCargaProd[5].cant)
            if column == TOTAL_CANT:
                #tot = dato.cant_inicial
                #for i in range(VentaProd.CANT_CARGAS):
                #   tot = tot + dato.colCargaProd[i].cant
                #dato.tot_venta = tot
                return _qc.QVariant(dato.totVentas())
            if column == DEVOL:
                return _qc.QVariant(dato.devoluciones)
            if column == TOT_NETO_CANT:
                #return _qc.QVariant(dato.tot_venta - dato.devoluciones)
                return _qc.QVariant(dato.cantNeta())
            if column == PRECIO_VENTA:
                return _qc.QVariant(dato.producto.precio)
            if column == TOT_VENTA:
                #return _qc.QVariant(dato.producto.price * (dato.tot_venta - dato.devoluciones))
                return _qc.QVariant(dato.calcular())
        
        elif role == _qc.Qt.TextAlignmentRole:
            if column == CARGA_6 or column == CARGA_1 or column == CARGA_2\
                or column == CARGA_3 or column == CARGA_4 or column == CARGA_5\
                or column == DEVOL or column == TOTAL_CANT or column == PRECIO_VENTA\
                or column == TOT_NETO_CANT or column == TOT_VENTA:
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        
        elif role == _qc.Qt.TextColorRole and column == NOM_PROD:
            return _qc.QVariant(_qg.QColor(_qc.Qt.white))
            #decena = int(str(numero)[-2:] if len(str(numero)) >=2 else str(numero))
            #if decena < 1 or decena > 90:
            #   return _qc.QVariant(_qg.QColor(_qc.Qt.darkRed))
            #else:
            #   return _qc.QVariant(_qg.QColor(_qc.Qt.green))
            
        elif role == _qc.Qt.FontRole:
            font = _qg.QFont('Helvetica', 11, _qg.QFont.Bold)
            if column > 0:
                font = _qg.QFont('Helvetica', 11, _qg.QFont.Bold)
            return _qc.QVariant(font)
        
        elif role == _qc.Qt.BackgroundColorRole:
            if column == NOM_PROD:
                return _qc.QVariant(_qg.QColor(107, 107, 107))
            if column in [TOT_NETO_CANT, TOT_VENTA]:
                    return _qc.QVariant(_qg.QColor(155, 216, 155))
            if column == DEVOL:
                return _qc.QVariant(_qg.QColor(216, 66, 58))
        return _qc.QVariant()
    
    def setData(self, index, value, role=_qc.Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.datos):
            dato = self.datos[index.row()]
            column = index.column()
            if column == NOM_PROD:
                dato.producto.name = value
            elif column in (CARGA_1, CARGA_2, CARGA_3, 
                            CARGA_4, CARGA_5, CARGA_6):
                is_set_dato = True
                if dato.colCargaProd[column - 1].cant > 0:
                    _qc.QCoreApplication.processEvents()
                    if not MsgBox.okToContinue(self.ventana, 
                                           'Venta diaria', 
                            u'La celda ya contiene un dato.\n¿Desea modificarla?'):
                        is_set_dato = False
                        #dato.colCargaProd[column - 1].cant = value
                if is_set_dato:
                    cant_items = dato.tot_venta + (value - dato.colCargaProd[column - 1].cant)
                    dato.colCargaProd[column - 1].cant = value
                    if dato.devoluciones > cant_items: #uSi las devoluciones superan la cantde ítems
                        dato.devoluciones = cant_items #u Las devoluciones igualan a los ítems
                #print('CANT_ITEMS:', cant_items)
                #print('CANT_DEVOLUCIONES:', dato.devoluciones)
            #elif column == CARGA_1:
            #    dato.colCargaProd[0].cant = value
            #elif column == CARGA_2:
            #    dato.colCargaProd[1].cant = value
            #elif column == CARGA_3:
            #    dato.colCargaProd[2].cant = value
            #elif column == CARGA_4:
            #    dato.colCargaProd[3].cant = value
            #elif column == CARGA_5:
            #    dato.colCargaProd[4].cant = value
            #elif column == CARGA_6:
            #    dato.colCargaProd[5].cant = value
            elif column == TOTAL_CANT:
                dato.tot_cant = value
            elif column == DEVOL:
                #if dato.devoluciones > dato.tot_venta:
                #   print('Datos:', dato.devoluciones)
                if not dato.setDevoluciones(value):
                    _qc.QCoreApplication.processEvents()
                    msg = u'Imposible cargar el valor.\nLas devoluciones no pueden superar\n' +\
                                u'el número de productos entregados'
                    _qg.QMessageBox.information(self.ventana, "Devoluciones", msg)
                #dato.devoluciones = value
            elif column == TOT_NETO_CANT:
                dato.tot_neto_cant = value
            elif column == PRECIO_VENTA:
                pass
            elif column == TOT_VENTA:
                dato.tot_venta = value
            self.emit(_qc.SIGNAL("dataChanged(QModelIndex, QModelIndex)"),
                      index, index)
            
            #self.emit(_qc.SIGNAL('CAMBIOS()'))
            
            return True
        return False
    
    def headerData(self, section, orientation, role=_qc.Qt.DisplayRole):
        if role == _qc.Qt.DisplayRole:
            if orientation == _qc.Qt.Horizontal:
                if section in lstHeader:
                    return _qc.QVariant(lstTitHeader[section])
                
        if role == _qc.Qt.FontRole:
            font = _qg.QFont('Helvetica', 9, _qg.QFont.Bold)
            return _qc.QVariant(font)
                
        if role == _qc.Qt.TextAlignmentRole:
            if orientation == _qc.Qt.Horizontal:
                return _qc.QVariant(int(_qc.Qt.AlignHCenter|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            
        #return _qc.QVariant(int(section + 1))
    
    def flags(self, index):
        if not index.isValid():
            return _qc.Qt.ItemIsEnabled
        column = index.column()
        if column == CARGA_6 or column == CARGA_1 or column == CARGA_2\
                or column == CARGA_3 or column == CARGA_4 or column == CARGA_5\
                or column == DEVOL or column == PRECIO_VENTA:
            return _qc.Qt.ItemFlags(_qc.QAbstractTableModel.flags(self, index) |
                            _qc.Qt.ItemIsEditable)
        else:
            return _qc.Qt.ItemIsEnabled | _qc.Qt.ItemIsSelectable

class VentaDiariaVariedadesDelegate(_qg.QItemDelegate):
    def __init__(self, parent=None):
        super(VentaDiariaVariedadesDelegate, self).__init__(parent)
        
        #self.connect(self, _qc.SIGNAL("closeEditor(QWidget*)"), self.cambios)
    
    @_qc.pyqtSlot("QWidget*")    
    def cambios(self, widget):
        pass
    
    def paint(self, painter, option, index):
        color = _qg.QColor(199, 199, 199)
        option.palette.setColor(_qg.QPalette.Highlight, color)
        
        _qg.QItemDelegate.paint(self, painter, option, index)
    
    def sizeHint(self, option, index):
        fm = option.fontMetrics

        text = index.model().data(index).toString()
        document = _qg.QTextDocument()
        document.setDefaultFont(option.font)
        document.setHtml(text)
        
        if index.column() in [CARGA_1, CARGA_2, CARGA_3, \
                CARGA_4, CARGA_5, CARGA_6, TOTAL_CANT, DEVOL, TOT_NETO_CANT, \
                PRECIO_VENTA, TOT_VENTA]:
            return _qc.QSize(document.idealWidth() + 30, fm.height())
        if index.column() == NOM_PROD:
            return _qc.QSize(document.idealWidth() + 10, fm.height())

    def createEditor(self, parent, option, index):
        if index.column() == PRECIO_VENTA:
            dSpin = _qg.QDoubleSpinBox(parent)
            dSpin.setLocale(_qc.QLocale('QLatin1Char'))
            dSpin.setRange(0.00, 999999.99)
            dSpin.setSingleStep(1)
            #dSpin.setPrefix("$ ")
            font = _qg.QFont('Helvetica', 11, _qg.QFont.Bold)
            dSpin.setFont(font)
            dSpin.setValue(0.00)
            dSpin.setAlignment(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter)
            return dSpin
        elif index.column() in (CARGA_1,  CARGA_2, CARGA_3, CARGA_4, CARGA_5, CARGA_6, DEVOL):
            iSpin = _qg.QDoubleSpinBox(parent)
            iSpin.setLocale(_qc.QLocale('QLatin1Char'))
            iSpin.setRange(0.00, 999999.99)
            iSpin.setSingleStep(1)
            font = _qg.QFont('Helvetica', 11, _qg.QFont.Bold)
            iSpin.setFont(font)
            iSpin.setValue(0)
            iSpin.setAlignment(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter)
            return iSpin
        else:
            return _qg.QItemDelegate.createEditor(self, parent, option,
                    index)
            
    def setEditorData(self, editor, index):
        text = index.model().data(index, _qc.Qt.DisplayRole).toString()
        if index.column() == CARGA_6 or index.column() == CARGA_1 or index.column() == CARGA_2\
            or index.column() == CARGA_3 or index.column() == CARGA_4 or index.column() == CARGA_5\
            or index.column() == DEVOL:
            value = text.toInt()[0]
            editor.setValue(value)
            #model.setData(index, _qc.QVariant(editor.text()))
        elif index.column() == PRECIO_VENTA:
            value = text#.toString()[0]
            editor.setValue(float(value))
        else:
            _qg.QItemDelegate.setEditorData(self, editor, index)
        
            
    def setModelData(self, editor, model, index):
        if index.column() == index.column() == CARGA_1 or index.column() == CARGA_2 \
            or index.column() == CARGA_3 or index.column() == CARGA_4 or index.column() == CARGA_5 \
            or index.column() == CARGA_6 or index.column() == DEVOL or index.column() == PRECIO_VENTA:
            #model.setData(index, QVariant(editor.value()))
            model.setData(index, editor.value())
        else:
            _qg.QItemDelegate.setModelData(self, editor, model, index)

    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (_qg.QDoubleSpinBox)):
            self.emit(_qc.SIGNAL("commitData(QWidget*)"), editor)
            self.emit(_qc.SIGNAL("closeEditor(QWidget*)"), editor)