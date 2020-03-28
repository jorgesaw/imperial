#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 02/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.datamodel.dataModel import DataModel
from imperial.model.models import ResumenFiscal
from imperial.util import variables
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import calendar
import datetime
from imperial.core.util.ManejaFechas import ManejaFechas

FECHA_RF, PROM_VENTA_RF, CANT_PERS_RF, CAJA_ABAJO_RF, PROM_PERS_CAJA_ABAJO = range(5)

lstHeader = [PROM_VENTA_RF, CANT_PERS_RF, CAJA_ABAJO_RF, FECHA_RF, PROM_PERS_CAJA_ABAJO]

lstTitHeader = [u'FECHA', u'PROM VENTA Z', u'CANT PERS Z', u'CAJA ABAJO', u'CANT PERS ABAJO']

class TableModelResumenFiscal(_qc.QAbstractTableModel):
    u""""""
    
    def __init__(self, modelo=None):
        super(TableModelResumenFiscal, self).__init__()
        
        self.modelo = modelo
        self.datos = []
        self.dao = None
        self.dicDatos = {}
        self.getDatos(datetime.date.today())
        self.tableView = None
        self.datosNuevos = True #Controla si los datos on para guardar o actualizar.
        self.dataChanged[_qc.QModelIndex, _qc.QModelIndex].connect(self.cambiarTotales)
        self.dias_mes = -1
        
    @_qc.pyqtSlot("QModelIndex, QModelIndex")        
    def cambiarTotales(self, index=None, index2=None):
        #dato = self.datos[index.row()]
        pass
        
    def getDatos(self, fecha):
        resumenes = self.buscarDatos(fecha) #Fecha
        
        if len(resumenes) > 0:
            self.datos = resumenes
            self.datosNuevos = False
        else:
            self.crearResumenesEnBlanco(fecha)
            self.datosNuevos = True
        
        self.reset()
            
    
    def crearResumenesEnBlanco(self, fecha):
        #hoy = datetime.date.today()
        inicio_mes = fecha.replace(day=1)
        self.datos = []
        
        #uCompleta los diás de resúmenes según el mes.
        dia_semana, self.dias_mes = calendar.monthrange(fecha.year, fecha.month)
        
        for i in range(self.dias_mes):
            resumen = ResumenFiscal.data2Object([
                        0.0, 0, 0.0, 
                        inicio_mes.replace(day=inicio_mes.day + i)])
            self.datos.append(resumen)
    
    
    def guardarDatos(self, lstDatos):
        self.modelo.dao.cerrarSesion = True
        if self.datosNuevos:
            msg = DataModel.LST_MSG[DataModel.MSG_SAVE]
            
            retorno = self.modelo.dao.insertMasivo(self.datos)
            
            if retorno <= 0:
                msg = DataModel.LST_MSG[DataModel.MSG_NOT_SAVE]
            else:
                self.datosNuevos = False
            
            return (retorno > 0, msg)
        return self.actualizarDatos(lstDatos)
    
    def actualizarDatos(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_EDIT]
        
        retorno = self.modelo.dao.updateMasivo(
                    self.datos)
        
        if retorno <= 0:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_EDIT]
        
        return (retorno > 0, msg)
    
    def buscarDatos(self, hoy):
        inicio_mes = hoy.replace(day=1)
        cierre_mes = hoy.replace(day=calendar.monthrange(hoy.year, hoy.month)[1])
        
        resumenes = self.modelo.dao.getResumenFiscalByFecha({
                'FECHA_INICIO': inicio_mes, 'FECHA_CIERRE': cierre_mes})
        
        return list(resumenes)
    
    def buscarDatosResumenes(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_LIST]
        
        self.getDatos(lstDatos[0])
        if self.datosNuevos:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
        
        return (self.datosNuevos == False, msg)
    
    def datos2Array(self):
        from imperial.model.modeltable import tableModelResumenFiscal
        lstDatos = []
        lst_resaltados = []
        for dato in self.datos:
            lstDatos.append([ManejaFechas.date2Str(dato.fecha), dato.prom_venta, dato.cant_pers, 
                             dato.caja_abajo, dato.cant_pers_abajo])
            
        return (tableModelResumenFiscal.lstTitHeader, lstDatos, lst_resaltados)
    
    def datos2ArrayBlank(self):
        from imperial.model.modeltable import tableModelResumenFiscal
        lstDatos = []
        lst_resaltados = []
        for dato in self.datos:
            lstDatos.append([ManejaFechas.date2Str(dato.fecha), None, None, None, None])
            
        return (tableModelResumenFiscal.lstTitHeader, lstDatos, lst_resaltados)
    
    def filaDato(self, row):
        return self.datos[row]

    def clear(self):
        self.datos = []
        self.reset()

    def rowCount(self, index=_qc.QModelIndex()):
        return len(self.datos)

    def columnCount(self, index=_qc.QModelIndex()):
        return 5
    
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
            if column == FECHA_RF:
                return _qc.QDate(dato.fecha).toString('dd-MM-yyyy')
            if column == PROM_VENTA_RF:
                return ((_qc.QString("%L1").\
                                     arg('{:.2f}'.format(dato.prom_venta))))
            if column == CANT_PERS_RF:
                return _qc.QVariant(dato.cant_pers)
            if column == CAJA_ABAJO_RF:
                return _qc.QVariant(dato.caja_abajo)
            if column == PROM_PERS_CAJA_ABAJO:
                dato.cant_pers_abajo = 0
                if dato.prom_venta > 0:
                    dato.cant_pers_abajo = int(dato.caja_abajo/dato.prom_venta)
                    #return _qc.QVariant(dato.cant_pers_abajo)
                return _qc.QVariant(dato.cant_pers_abajo)
                #return _qc.QVariant(dato.)
                #return QVariant(QString("%L1").arg(numero, 5, 10, QChar('0')))
                #return QVariant(QString("%L1").arg(numero))

        elif role == _qc.Qt.TextAlignmentRole:
            if column == PROM_VENTA_RF or column == CANT_PERS_RF or \
                        column == CAJA_ABAJO_RF or column == PROM_PERS_CAJA_ABAJO:
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            if column == FECHA_RF:
                return _qc.QVariant(int(_qc.Qt.AlignHCenter|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        
        elif role == _qc.Qt.TextColorRole and column == PROM_VENTA_RF:
            pass
            #decena = int(str(numero)[-2:] if len(str(numero)) >=2 else str(numero))
            #if decena < 1 or decena > 90:
            #   return _qc.QVariant(_qg.QColor(_qc.Qt.darkRed))
            #else:
            #   return _qc.QVariant(_qg.QColor(_qc.Qt.green))
        elif role == _qc.Qt.BackgroundColorRole:
            if column == FECHA_RF:
                if index.row() % 2 == 0:
                    return _qc.QVariant(_qg.QColor(58, 216, 58))
                return _qc.QVariant(_qg.QColor(155, 216, 155))
            
        elif role == _qc.Qt.FontRole:
            font = _qg.QFont('Helvetica', 11, _qg.QFont.Bold)
            return _qc.QVariant(font)
        
        return _qc.QVariant()
    
    def setData(self, index, value, role=_qc.Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.datos):
            dato = self.datos[index.row()]
            column = index.column()
            if column == CANT_PERS_RF:
                #value, ok = value.toInt()
                #if ok:
                #   dato.cant_pers = value
                dato.cant_pers = value
            elif column == PROM_VENTA_RF:
                dato.prom_venta = value
            elif column == CAJA_ABAJO_RF:
                dato.caja_abajo = value
            elif column == PROM_PERS_CAJA_ABAJO:
                dato.cant_pers_abajo = value
            self.emit(_qc.SIGNAL("dataChanged(QModelIndex, QModelIndex)"),
                      index, index)
            return True
        return False
    
    def headerData(self, section, orientation, role=_qc.Qt.DisplayRole):
        if role == _qc.Qt.TextAlignmentRole:
            if orientation == _qc.Qt.Horizontal:
                return _qc.QVariant(int(_qc.Qt.AlignHCenter|_qc.Qt.AlignVCenter))
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
        if column == PROM_VENTA_RF or column == CANT_PERS_RF or column == CAJA_ABAJO_RF:
            return _qc.Qt.ItemFlags(_qc.QAbstractTableModel.flags(self, index) |
                            _qc.Qt.ItemIsEditable)
        else:
            return _qc.Qt.ItemIsEnabled
        
class ResumenFiscalDelegate(_qg.QItemDelegate):
    def __init__(self, parent=None):
        super(ResumenFiscalDelegate, self).__init__(parent)
        
    def sizeHint(self, option, index):
        fm = option.fontMetrics

        text = index.model().data(index).toString()
        document = _qg.QTextDocument()
        document.setDefaultFont(option.font)
        document.setHtml(text)
        
        if index.column() == PROM_VENTA_RF:
            return _qc.QSize(document.idealWidth() + 60, fm.height())
        if index.column() == CANT_PERS_RF:
            return _qc.QSize(document.idealWidth() + 60, fm.height())
        if index.column() == CAJA_ABAJO_RF:
            return _qc.QSize(document.idealWidth() + 60, fm.height())
        if index.column() == PROM_PERS_CAJA_ABAJO:
            return _qc.QSize(document.idealWidth() + 60, fm.height())

    def createEditor(self, parent, option, index):
        if index.column() == PROM_VENTA_RF:
            dSpin = _qg.QDoubleSpinBox(parent)
            dSpin.setLocale(_qc.QLocale('QLatin1Char'))
            dSpin.setRange(0.00, 999999.99)
            dSpin.setSingleStep(1)
            #dSpin.setPrefix("$ ")
            dSpin.setValue(0.00)
            dSpin.setAlignment(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter)
            return dSpin
        elif index.column() == CAJA_ABAJO_RF:
            dSpin = _qg.QDoubleSpinBox(parent)
            dSpin.setLocale(_qc.QLocale('QLatin1Char'))
            dSpin.setRange(0.00, 999999.99)
            dSpin.setSingleStep(1)
            #dSpin.setPrefix("$ ")
            dSpin.setValue(0.00)
            dSpin.setAlignment(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter)
            return dSpin
        elif index.column() == CANT_PERS_RF:
            iSpin = _qg.QSpinBox(parent)
            iSpin.setRange(0, 999999)
            iSpin.setSingleStep(1)
            iSpin.setValue(0)
            iSpin.setAlignment(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter)
            return iSpin
        else:
            return _qg.QItemDelegate.createEditor(self, parent, option,
                    index)
            
    def setEditorData(self, editor, index):
        text = index.model().data(index, _qc.Qt.DisplayRole).toString()
        if index.column() == CANT_PERS_RF:
            value = text.toInt()[0]
            editor.setValue(value)
            #model.setData(index, _qc.QVariant(editor.text()))
        elif index.column() == PROM_VENTA_RF:
            value = text#.toString()[0]
            editor.setValue(float(value))
        elif index.column() == CAJA_ABAJO_RF:
            value = text#.toString()[0]
            editor.setValue(float(value))
        else:
            _qg.QItemDelegate.setEditorData(self, editor, index)
            
    def setModelData(self, editor, model, index):
        if index.column() == CANT_PERS_RF:
            #model.setData(index, QVariant(editor.value()))
            model.setData(index, editor.value())
        elif index.column() == PROM_VENTA_RF:
            model.setData(index, editor.value())
        elif index.column() == CAJA_ABAJO_RF:
            model.setData(index, editor.value())
        else:
            _qg.QItemDelegate.setModelData(self, editor, model, index)

    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (_qg.QDoubleSpinBox)):
            self.emit(_qc.SIGNAL("commitData(QWidget*)"), editor)
            self.emit(_qc.SIGNAL("closeEditor(QWidget*)"), editor)