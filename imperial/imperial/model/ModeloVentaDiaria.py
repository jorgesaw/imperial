#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 24/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.model.datamodel.dataModel import DataModel
from imperial.dao.DAOProducto import DAOProducto
from imperial.model.models import VentaProd, Category, Venta
from imperial.model.modeltable.modeldatatable.tmVentaDiariaVariedades import \
    TMVentaDiariaVariedades
from imperial.util import variables
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime

class ModeloVentaDiaria(object):
    u"""Modelo que controla los dos modelos de la venta diaria."""
    
    def __init__(self, modelo=None):
        self.modelo = modelo
        
        self.modeloVarios = TMVentaDiariaVariedades(modelo)
        self.modeloVarios.modeloPadre = self
        self.modeloVarios.categoria = Category.VARIOS
        
        self.modeloPan = TMVentaDiariaVariedades(modelo)
        self.modeloPan.modeloPadre = self
        self.modeloPan.categoria = Category.PAN
        
        self.lstModelosHijos = (self.modeloVarios, self.modeloPan)
        
        self.ventana = None
        self.datosNuevos = True
        
        #self.mov_venta_prod = None
        self.venta = None
    
    def buscarDatos(self, lstDatos):
        fecha = lstDatos[0]
        vendedor = lstDatos[1]
        mapParam = {'FECHA_MOV': fecha, 'VENDEDOR': vendedor}
        self.buscarDatosByFechaVendedor(mapParam)
        #self.datos = []
        
        self.modeloVarios.datos = []
        self.modeloPan.datos = []
        
        if self.venta:
            #Filtrar datos por categoría.
            #listasDatos = self.datosPorCategoria(
            #                       self.mov_venta_prod.colVentasProd)
            #listasDatos = self.datosPorCategoria(self.venta.colVentasProd)
            #listasDatos = self.venta.colVentasProd
            #listasDatos = self.datosPorCategoria(self.modelo.dao.ventaProdByVenta(
            #               {'ID_VENTA': self.venta.id}))
            #Le paso los datos a cada modelo hijo.
            #for ventaProd in listasDatos:
             #   ventaProd.setPrecioUnitario(fecha)
              #  ventaProd.totVentas()
               # ventaProd.cantNeta()
                #ventaProd.calcular()
            #print('::::', len(self.venta.colVentasProd))
            #for ventaProd in self.venta.colVentasProd:
            #   print(':', ventaProd)
            listasDatos = self.datosPorCategoria(self.venta.colVentasProd, fecha)
            
            if len(listasDatos[0]) == 0: #Si la venta fué creada en la vista Saldos y no hay productos.
                self.generarListaProductos(fecha)
            else:
                #print('ACA')
                for modeloHijo, lstDatos in zip(self.lstModelosHijos, listasDatos):
                    modeloHijo.datos = lstDatos
                    #modeloHijo.actualizarTotalDatos(fecha)
                    self.avisarCambioDatos(modeloHijo.categoria)
            self.datosNuevos = False
        else:
            self.crearMovVentaEnBlanco(fecha, vendedor)
            self.avisarCambioDatos(Category.VARIOS)
            self.avisarCambioDatos(Category.PAN)
            self.datosNuevos = True
        
        self.reset()
        
    def cerrarSesionDAO(self):
        self.modelo.dao.cerrarSesion()
        
    def showVentana(self, msg):
        self.ventana.showVentana(msg)
    
    def buscarDatosByFecha(self, fecha):
        #self.mov_venta_prod = self.modelo.dao.movVentaProdByFechaVende({
        #       'FECHA_MOV': fecha})
        self.venta = self.modelo.dao.ventaByFecha({
                'FECHA_MOV': fecha})
        
    def datos2Array(self):
        lstDatos = []

        for dato in self.modeloVarios.datos:
            if dato.tot_venta > 0:
                lstDato = [dato.producto.name[0:36],]
                
                for i in range(VentaProd.CANT_CARGAS):
                    lstDato.append(dato.colCargaProd[i].cant)
                
                lstDato.append(dato.tot_venta)
                lstDato.append(dato.devoluciones)
                lstDato.append(dato.cant_neta)
                lstDato.append(dato.producto.precio)
                lstDato.append(dato.costo)
                
                lstDatos.append(lstDato)
        lstDatos.append(['TOTAL VENTA VARIOS', None, None, None, 
                               None, None, None, None, None, None, 
                               None, self.modeloVarios.total_ventas])
        
        lst_resaltados = [len(lstDatos) - 1,]

        for dato in self.modeloPan.datos:
            if dato.costo > 0:
                lstDato = [dato.producto.name[0:36],]
                
                for i in range(VentaProd.CANT_CARGAS):
                    lstDato.append(dato.colCargaProd[i].cant)
                
                lstDato.append(dato.tot_venta)
                lstDato.append(dato.devoluciones)
                lstDato.append(dato.cant_neta)
                lstDato.append(dato.producto.precio)
                lstDato.append(dato.costo)
                
                lstDatos.append(lstDato)
        lstDatos.append(['TOTAL VENTA PAN', None, None, None, 
                               None, None, None, None, None, None, 
                               None, self.modeloPan.total_ventas])
        
        
        
        lstDatos.append(['TOTAL VENTAS', None, None, None, 
                               None, None, None, None, None, None, 
                               None, 
                               self.modeloPan.total_ventas + self.modeloVarios.total_ventas])
        lst_resaltados.append(len(lstDatos) - 2)
        lst_resaltados.append(len(lstDatos)- 1)
        

            
        return (variables.LST_HEADER_VENTA_DIARIA, lstDatos, lst_resaltados)
    
    def datos2ArrayBlank(self):
        lstDatos = []
        for dato in self.modeloPan.datos:
            lstDatos.append([dato.__str__(), None])
            
        return (variables.LST_HEADER_VENTA_DIARIA, lstDatos)
        
    def buscarDatosByFechaVendedor(self, mapParam):
        #self.mov_venta_prod = self.modelo.dao.\
        #           movVentaProdByFechaVende(mapParam)
        #print('MAP_PARAM:', mapParam['VENDEDOR'].id)               
        self.venta = self.modelo.dao.ventaByFechaVendedorNotLazy(mapParam)
        
    def datosPorCategoria(self, lstDatosVentaProd, fecha):
        u"""Clase que filtra una lista de datos según la categoría."""
        lstVarios = []
        lstPan = []
        
        for ventaProd in lstDatosVentaProd:
            if ventaProd.producto.categoria == Category.VARIOS:
                lstVarios.append(ventaProd)
            else:
                lstPan.append(ventaProd)
            ventaProd.setPrecioUnitario(fecha)
            ventaProd.totVentas()
            ventaProd.cantNeta()
            ventaProd.calcular()
                
        return (lstVarios, lstPan)
    
    def crearMovVentaEnBlanco(self, fecha, vendedor):
        #uAgregar el histórico de precios.
        #self.datos = []
        saldo_parcial = 0.0
        self.venta = Venta(saldo_parcial, vendedor, fecha)
        #self.mov_venta_prod.vendedor = vendedor
        self.generarListaProductos(fecha)

    def generarListaProductos(self, fecha):
        dao = DAOProducto(False)
        
        productosVarios = list(dao.getProductosByCategoria({'categoria': Category.VARIOS, 
                                                            'activo': True}))
        productosPan = list(dao.getProductosByCategoria({'categoria': Category.PAN, 
                                                         'activo': True}))
        
        for producto in productosVarios:
            venta_prod = VentaProd.data2Object([
                        producto, 0, 0 #Producto, cantidad inicial, devoluciones.
                        ])
            #venta_prod.venta = self.venta
            self.modeloVarios.datos.append(venta_prod)
            self.modeloVarios.actualizarPrecioProd(fecha)
            #self.modeloVarios.reset()
            
        for producto in productosPan:
            venta_prod = VentaProd.data2Object([
                        producto, 0, 0 #Producto, cantidad inicial, devoluciones.
                        ])
            #venta_prod.venta = self.venta
            self.modeloPan.datos.append(venta_prod)
            self.modeloPan.actualizarPrecioProd(fecha)
            #self.modeloPan.reset()
            
        #self.mov_venta_prod.colVentasProd = self.modeloVarios.datos + self.modeloPan.datos
        #self.venta.colVentasProd = self.modeloVarios.datos + self.modeloPan.datos
    
    def buscarDatosVentas(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_LIST]
        
        self.buscarDatos(lstDatos)
        
        if self.datosNuevos:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_LIST]
        
        return (self.datosNuevos == False, msg)
    
    def reset(self):
        self.modeloVarios.reset()
        self.modeloPan.reset()
        
    def avisarCambioDatos(self, categoria):
        modeloTabla = self.modeloVarios
        
        if categoria == Category.PAN:
            modeloTabla = self.modeloPan
            
        #total = 0.0
        #for ventaProd in modeloTabla.datos:
        #   total = total + ventaProd.costo
        
        self.ventana.avisarCambiosDatos(categoria, modeloTabla.totalVentas())
        
        self.venta.subtotal = 0.0
        for modeloTabla in self.lstModelosHijos:
            self.venta.subtotal += modeloTabla.total_ventas
            
        #print('SUBTOTAL_VENTAS:', self.venta.subtotal)
        
    def guardarDatos(self, lstDatos):
        if self.datosNuevos:
            msg = DataModel.LST_MSG[DataModel.MSG_SAVE]
            
            #retorno = self.modelo.dao.insert(self.mov_venta_prod)
            self.venta.colVentasProd = self.modeloVarios.datos + self.modeloPan.datos
            
            retorno = self.modelo.dao.insert(self.venta)
            
            if retorno <= 0:
                msg = DataModel.LST_MSG[DataModel.MSG_NOT_SAVE]
            else:
                self.datosNuevos = False
            
            return (retorno > 0, msg)
        return self.actualizarDatos(lstDatos)
    
    def actualizarDatos(self, lstDatos):
        msg = DataModel.LST_MSG[DataModel.MSG_EDIT]
        #print('ACTUALIZAR_SUBTOTAL:', self.venta.subtotal)
        #retorno = self.modelo.dao.update(self.mov_venta_prod)
        retorno = self.modelo.dao.update(self.venta)
        
        if retorno <= 0:
            msg = DataModel.LST_MSG[DataModel.MSG_NOT_EDIT]
        
        return (retorno > 0, msg)