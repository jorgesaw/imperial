#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 03/04/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.MsgBox import MsgBox
from imperial.core.model.datamodel.dataModel import DataModel
from imperial.dao.DAOMovVentaProd import DAOMovVentaProd
from imperial.dao.DAOSaldos import DAOSaldos
from imperial.dao.DAOVenta import DAOVenta
from imperial.model.models import Vendedor, Egreso, Venta, MovEgreso, \
    SaldoDiario, VendedorInterno, VendedorExterno
from imperial.util import variables
from imperial.vista.gui.dlg.NewProveedorDlg import NewProveedorDlg
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime

NOMBRE, SALDO_PARCIAL, SUBTOTAL, TOTAL = range(4)

lstHeader = [NOMBRE, SALDO_PARCIAL, SUBTOTAL, TOTAL]

lstTitHeader = ['NOMBRE', 'SALDO PARCIAL', 'SUBTOTAL', 'TOTAL']

class TableModelSaldoDiario(_qc.QAbstractTableModel):
    u""""""
    
    def __init__(self, modelo=None):
        super(TableModelSaldoDiario, self).__init__()
        
        self.modelo = modelo
        self.datos = []
        self.dao = None
        self.dicDatos = {}
        #self.getDatos(datetime.date.today())
        self.tableView = None
        
        self.saldo_diario = None
        self.datosNuevos = True #Controla si los datos on para guardar o actualizar.
        self.totVenta = Venta(0.0, Vendedor('TOTAL VENTA'), datetime.date.today())
        self.saldoNeto = Venta(0.0, Vendedor('VENTA NETA'), datetime.date.today)
        self.totEgreso = MovEgreso(0.0, Egreso('TOTAL EGRESO'), datetime.date.today)
        
        self.lst_mov_ventas_prod = []
        
        self.lstSaldos = []
        
        self.dataChanged[_qc.QModelIndex, _qc.QModelIndex].connect(self.cambiarTotales)
        
    @_qc.pyqtSlot("QModelIndex, QModelIndex")        
    def cambiarTotales(self, index=None, index2=None):
        #totVentas = 0
        #sizeVend = len(self.vendedores)
        
        #for i in range(sizeVend):
        #   totVentas += self.datos[i][1]
        
        #self.datos[sizeVend][1] = totVentas
        
        #totEgresos = 0
        #sizeEgresos = len(self.egresos)
        
        #for i in range(sizeEgresos):
        #    totEgresos += self.datos[sizeVend + i + 1][1]
        
        #self.datos[sizeVend + sizeEgresos + 1][1] = totEgresos
        #self.datos[sizeVend + sizeEgresos + 1 + 1][1] = totVentas - totEgresos 
        
        #self.datos[len(self.saldo_diario.colVentas)].valor = self.saldo_diario.saldoVentas()
        #self.datos[len(self.saldo_diario.colVentas) + len(self.saldo_diario.colMovEgresos) + 1].valor = self.saldo_diario.saldoEgresos()
        
        #self.datos[len(self.saldo_diario.colVentas) + \
        #          len(self.saldo_diario.colMovEgresos) + 2 ].valor = \
        #          self.saldo_diario.saldo()
        
        #self.reset()
        #if index:
        #   next_index =  self.tableView.model().index(index.row() + 1, index.column())
        #  self.tableView.setCurrentIndex(next_index)#self.tableView.edit(next_index)
        #_qg.QMessageBox.about(None, "Devoluciones", '')
        #r =_qg.QMessageBox(None)
        #r.setText('Hola')
        #r.show()
        #r.setWindowModality(_qc.Qt.NonModal)
        
        #_qc.QCoreApplication.processEvents()
        #_qg.QMessageBox.about(None, "Devoluciones", '')
        
        #r.exec_()
        pass
        
    
    def guardarDatos(self, lstDatos):
        if self.datosNuevos:
            msg = DataModel.LST_MSG[DataModel.MSG_SAVE]
        
            #retorno = self.modelo.dao.insertMasivo(
            #       self.makeObjetosSaldos(lstDatos[0]))
            retorno = self.modelo.dao.insert(self.saldo_diario)
        
            if retorno <= 0:
                msg = DataModel.LST_MSG[DataModel.MSG_NOT_SAVE]
        
            return (retorno > 0, msg)
        return self.actualizarDatos(lstDatos)
    
    
    def cerrarSesionDAO(self):
        self.modelo.dao.cerrarSesion()
        
    def makeObjetosSaldos(self, fecha):
        sizeVend = len(self.vendedores)
        lstVentas = [] 
        
        for i in range(sizeVend):
            lstVentas.append(Venta(self.datos[i][1], #Valor
                                       self.vendedores[i], #
                                       fecha
                                       ))
            
        lstEgresos = []
        sizeEgresos = len(self.egresos)
        
        for i in range(sizeEgresos):
            lstEgresos.append(MovEgreso(self.datos[sizeVend + i + 1][1], 
                                     self.egresos[i], 
                                     fecha
                                     ))
            
        return lstVentas + lstEgresos
        
        
    def filaDato(self, row):
        return self.datos[row]

    def clear(self):
        self.datos = []
        self.reset()

    def rowCount(self, index=_qc.QModelIndex()):
        return len(self.datos)

    def columnCount(self, index=_qc.QModelIndex()):
        return 4
    
    def limpiarValores(self):
        for lstValores in self.datos:
            lstValores[1] = 0.0
        self.reset()
    
    def getDatos(self, fecha):
        #print('GET_DATOS')
        self.vendedores = self.modelo.dao.getAll(VendedorInterno)
        
        self.vendedoresExternos = self.modelo.dao.getAll(VendedorExterno)
        #vendedores.append(Venta('Total Ventas'))
        
        self.egresos = self.modelo.dao.getAll(Egreso)
        #egresos.append(Egreso('Total Egresos'))
        
        #self.lst_mov_ventas_prod = []
        
        #dao = DAOMovVentaProd(False)
        #self.lst_mov_ventas_prod = dao.movVentaProdByFecha({'FECHA_MOV': fecha})
                
        #self.lst_mov_ventas_prod = dao.ventaProdByFecha({'FECHA_MOV': fecha})
        
        #for mov_venta in self.lst_mov_ventas_prod:
            #uAtributo creado Ad Hoc para mantener compatibilidad en el evento data()
            
        #   mov_venta.valor = mov_venta.calcularSaldo()
            
        self.datos = []
        #for vend in self.vendedores:            
            #self.datos.append(Venta(0.0, vend))
        #    self.datos.append([vend.nombre, 0.0])
        #self.datos.append(['Total ventas', 0])
            
        #for egreso in self.egresos:
        #   self.datos.append([egreso.nombre, 0.0])
        #self.datos.append(['Total egresos', 0])

        #self.datos.append(['Venta Neta', 0])
        self.lstVentas = []; self.lstEgresos = []
        
        self.lstVentasNuevas = []
        self.lstVentasActualizar = []
        dao = DAOVenta(False)
        
        for vend in self.vendedoresExternos:
            venta = dao.ventaByFechaVendedor({'VENDEDOR': vend, 
                                'FECHA_MOV': fecha})
            if venta:
                self.lstVentasActualizar.append(venta)
            else:
                venta = Venta(0.0, vend, fecha)
                self.lstVentasNuevas.append(venta)
            
            vend.venta = venta
            
            self.lstVentas.append(venta)
        
        for vend in self.vendedores:
            self.lstVentas.append(Venta(0.0, vend, fecha))
        for egreso in self.egresos:
            self.lstEgresos.append(MovEgreso(0.0, egreso, fecha))
            
        self.saldo_diario = SaldoDiario(fecha)
        self.saldo_diario.colVentas = self.lstVentas
        
        self.saldo_diario.colMovEgresos = self.lstEgresos
        
        #self.datos += self.lst_mov_ventas_prod
        self.datos += self.lstVentas
        
        saldo_parcial = self.saldo_diario.saldoParcial()
        self.totVenta = Venta(saldo_parcial, Vendedor('TOTAL VENTA'), fecha)
        self.saldoNeto = Venta(saldo_parcial, Vendedor('VENTA NETA'), fecha)
        self.totEgreso = MovEgreso(0.0, Egreso('TOTAL EGRESO'), fecha)
        
        #self.totVenta.valor = 0.0
        self.datos.append(self.totVenta)
        
        self.datos += self.lstEgresos
        
        #self.totEgreso.valor = 0.0
        #self.saldoNeto.valor = 0.0
        self.datos.append(self.totEgreso)
        self.datos.append(self.saldoNeto)
        
        #setear longitudes de listas
        self.cant_ventas = len(self.lstVentas)
        self.cant_egresos = len(self.lstEgresos)
        
        self.reset()
        
    def actualizarDatos(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_EDIT]
        
        retorno = self.modelo.dao.update(self.saldo_diario)
        
        if retorno <= 0:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_EDIT]
        
        return (retorno > 0, msg)
    
        sizeVend = len(self.vendedores)
        
        for i in range(sizeVend):
            venta = self.vendedores[i]
            venta.fecha = lstDatos[0]
            venta.valor = self.datos[i][1]
        
        sizeEgresos = len(self.egresos)

        for i in range(sizeEgresos):
            mov_egresos = self.egresos[i]
            mov_egresos.fecha = lstDatos[0]
            mov_egresos.valor = self.datos[sizeVend + i + 1][1]
            
        msg = DataModel.LST_MSG[DataModel.MSG_EDIT]
        
        retorno = self.modelo.dao.updateMasivo(
                    self.vendedores + self.egresos)
        
        if retorno <= 0:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_EDIT]
        
        return (retorno > 0, msg)
                
    def buscarDatos(self, lstDatos):
        #print('BUSCAR_DATOS')
        self.datos = []
        #daoSaldos = DAOSaldos(False)
        msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
        ok = False
        
        self.saldo_diario = self.modelo.dao.getSaldoByFecha(lstDatos[0])

        #self.vendedores = daoSaldos.getSaldosByFecha([Venta, lstDatos[0]])
        #self.lstSaldos.append(ventas)
        #self.egresos = daoSaldos.getSaldosByFecha([MovEgreso, lstDatos[0]])
        #self.lstSaldos.append(egresos)
        
        #if len(self.vendedores) > 0 and len(self.egresos) > 0:
        if self.saldo_diario:
            msg = DataModel.LST_MSG[DataModel.MSG_LIST]
            ok = True
            self.datosNuevos = False
            
            #for venta in self.vendedores:            
                #self.datos.append(Venta(0.0, vend))
                #   self.datos.append([venta.vendedor.nombre, venta.valor])
            #self.datos.append(['Total ventas', 0])
            self.vendedores = list(self.saldo_diario.colVentas)
            #for i in range(len(self.vendedores)):
            #   print('i: {}, VEND: {}'.format(i, self.vendedores[i]))
            #self.lst_mov_ventas_prod = list(self.saldo_diario.colMovVentasProd)
            
            #for mov_venta in self.lst_mov_ventas_prod:
            #uAtributo creado Ad Hoc para mantener compatibilidad en el evento data()
            #   mov_venta.valor = mov_venta.calcularSaldo()
            
            #self.saldo_diario.saldoMovVentasProd()
            
            #self.datos = self.lst_mov_ventas_prod + self.vendedores
            self.datos += self.vendedores
            
            saldo_parcial = self.saldo_diario.saldoParcial()
            #print('EL SALDO en SALDO ES:', saldo_parcial)
            self.totVenta = Venta(saldo_parcial, Vendedor('TOTAL VENTA'), lstDatos[0])
            self.saldo_diario.saldoVentasSubtotal()
            self.totVenta.subtotal = self.saldo_diario.saldoTotalVentas()
            
            self.datos.append(self.totVenta)
            
            #for mov_egreso in self.egresos:
            #   self.datos.append([mov_egreso.egreso.nombre, mov_egreso.valor])
            #self.datos.append(['Total egresos', 0])
            self.lstEgresos = list(self.saldo_diario.colMovEgresos)
            self.datos += self.lstEgresos
            
            self.totEgreso.saldo_parcial = self.saldo_diario.saldoEgresos()
            
            self.datos.append(self.totEgreso)
    
            self.saldoNeto.saldo_parcial = self.saldo_diario.saldo()
            self.datos.append(self.saldoNeto)
            
            self.cambiarTotales(None, None)
            
            #setear longitudes de listas
            self.cant_ventas = len(self.vendedores) #+ len(self.lst_mov_ventas_prod)
            self.cant_egresos = len(self.lstEgresos)
        
        else:
            self.datosNuevos = True
            self.getDatos(lstDatos[0])
        
        return (ok, msg)
    
    def datos2Array(self):
        lstDatos = []
        lst_resaltados = [self.cant_ventas, self.cant_ventas + self.cant_egresos + 1, 
                          self.cant_ventas + self.cant_egresos + 2]
        
        #self.saldo_diario.saldoVentasSubtotal()
        self.saldo_diario.saldoTotalVentas()
        self.saldo_diario.saldoEgresos()
        self.saldo_diario.saldo()
        
        for dato in self.datos:
            print('TOTAL:', dato.calcularTotal())
            lstDatos.append([dato.__str__()[0:36], dato.calcularTotal()])
            
        return (variables.LST_HEADER_REPORTE_SALDO, lstDatos, lst_resaltados)
    
    def datos2ArrayBlank(self):
        lstDatos = []
        lst_resaltados = [self.cant_ventas, self.cant_ventas + self.cant_egresos + 1, 
                          self.cant_ventas + self.cant_egresos + 2]
        for dato in self.datos:
            lstDatos.append([dato.__str__(), None])
            
        return (variables.LST_HEADER_REPORTE_SALDO, lstDatos, lst_resaltados)
    
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
        #lstDato = self.datos[index.row()]
        dato = self.datos[index.row()]
        column = index.column()
        row = index.row()
        if role == _qc.Qt.DisplayRole:
            if column == NOMBRE:
                #return _qc.QVariant(lstDato[0])
                return _qc.QVariant(dato.__str__())
            if column == SALDO_PARCIAL:
                #return _qc.QVariant(lstDato[1])
                if row == self.cant_ventas:
                    #self.saldo_diario.saldoParcial()
                    #dato.saldo_parcial = self.saldo_diario.saldoTotalVentas()
                    dato.saldo_parcial = self.saldo_diario.saldoParcial()
                    #print('SALDOOOO_PARRRRCIAL:', dato.saldo_parcial)
                    dato.subtotal = self.saldo_diario.saldoVentasSubtotal()
                    #print('SALDOOOO_SUBBBTTTOOOOTAL:', dato.subtotal)
                    #return _qc.QVariant(dato.saldo_parcial)
                    return _qc.QVariant('')
                if row == self.cant_ventas + self.cant_egresos + 1:
                    dato.saldo_parcial = self.saldo_diario.saldoEgresos()
                    #return _qc.QVariant(dato.saldo_parcial)
                    return _qc.QVariant('')
                if row == self.cant_ventas + \
                        self.cant_egresos + 2 :
                    dato.saldo_parcial = self.saldo_diario.saldo()
                    #return _qc.QVariant(dato.saldo_parcial)
                    return _qc.QVariant('')
                return _qc.QVariant(dato.saldo_parcial)
                #return QVariant(QString("%L1").arg(numero, 5, 10, QChar('0')))
                #return QVariant(QString("%L1").arg(numero))
            if column == SUBTOTAL:
                if row in (self.cant_ventas, self.cant_ventas + self.cant_egresos + 1, 
                           self.cant_ventas + self.cant_egresos + 2):
                    dato.calcularSubtotal()
                    return _qc.QVariant('')
                return _qc.QVariant((_qc.QString("%L1").\
                                     arg('{:.2f}'.format(dato.calcularSubtotal()))))
            if column == TOTAL:
                if row == self.cant_ventas:
                    dato.calcularTotal()
                    #print('TOTALLLLLL:', dato.calcularTotal())
                return _qc.QVariant((_qc.QString("%L1").\
                                     arg('{:.2f}'.format(dato.calcularTotal()))))
        elif role == _qc.Qt.TextAlignmentRole:
            if column in(SALDO_PARCIAL, SUBTOTAL, TOTAL):
                return _qc.QVariant(int(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter))
            return _qc.QVariant(int(_qc.Qt.AlignLeft|_qc.Qt.AlignVCenter))
        elif role == _qc.Qt.TextColorRole and column == SALDO_PARCIAL:
            pass
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
            #print('ROW:{}, CANT_VENTAS:{}'.format(row, self.cant_ventas))
            if row == self.cant_ventas:
                return _qc.QVariant(_qg.QColor(58, 216, 58))
            if row == self.cant_ventas + self.cant_egresos + 1:
                return _qc.QVariant(_qg.QColor(216, 66, 58))
            if row == self.cant_ventas + self.cant_egresos + 2:
                #if lstDato[1] >= 0:
                if dato.saldo_parcial >= 0:
                    return _qc.QVariant(_qg.QColor(58, 216, 58))
                return _qc.QVariant(_qg.QColor(216, 66, 58))
        return _qc.QVariant()
    
    def setData(self, index, value, role=_qc.Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.datos):
            #lstDatos = self.datos[index.row()]
            dato = self.datos[index.row()]
            column = index.column()
            if column == SALDO_PARCIAL:
                #value, ok = value.toInt()
                #if ok:
                    #self.datos[index.row()] = value
                #lstDatos[1] = value
                dato.setSaldoParcial(value)
            self.emit(_qc.SIGNAL("dataChanged(QModelIndex, QModelIndex)"),
                      index, index)
            return True
        return False
    
    def headerData(self, section, orientation, role):
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
        if column == SALDO_PARCIAL and index.row() not in (self.cant_ventas, 
                                self.cant_ventas + self.cant_egresos + 1, 
                                self.cant_ventas + self.cant_egresos + 2):
            return _qc.Qt.ItemFlags(_qc.QAbstractTableModel.flags(self, index) |
                            _qc.Qt.ItemIsEditable)
        else:
            return _qc.Qt.ItemIsEnabled | _qc.Qt.ItemIsSelectable
 
class SaldoDiarioDelegate(_qg.QItemDelegate):
    def __init__(self, parent=None):
        super(SaldoDiarioDelegate, self).__init__(parent)
        
    def paint(self, painter, option, index):
        color = _qg.QColor(103, 103, 103)
        option.palette.setColor(_qg.QPalette.Highlight, color)
        
        _qg.QItemDelegate.paint(self, painter, option, index)
        
    def sizeHint(self, option, index):
        fm = option.fontMetrics

        text = index.model().data(index).toString()
        document = _qg.QTextDocument()
        document.setDefaultFont(option.font)
        document.setHtml(text)
        if index.column() == NOMBRE:
            return _qc.QSize(450, fm.height())
        if index.column() == SALDO_PARCIAL:
            return _qc.QSize(60, fm.height())
        if index.column() == SUBTOTAL:
            return _qc.QSize(60, fm.height())
        if index.column() == TOTAL:
            return _qc.QSize(60, fm.height())

    def createEditor(self, parent, option, index):
        if index.column() == SALDO_PARCIAL:
            dSpin = _qg.QDoubleSpinBox(parent)
            dSpin.setLocale(_qc.QLocale('QLatin1Char'))
            dSpin.setRange(0.00, 999999.99)
            dSpin.setSingleStep(1)
            font = _qg.QFont('Helvetica', 11, _qg.QFont.Bold)
            dSpin.setFont(font)
            #dSpin.setPrefix("$ ")
            dSpin.setValue(0.00)
            dSpin.setAlignment(_qc.Qt.AlignRight|_qc.Qt.AlignVCenter)
            return dSpin
        else:
            return _qg.QItemDelegate.createEditor(self, parent, option,
                    index)
            
    def setEditorData(self, editor, index):
        text = index.model().data(index, _qc.Qt.DisplayRole).toString()
        if index.column() == SALDO_PARCIAL:
            value = text.toInt()[0]
            editor.setValue(value)
            #model.setData(index, _qc.QVariant(editor.text()))
        else:
            _qg.QItemDelegate.setEditorData(self, editor, index)
            
    def setModelData(self, editor, model, index):
        if index.column() == SALDO_PARCIAL:
            #model.setData(index, QVariant(editor.value()))
            model.setData(index, editor.value())
        else:
            _qg.QItemDelegate.setModelData(self, editor, model, index)

    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (_qg.QDoubleSpinBox)):
            self.emit(_qc.SIGNAL("commitData(QWidget*)"), editor)
            self.emit(_qc.SIGNAL("closeEditor(QWidget*)"), editor)