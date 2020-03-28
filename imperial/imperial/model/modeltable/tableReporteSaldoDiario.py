#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 31/05/2015

@author: jorgesaw
'''

from imperial.core.model.modelotable.modeloTabla import ModeloTabla
from imperial.core.util.ManejaFechas import ManejaFechas
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg

class TableReporteSaldoDiario(ModeloTabla):
    
    def __init__(self, modelo, modeloDatosTabla, parent=None):
        super(TableReporteSaldoDiario, self).__init__(modelo, modeloDatosTabla, parent=None)
        
        self.modeloDatosTabla.tabla_reporte = self
        
    def buscarDatosSaldos(self, lstDatos):
        fecha_busqueda = lstDatos[0]
        
        self.lstSaldos, msg = self.modelo.saldosEntreFechas({'INICIO': fecha_busqueda, 
                                        'CIERRE': ManejaFechas.sumarFechasDias(
                                                        fecha_busqueda, 6)})
        
        if not self.lstSaldos:
            print('SIN SALDOS', self.lstSaldos, msg)
            self.clear()
            return (self.lstSaldos == True, msg)
        
        self.agruparDatosVentaEgresos()
        self.datos = []
        
        print('LEN_SALDOS:', len(self.lstSaldos))
        
        self.lstNombres = [nombre.__str__() for nombre in self.lstSaldos[0].lstDatosAgrupados]
        
        #print('NOMBRES:', lstNombres)
        
        #VENTAS
        self.cant_ventas = len(self.lstSaldos[0].colTotalVentas)
        
        print('LEN_SALDOS:', len(self.lstSaldos))
        
        #Crear totales de mov_venta_prod
        for saldo in self.lstSaldos:
            print('LEN_SALDOS_FOR_TOT:', len(self.lstSaldos))
            for mov_venta in saldo.colMovVentasProd:
                #uAtributo creado Ad Hoc para mantener compatibilidad en el evento data()
                mov_venta.valor = mov_venta.calcularSaldo()
            saldo.saldoVentas()
            saldo.saldoMovVentasProd()
        
        for i in xrange(self.cant_ventas):
            rowDatos = []
            rowDatos.append(self.lstSaldos[0].colTotalVentas[i].__str__())
            print(self.lstSaldos[0].colTotalVentas[i].__str__())
            #print('LEN_SALDOS_XRANGE:', len(self.lstSaldos))
            
            for saldo in self.lstSaldos:
                #print('LEN_SALDOS_EN_SALDOS:', len(self.lstSaldos))
                #print('SALDOOO:', saldo)
                if saldo:
                    rowDatos.append(saldo.colTotalVentas[i].valor)
                else:
                    rowDatos.append('')
                #print('------VALOR:', saldo.colTotalVentas[i].valor)
            rowDatos.append(self.totFila(rowDatos[1:]))
            
            self.datos.append(rowDatos)
        
        rowDatos = ['TOTAL VENTAS',]
        rowDatos += [saldo.saldoTotalVentas() for saldo in self.lstSaldos]
        rowDatos.append(self.totFila(rowDatos[1:]))
        
        self.datos.append(rowDatos)
        
        #EGRESOS
        self.cant_egresos = len(self.lstSaldos[0].colMovEgresos)
        
        for i in xrange(self.cant_egresos):
            rowDatos = []
            rowDatos.append(self.lstSaldos[0].colMovEgresos[i].__str__())
            
            for saldo in self.lstSaldos:
                if saldo:
                    rowDatos.append(saldo.colMovEgresos[i].valor)
                else:
                    rowDatos.append('')
                
            rowDatos.append(self.totFila(rowDatos[1:]))
            
            self.datos.append(rowDatos)
        
        rowDatos = ['TOTAL EGRESOS',]
        rowDatos += [saldo.saldoEgresos() for saldo in self.lstSaldos]
        rowDatos.append(self.totFila(rowDatos[1:]))
        self.datos.append(rowDatos)
        
        rowDatos = ['TOTAL NETO',]
        rowDatos += [saldo.saldo() for saldo in self.lstSaldos]
        rowDatos.append(self.totFila(rowDatos[1:]))
        
        self.datos.append(rowDatos)
        
        ###########
        #self.modeloDatosTabla.datos = self.datos
        
        #print self.datos
        
        print(self.datos)
        self.reset()    
                
        
    def cambiarNombresHeader(self):
        #u Método que cambia los nombres a las columnas d ela tabla.
        pass    
    
    def agruparDatosVentaEgresos(self):
        for saldo_diario in self.lstSaldos:
            saldo_diario.colTotalVentas = saldo_diario.colMovVentasProd + saldo_diario.colVentas
            saldo_diario.lstDatosAgrupados = saldo_diario.colTotalVentas + \
                                saldo_diario.colMovEgresos
                                
    def totFila(self, lstValores):
        tot = 0.0
        for valor in lstValores:
            tot += valor
        return tot
    
    def totColumnas(self):
        lstTotales = []
        fin = len(self.lstNombres) 
        print ()
        for col in range(1, 9):
            tot = 0.0
            for i in range(0, len(self.datos)):
                print(i, col)
                tot += self.datos[i][col]
            lstTotales.append(tot)
            
        return lstTotales