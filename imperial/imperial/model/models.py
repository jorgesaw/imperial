#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 14/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
import PyQt4.QtCore as _qc
from imperial.core.util.cadenas import printable
import datetime

#uDatos que sirven para diferenciarlos al editar los precios de ambos.
PRECIO_PRODUCTO, PRECIO_INGREDIENTE = range(2) 
#NAME, CODE, EXT_CODE, PRICE, BUY_PRICE, STOCK, PACK_UNITS, CATEGORY, \
#MIN_STOCK, IDEAL_STOCK, DESCRIPTION = range(11)
NAME, PRICE, DESCRIPTION, CATEGORIA_PROD, PRECIO_NUEVO, POS_PRECIO = range(6)
class Product(object):
    """
    """
    name = ""
    #precio = 0.0
    categoria = 1
    #Constants for type of product, it defines the tax it to be charged (depends on other crappy stuff)
    descripcion = ""

    def __init__(self, name="", precio=0.0, categoria=1):
        self.setName(name)
        self.precio = precio
        self.categoria = categoria
        self.activo = True
        
    def __cmp__(self, other):
        return _qc.QString.localeAwareCompare(self.name.lower(),
                                          other.name.lower())
    
    def precioActivo(self, fecha_precio=datetime.date.today()):
        #lstPrecios = set()
        
        fecha_precio_activo = datetime.date(1982, 1, 27)
        precio_activo = None
        
        for precio_guardado in self.colPrecioProd:
            #if self.id == 4:
            #   print('FECHA:', precio_guardado.fecha_ingreso, ' | PRECIO:', precio_guardado.precio)
            if precio_guardado.fecha_ingreso <= fecha_precio:
                #lstPrecios.add(precio_guardado)
                if precio_guardado.fecha_ingreso > fecha_precio_activo:
                    precio_activo = precio_guardado
                    fecha_precio_activo = precio_guardado.fecha_ingreso
                
        #if len(lstPrecios) > 0:        
         #   self.precio = max(lstPrecios).precio
            #print('Hay Precio!!!')
        #else: 
         #   self.precio = 0.0
            #self.precio = min(self.colPrecioProd).precio
        #print(self.precio)
        
        if precio_activo:
            self.precio = precio_activo.precio
        else:
            self.precio = 0.0
        
        #if self.id == 4:
        #   print('El precio activo a la fecha de hot es:', self.precio)
        
        return self.precio
        
    def __str__(self):
        #return "[{0}] ${1:.2f} {2}".format(self.code, self.price, self.name)
        return "{}".format(self.name)

    def setName(self, name):
        self.name = printable(name)
        
    @staticmethod
    def data2Object(lstDatos):
        prod = Product(lstDatos[NAME], lstDatos[PRICE], lstDatos[CATEGORIA_PROD])
        prod.description = lstDatos[DESCRIPTION]
        
        precioProd = PrecioProd(lstDatos[PRICE], datetime.date.today())
        
        prod.colPrecioProd.append(precioProd)
        
        return prod

    @staticmethod
    def object2Data(prod):
        precio = 0.0
        if len(prod.colPrecioProd) > 0:
            precio = prod.colPrecioProd[len(prod.colPrecioProd) - 1].precio
        return [prod.name, precio, 
                prod.description, prod.categoria] 
    
    @staticmethod
    def editObject(prod, lstDatos):
        prod.name = lstDatos[NAME] 
        prod.price = lstDatos[PRICE]
        prod.description = lstDatos[DESCRIPTION]
        prod.categoria = lstDatos[CATEGORIA_PROD]
        
        if lstDatos[PRECIO_NUEVO]:#uSi el precio es nuevo.
            #uCreo un nuevo precio
            precioProd = PrecioProd(lstDatos[PRICE], datetime.date.today())
            prod.colPrecioProd.append(precioProd)
        else:
            #uActualizo el precio
            prod.colPrecioProd[lstDatos[POS_PRECIO]].precio = lstDatos[PRICE]
        
    @staticmethod
    def type():
        return Product
    
PRECIO_PROD, FECHA_INGRESO_PROD = range(2)
class PrecioProd(object):
    u"""Clase que representa el precio de un producto."""
    
    def __init__(self, precio, fecha_ingreso):
        self.precio = precio
        self.fecha_ingreso = fecha_ingreso
        
    def __str__(self):
        return '{}-{}'.format(self.precio, self.fecha_ingreso)
        
    @staticmethod
    def data2Object(lstDatos):
        precioProd = PrecioProd(lstDatos[PRECIO_PROD, FECHA_INGRESO_PROD])
        return precioProd
    
    @staticmethod
    def object2Data(precioProd):
        return [precioProd.ingrediente, precioProd.cant]
    
    @staticmethod
    def editObject(precioProd, lstDatos):
        precioProd.precio = lstDatos[PRECIO_PROD]
        precioProd.fecha_ingreso = lstDatos[FECHA_INGRESO_PROD]
        
    @staticmethod
    def type():
        return PrecioProd  
    
NAME_CATEGORIA, = range(1)
class Category(object):
    VARIOS = 1
    PAN = 2
    
    lstRubros = [u'VARIOS', u'PAN']
    
    name = ""
    def __init__(self, name=""):
        self.name = name
        
    def __str__(self):
        return '{}'.format(self.name)
        
    @staticmethod
    def data2Object(lstDatos):
        category = Category(lstDatos[NAME])
        return category
    
    @staticmethod
    def object2Data(category):
        return [category.name]
    
    @staticmethod
    def editObject(category, lstDatos):
        category.name = lstDatos[NAME]
        
    @staticmethod
    def type():
        return Category

NAME_PROV, EMAIL_PROV, DIRECCION_PROV, BARRIO_PROV, CIUDAD_PROV, \
TELEFONO_PROV, CELULAR_PROV, ALTURA_PROV, PISO_PROV, DEPTO_PROV, PROVINCIA_PROV, \
FECHA_ALTA_PROV, VENDEDOR_PROV = range(13)
class Proveedor(object):
    """Proveedor
    """
    nombre = ""
    direccion = None
    tel = ""
    cel = ""
    fecha_alta = None
    
    def __init__(self, nombre, telefono=None, celular=None, email=None):
        self.nombre = nombre
        self.telefono = telefono
        self.celular = celular
        self.email = email
        self.fecha_alta = datetime.date.today()
        
    def __cmp__(self, other):
        return _qc.QString.localeAwareCompare(self.nombre.lower(),
                                          other.nombre.lower())
        
    @staticmethod
    def data2Object(lstDatos):
        #lstDatos = lstDatosProv[0]
        #lstDatosVendedor = lstDatosProv[1]
        
        prov = Proveedor(lstDatos[NAME_PROV], lstDatos[TELEFONO_PROV], 
                         lstDatos[CELULAR_PROV], lstDatos[EMAIL_PROV])
        #if lstDatos[FECHA_ALTA]:
        #   prov.fecha_alta = lstDatos[FECHA_ALTA]
            
        direccion = Direccion(calle=lstDatos[DIRECCION_PROV],
                            altura=lstDatos[ALTURA_PROV], 
                            barrio=lstDatos[BARRIO_PROV]
                            )
        
        if lstDatos[PISO]:
            direccion.piso = lstDatos[PISO_PROV]
            direccion.depto = lstDatos[DEPTO_PROV]
        
        prov.direccion = direccion
        prov.ciudad = lstDatos[CIUDAD_PROV]
        
        if lstDatos[VENDEDOR_PROV]:
            prov.vendedorProv = lstDatos[VENDEDOR_PROV]
        #uCargo el vendedor/contacto
        #prov.vendedorProv = VendedorProv.data2Object(lstDatosVendedor)
        
        return prov
    
    @staticmethod
    def object2Data(prov):
        lstDatosProv = [prov.nombre, prov.email, prov.direccion.calle, 
                prov.direccion.barrio, prov.ciudad, 
                prov.telefono, prov.celular, 
                prov.direccion.altura, prov.direccion.piso,
                prov.direccion.depto, prov.ciudad.provincia, 
                prov.fecha_alta, prov.vendedorProv]
        
        #lstDatosVendedorProv =  VendedorProv.object2Data(prov.vendedorProv)
        
        return lstDatosProv#[lstDatosProv, lstDatosVendedorProv]
    
    @staticmethod
    def editObject(prov, lstDatos):
        #lstDatosVendedor = lstDatosProv[1]
        
        prov.nombre = lstDatos[NAME]

        direccion = Direccion(calle=lstDatos[DIRECCION_PROV],
                            altura=lstDatos[ALTURA_PROV], 
                            barrio=lstDatos[BARRIO_PROV]
                            )
        if lstDatos[PISO]:
            direccion.piso = lstDatos[PISO_PROV]
            direccion.depto = lstDatos[DEPTO_PROV]
        
        prov.direccion = direccion
        prov.ciudad = lstDatos[CIUDAD_PROV]
        prov.telefono = lstDatos[TELEFONO_PROV]
        prov.celular = lstDatos[CELULAR_PROV]
        prov.email = lstDatos[EMAIL_PROV]
        
        if lstDatos[VENDEDOR_PROV]:
            prov.vendedorProv = lstDatos[VENDEDOR_PROV]
        #VendedorProv.editObject(prov.vendedorProv, lstDatosVendedor)
        
    @staticmethod
    def type():
        return Proveedor


NAME_VEND_PROV, EMAIL_VEND_PROV, DIRECCION_VEND_PROV, BARRIO_VEND_PROV, CIUDAD_VEND_PROV, \
TELEFONO_VEND_PROV, CELULAR_VEND_PROV, ALTURA_VEND_PROV, \
PISO_VEND_PROV, DEPTO_VEND_PROV, PROVINCIA_VEND_PROV, \
FECHA_ALTA_VEND_PROV, PROVEEDOR_VEND = range(13)
class VendedorProv(object):
    
    """VendedorProv
    """
    nombre = ""
    direccion = None
    tel = ""
    cel = ""
    fecha_alta = None
    
    def __init__(self, nombre, telefono=None, celular=None, email=None):
        self.nombre = nombre
        self.telefono = telefono
        self.celular = celular
        self.email = email
        self.fecha_alta = datetime.date.today()
        
    def __cmp__(self, other):
        return _qc.QString.localeAwareCompare(self.nombre.lower(),
                                          other.nombre.lower())
        
    @staticmethod
    def data2Object(lstDatos):
        prov = VendedorProv(lstDatos[NAME_PROV], lstDatos[TELEFONO_PROV], 
                         lstDatos[CELULAR_PROV], lstDatos[EMAIL_PROV])
        #if lstDatos[FECHA_ALTA]:
        #   prov.fecha_alta = lstDatos[FECHA_ALTA]
            
        direccion = Direccion(calle=lstDatos[DIRECCION_PROV],
                            altura=lstDatos[ALTURA_PROV], 
                            barrio=lstDatos[BARRIO_PROV]
                            )
        
        if lstDatos[PISO]:
            direccion.piso = lstDatos[PISO_PROV]
            direccion.depto = lstDatos[DEPTO_PROV]
        
        prov.direccion = direccion
        prov.ciudad = lstDatos[CIUDAD_PROV]
        
        return prov
    
    @staticmethod
    def object2Data(prov):
        return [prov.nombre, prov.email, prov.direccion.calle, 
                prov.direccion.barrio, prov.ciudad, 
                prov.telefono, prov.celular, 
                prov.direccion.altura, prov.direccion.piso,
                prov.direccion.depto, prov.ciudad.provincia, 
                prov.fecha_alta, prov.proveedor]
    
    @staticmethod
    def editObject(prov, lstDatos):
        prov.nombre = lstDatos[NAME]

        direccion = Direccion(calle=lstDatos[DIRECCION_PROV],
                            altura=lstDatos[ALTURA_PROV], 
                            barrio=lstDatos[BARRIO_PROV]
                            )
        if lstDatos[PISO]:
            direccion.piso = lstDatos[PISO_PROV]
            direccion.depto = lstDatos[DEPTO_PROV]
        
        prov.direccion = direccion
        prov.ciudad = lstDatos[CIUDAD_PROV]
        prov.telefono = lstDatos[TELEFONO_PROV]
        prov.celular = lstDatos[CELULAR_PROV]
        prov.email = lstDatos[EMAIL_PROV]
    
    @staticmethod
    def type():
        return VendedorProv
        

NAME_PROV, = range(1)
class Provincia(object):
    u"""Clase que representa una provincia."""

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return '{}'.format(self.nombre)
    
    @staticmethod
    def data2Object(lstDatos):
        prov = Proveedor(lstDatos[NAME])
        return prov
    
    @staticmethod
    def object2Data(prov):
        return [prov.name, ]
    
    @staticmethod
    def editObject(prov, lstDatos):
        prov.nombre = lstDatos[NAME_PROV]
        
    @staticmethod
    def type():
        return Provincia
    
NAME_CIUDAD, COD_POSTAL, DDN = range(3)    
class Ciudad(object):
    u"""Clase que representa una ciudad."""

    def __init__(self, nomCiudad, codPostal, DDN):
        self.nomCiudad = nomCiudad
        self.codPostal = codPostal
        self.DDN = DDN

    def __str__(self):
        return u'{0}'.format(self.nomCiudad)
    
    @staticmethod
    def data2Object(lstDatos):
        ciudad = Ciudad(lstDatos[NAME_CIUDAD], lstDatos[COD_POSTAL], 
                        lstDatos[DDN])
        return ciudad
    
    @staticmethod
    def object2Data(ciudad):
        return [ciudad.nomCiudad, ciudad.codPostal, ciudad.DDN]
    
    @staticmethod
    def editObject(ciudad, lstDatos):
        ciudad.nomCiudad = lstDatos[NAME_CIUDAD]
        ciudad.codPostal = lstDatos[COD_POSTAL]
        ciudad.DDN = lstDatos[DDN]
        
    @staticmethod
    def type():
        return Ciudad

CALLE, ALTURA, PISO, DEPTO, BARRIO = range(5)    
class Direccion(object):
    u"""Clase que representa una dirección física."""

    def __init__(self, calle, altura, piso=None, depto=None, barrio=None):
        self.calle = calle
        self.altura = altura
        self.piso = piso
        self.depto = depto
        self.barrio = barrio

    def __str__(self):
        return '{0} {1}'.format(self.calle, self.altura)
    
    @staticmethod
    def data2Object(lstDatos):
        direc = Direccion(lstDatos[CALLE], lstDatos[ALTURA], lstDatos[PISO], 
                        lstDatos[DEPTO], lstDatos[BARRIO])
        return direc
    
    @staticmethod
    def object2Data(direc):
        return [direc.calle, direc.altura, direc.piso, 
                direc.depto, direc.barrio]
    
    @staticmethod
    def editObject(direc, lstDatos):
        direc.calle = lstDatos[CALLE]
        direc.altura = lstDatos[ALTURA]
        direc.piso = lstDatos[PISO]
        direc.depto = lstDatos[DEPTO]
        direc.barrio = lstDatos[BARRIO]
        
    @staticmethod
    def type():
        return Direccion
    
NOMBRE_EGRESO, = range(1)
class Egreso(object):   
    u"""Egreso
    """ 
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def __cmp__(self, other):
        return _qc.QString.localeAwareCompare(self.nombre.lower(),
                                          other.nombre.lower())
    
    @staticmethod
    def data2Object(lstDatos):
        egreso = Egreso(lstDatos[NOMBRE_EGRESO])
        return egreso
    
    @staticmethod
    def object2Data(egreso):
        return [egreso.nombre, ]
    
    @staticmethod
    def editObject(egreso, lstDatos):
        egreso.nombre = lstDatos[NOMBRE_EGRESO]
        
    @staticmethod
    def type():
        return Egreso
    
VALOR_EGRESO, NOM_EGRESO, FECHA_EGRESO = range(3)
class MovEgreso(object):
    """Clase que representa el movimiento diario de egresos."""
    
    total = 0.0
    
    def __init__(self, saldo_parcial, egreso, fecha):
        self.saldo_parcial = saldo_parcial
        self.egreso = egreso
        self.fecha = fecha
        self.total = 0.0
        
    def setSaldoParcial(self, saldo_parcial):
        self.saldo_parcial = saldo_parcial
        
    def calcularSubtotal(self):
        return self.saldo_parcial
    
    def calcularTotal(self):
        self.total = 0.0
        self.total += self.saldo_parcial
        
        return self.total
        
    def __str__(self):
        return '{}'.format(self.egreso.nombre)
        
    @staticmethod
    def data2Object(lstDatos):
        mov_egreso = MovEgreso(lstDatos[VALOR_EGRESO], lstDatos[NOM_EGRESO], 
                               lstDatos[FECHA_EGRESO])
        return mov_egreso
    
    @staticmethod
    def object2Data(mov_egreso):
        return [mov_egreso.valor, mov_egreso.egreso, mov_egreso.fecha]
    
    @staticmethod
    def editObject(mov_egreso, lstDatos):
        mov_egreso.valor = lstDatos[VALOR_EGRESO]
        mov_egreso.egreso = lstDatos[NOM_EGRESO]
        mov_egreso.fecha = lstDatos[FECHA_EGRESO]
    @staticmethod
    def type():
        return MovEgreso
    
NOMBRE_VEND, ES_VENDEDOR = range(2)
class Vendedor(object):
    u"""Vendedor
    """
    TIPO = 'vendedor'
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = Vendedor.TIPO
        
    def __str__(self):
        return '{}'.format(self.nombre)
    
    def __cmp__(self, other):
        return _qc.QString.localeAwareCompare(self.nombre.lower(),
                                          other.nombre.lower())
    
    @staticmethod
    def data2Object(lstDatos):
        vend = None
        if lstDatos[ES_VENDEDOR]:
            vend = VendedorExterno(lstDatos[NOMBRE_VEND])
        else:
            vend = VendedorInterno(lstDatos[NOMBRE_VEND])
        return vend
    
    @staticmethod
    def object2Data(vend):
        is_vendedor = False
        if isinstance(vend, VendedorExterno):
            is_vendedor = True
            
        return [vend.nombre, is_vendedor]
    
    @staticmethod
    def editObject(vend, lstDatos):
        vend.nombre = lstDatos[NOMBRE_VEND]
        vend.tipo = VendedorExterno.TIPO if lstDatos[ES_VENDEDOR] else \
            VendedorInterno.TIPO
        
    @staticmethod
    def type():
        return Vendedor
    
NOM_VENDEDOR_EXTERNO, = range(1)
class VendedorExterno(Vendedor):
    u"""VendedorExterno
    """
    TIPO = 'vendedor_ext'
    
    def __init__(self, nombre):
        super(VendedorExterno, self).__init__(nombre)
        self.tipo = VendedorExterno.TIPO
        
    def __str__(self):
        return '{}'.format(self.nombre)
    
    @staticmethod
    def data2Object(lstDatos):
        vend = VendedorExterno(lstDatos[NOMBRE_VEND])
        return vend
    
    @staticmethod
    def object2Data(vend):
        return [vend.nombre, ]
    
    @staticmethod
    def editObject(vend, lstDatos):
        vend.nombre = lstDatos[NOMBRE_VEND]
        
    @staticmethod
    def type():
        return VendedorExterno
    
NOM_VENDEDOR_INTERNO, = range(1)
class VendedorInterno(Vendedor):
    u"""VendedorInterno
    """
    TIPO = 'vendedor_int'
    
    def __init__(self, nombre):
        super(VendedorInterno, self).__init__(nombre)
        self.tipo = VendedorInterno.TIPO
        
    def __str__(self):
        return '{}'.format(self.nombre)
    @staticmethod
    def type():
        return VendedorInterno
    
VALOR_VENTA, VENDEDOR, FECHA_VENTA, SALDO_PARCIAL_VENTA, SUBTOTAL_VENTA = range(5)
class Venta(object):
    u"""Venta
    """
    
    subtotal = 0.0
    total = 0.0
    
    def __init__(self, saldo_parcial, vendedor, fecha):
        self.saldo_parcial = saldo_parcial
        self.vendedor = vendedor
        self.fecha = fecha 
        self.subtotal = 0.0
        
    def __str__(self):
        return '{}'.format(self.vendedor.nombre)
    
    def setSaldoParcial(self, saldo_parcial):
        self.saldo_parcial = saldo_parcial
        if isinstance(self.vendedor, VendedorInterno):
            self.subtotal = 0.0
            self.subtotal += self.saldo_parcial
    
    def addVentaProd(self, ventaProd):
        if ventaProd in self.colVentasProd:
            return False

        self.colVentasProd.append(ventaProd)
        return True
    
    def delVentaProd(self, i):
        del self.colVentasProd[i]
        
    def calcular(self):
        self.subtotal = 0.0
        for ventaProd in self.colVentasProd:
            ventaProd.calcular()
            self.subtotal += ventaProd.costo
            
        return self.subtotal
    
    def calcularSubtotal(self):
        if isinstance(self.vendedor, VendedorInterno):
            return self.saldo_parcial
        return self.subtotal
    
    def calcularSaldo(self):
        self.subtotal = 0.0
        for ventaProd in self.colVentasProd:
            ventaProd.setPrecioUnitario(self.fecha)
            ventaProd.totVentas()
            ventaProd.calcular()
            self.subtotal += ventaProd.costo
        return self.subtotal
    
    def calcularTotal(self):
        self.total = 0.0
        
        if isinstance(self.vendedor, VendedorInterno):
            self.total += self.saldo_parcial
        else:
            self.total = self.saldo_parcial + self.subtotal
        
        #print('TOTAL_:', self.total)
        return self.total
    
    @staticmethod
    def data2Object(lstDatos):
        venta = Venta(lstDatos[VALOR_VENTA], 
                      lstDatos[VENDEDOR],
                      lstDatos[FECHA_VENTA])
        return venta
    
    @staticmethod
    def object2Data(venta):
        return [venta.valor, venta.vendedor, venta.fecha, 
                venta.saldo_parcial, venta.subtotal]
    
    @staticmethod
    def editObject(venta, lstDatos):
        venta.vendedor = lstDatos[VENDEDOR]
        venta.valor = lstDatos[VALOR_VENTA]
        venta.fecha = lstDatos[FECHA_VENTA]
        venta.saldo_parcial = lstDatos[SALDO_PARCIAL_VENTA]
        
    @staticmethod
    def type():
        return Venta
    
VALOR_VENTA, VENDEDOR, FECHA_VENTA, SALDO_PARCIAL_VENTA, SUBTOTAL_VENTA = range(5)
class Factura(object):
    u"""Factura
    """
    num_factura = 0
    subtotal = 0.0
    total = 0.0
    con_cinco_por_ciento_descuento = False
    con_iva = False
    
    def __init__(self, vendedor, fecha):
        self.vendedor = vendedor
        self.fecha = fecha 
        self.subtotal = 0.0
        
    def __str__(self):
        return '{}'.format(self.vendedor.nombre)
    
    def setSaldoParcial(self, saldo_parcial):
        self.saldo_parcial = saldo_parcial
        if isinstance(self.vendedor, VendedorInterno):
            self.subtotal = 0.0
            self.subtotal += self.saldo_parcial
    
    def addVentaProd(self, ventaProd):
        if ventaProd in self.colVentasProd:
            return False

        self.colVentasProd.append(ventaProd)
        return True
    
    def delVentaProd(self, i):
        del self.colVentasProd[i]
        
    def calcular(self):
        self.subtotal = 0.0
        for ventaProd in self.colVentasProd:
            ventaProd.calcular()
            self.subtotal += ventaProd.costo
            
        return self.subtotal
    
    def calcularSubtotal(self):
        if isinstance(self.vendedor, VendedorInterno):
            return self.saldo_parcial
        return self.subtotal
    
    def calcularSaldo(self):
        self.subtotal = 0.0
        for ventaProd in self.colVentasProd:
            ventaProd.setPrecioUnitario(self.fecha)
            ventaProd.totVentas()
            ventaProd.calcular()
            self.subtotal += ventaProd.costo
        return self.subtotal
    
    def calcularTotal(self):
        self.total = 0.0
        
        if isinstance(self.vendedor, VendedorInterno):
            self.total += self.saldo_parcial
        else:
            self.total = self.saldo_parcial + self.subtotal
        
        #print('TOTAL_:', self.total)
        return self.total
    
    @staticmethod
    def data2Object(lstDatos):
        venta = Venta(lstDatos[VENDEDOR],
                      lstDatos[FECHA_VENTA])
        return venta
    
    @staticmethod
    def object2Data(venta):
        return [venta.valor, venta.vendedor, venta.fecha, 
                venta.saldo_parcial, venta.subtotal]
    
    @staticmethod
    def editObject(venta, lstDatos):
        venta.vendedor = lstDatos[VENDEDOR]
        venta.fecha = lstDatos[FECHA_VENTA]
        
    @staticmethod
    def type():
        return Factura


FECHA_SALDO, = range(1)
class SaldoDiario(object):
    u""" Saldo diario
    """
    saldo_egresos = 0.0
    saldo_ventas_parcial = 0.0
    
    saldo_ventas_subtotal = 0.0
    saldo_tot_ventas = 0.0
    
    saldo_neto = 0.0
    saldo_parcial = 0.0
    
    def __init__(self, fecha_saldo):
        self.fecha_saldo = fecha_saldo
        
    def saldoEgresos(self):
        self.saldo_egresos = 0.0
        for mov in self.colMovEgresos:
            self.saldo_egresos += mov.saldo_parcial
        
        return self.saldo_egresos
            
    def saldoParcial(self):
        self.saldo_ventas_parcial = 0.0
        for venta in self.colVentas:
            #print('VENTA_SALDO:', venta.saldo_parcial)
            self.saldo_ventas_parcial += venta.saldo_parcial
        #print('SALDO:PARCIAL:', self.saldo_ventas_parcial)
        return self.saldo_ventas_parcial
    
    def saldoVentasSubtotal(self):
        self.saldo_ventas_subtotal = 0.0
        for venta in self.colVentas:
            if isinstance(venta.vendedor, VendedorExterno):
                self.saldo_ventas_subtotal += venta.subtotal
            
        print('SUBTOTAL:', self.saldo_ventas_subtotal)    
        return self.saldo_ventas_subtotal
    
    def saldoTotalVentas(self):
        self.saldo_tot_ventas = self.saldo_ventas_parcial + self.saldo_ventas_subtotal
        return self.saldo_tot_ventas
        
    
    def saldo(self):
        self.saldo_neto = self.saldo_ventas_parcial + self.saldo_ventas_subtotal - self.saldo_egresos
        return self.saldo_neto
    
    @staticmethod
    def data2Object(lstDatos):
        saldo = SaldoDiario(lstDatos[FECHA_SALDO])
        return saldo
    
    @staticmethod
    def object2Data(saldo):
        return [saldo.fecha_saldo, ]
    
    @staticmethod
    def editObject(saldo, lstDatos):
        saldo.fecha_saldo = lstDatos[FECHA_SALDO]
        
    @staticmethod
    def type():
        return SaldoDiario
    
PROD, CANT_INICIAL, DEVOLUCIONES = range(3)
class VentaProd(object):
    u"""Venta producto
    """
    
    CANT_CARGAS = 6
    precio_unitario = 0.0
    costo = 0.0
    tot_venta = 0
    cant_neta = 0
    
    def __init__(self, producto, cant_inicial=0, devoluciones=0, 
                 fecha_ingreso=datetime.date.today()):
        self.setProducto(producto)
        self.cant_inicial = cant_inicial
        self.devoluciones = devoluciones
        
    def setProducto(self, producto, fecha_ingreso=datetime.date.today()):
        self.producto = producto
        self.setPrecioUnitario(fecha_ingreso)
        
    def setDevoluciones(self, devoluciones):
        if devoluciones > self.tot_venta:
            return False
        else:
            self.devoluciones = devoluciones
            return True
        
    def setPrecioUnitario(self, fecha_ingreso):        
        self.precio_unitario = round(self.producto.precioActivo(fecha_ingreso), 2)
        
    def totVentas(self):
        tot = 0.0
        for i in xrange(VentaProd.CANT_CARGAS):
            tot = tot + self.colCargaProd[i].cant
        
        self.tot_venta = tot
        
        return self.tot_venta
    
    def cantNeta(self):
        self.cant_neta = self.tot_venta - self.devoluciones
        
        return self.cant_neta
        
    def calcular(self):
        self.costo = round(self.precio_unitario * float((self.tot_venta - self.devoluciones)), 2)
    
        return self.costo
        
    @staticmethod
    def data2Object(lstDatos):
        ventaProd = VentaProd(lstDatos[PROD], 
                          lstDatos[CANT_INICIAL], 
                          lstDatos[DEVOLUCIONES])
        
        colCargaProd = []
        
        for i in range(VentaProd.CANT_CARGAS):
            cargaProd = CargaProd()
            colCargaProd.append(cargaProd)
            
        ventaProd.colCargaProd = colCargaProd
        
        return ventaProd
    
    @staticmethod
    def object2Data(ventaProd):
        return [ventaProd.producto, ventaProd.cant_inicial, 
                ventaProd.devoluciones]
    
    @staticmethod
    def editObject(ventaProd, lstDatos):
        ventaProd.producto = lstDatos[PROD]
        ventaProd.cant_inicial = lstDatos[CANT_INICIAL]
        ventaProd.devoluciones = lstDatos[DEVOLUCIONES]
        
    @staticmethod
    def type():
        return VentaProd

CANT, FECHA_HORA = range(2)
class CargaProd(object):
    u"""Carga producto
    """
    
    def __init__(self, cant=0.0, fecha_hora=datetime.date.today()):
        self.cant = cant
        self.fecha_hora = fecha_hora
        
    @staticmethod
    def data2Object(lstDatos):
        cargaProd = CargaProd(lstDatos[CANT], 
                          lstDatos[FECHA_HORA])
        return cargaProd
    
    @staticmethod
    def object2Data(cargaProd):
        return [cargaProd.cant, cargaProd.fecha_hora]
    
    @staticmethod
    def editObject(cargaProd, lstDatos):
        cargaProd.cant = lstDatos[CANT]
        cargaProd.fecha_hora = lstDatos[FECHA_HORA]
        
    @staticmethod
    def type():
        return CargaProd

#FECHA_MOV_VENTA_PROD = range(1)
#class MovVentaProd(object):
#   pass
#   """Clase que representa el movimiento de la venta diaria detallada."""
    
  #  total = 0.0
    
   # def __init__(self, fecha=datetime.date.today()):
    #    self.fecha = fecha
    #    
    #def __str__(self):
    #    return '{}'.format(self.vendedor.nombre)
        
    #def addVentaProd(self, ventaProd):
     #   if ventaProd in self.colVentasProd:
      #      return False

       # self.colVentasProd.append(ventaProd)
        #return True
    
    #def delVentaProd(self, i):
     #   del self.colVentasProd[i]
        
    #def calcular(self):
     #   self.total = 0.0
      #  for ventaProd in self.colVentasProd:
       #     ventaProd.calcular()
        #    self.total += ventaProd.costo
            
        #return self.total
    
    #def calcularSaldo(self):
     #   self.total = 0.0
      #  for ventaProd in self.colVentasProd:
       #     ventaProd.setPrecioUnitario(self.fecha)
        #    ventaProd.totVentas()
         #   ventaProd.calcular()
          #  self.total += ventaProd.costo
        #return self.total
    
    #@staticmethod
    #def data2Object(lstDatos):
     #   mov_venta = MovVentaProd(lstDatos[FECHA_MOV_VENTA_PROD])
      #  return mov_venta
    
    #@staticmethod
    #def object2Data(mov_venta):
     #   return [mov_venta.fecha, ]
    
    #@staticmethod
    #def editObject(mov_venta, lstDatos):
     #   mov_venta.fecha = lstDatos[FECHA_MOV_VENTA_PROD]
        
    #@staticmethod
    #def type():
     #   return MovVentaProd
    
PROM_VENTA_RF, CANT_PERS_RF, CAJA_ABAJO_RF, FECHA_RF = range(4)
class ResumenFiscal(object):
    u"""Clase que representa un resumen fiscal."""

    cant_pers_abajo = 0
    
    def __init__(self, prom_venta, cant_pers, caja_abajo, fecha):
        self.prom_venta = prom_venta
        self.cant_pers = cant_pers
        self.caja_abajo = caja_abajo
        self.fecha = fecha
        self.cant_pers_abajo = 0

    def __str__(self):
        return '{}-{}'.format(self.prom_venta)
    
    @staticmethod
    def data2Object(lstDatos):
        rf = ResumenFiscal(lstDatos[PROM_VENTA_RF], lstDatos[CANT_PERS_RF], 
                           lstDatos[CAJA_ABAJO_RF], lstDatos[FECHA_RF])
        return rf
    
    @staticmethod
    def object2Data(rf):
        return [rf.prom_venta, rf.cant_pers, 
                rf.caja_abajo, rf.fecha]
    
    @staticmethod
    def editObject(rf, lstDatos):
        rf.prom_venta = lstDatos[PROM_VENTA_RF]
        rf.cant_pers = lstDatos[CANT_PERS_RF]
        rf.caja_abajo = lstDatos[CAJA_ABAJO_RF]
        rf.fecha = lstDatos[FECHA_RF]
        
    @staticmethod
    def type():
        return ResumenFiscal
    
NOM_INGRED, PRECIO_INGREDIENTE, UNIDAD_INGRED, CANT_UNIDAD_INGRED  = range(4)
class Ingrediente(object):
    """Clase que representa un ingrediente."""
    
    UNIDAD_KG = 0
    UNIDAD_LTS = 1
    UNIDAD_OTROS = 2
    
    CANT_UNIDAD_KG_LTS = -1
    CANT_UNIDAD_KG_LTS_X1 = 0
    
    LST_UNIDADES = [u'Kg.', u'Lts.', u'Unidades']
    LST_MULTIPLO_UND = ['grs.', 'cm3', 'und.']
    LST_CANT_UNIDADADES = [1000, 1]#Equivalencias por kilo/litro o gramo/cm3.
    
    precio = 0.0
    
    def __init__(self, nombre, unidad=UNIDAD_KG, cantUnidad=CANT_UNIDAD_KG_LTS):
        self.nombre = nombre
        self.unidad = unidad
        self.cantUnidad = cantUnidad
        
    def __cmp__(self, other):
        return _qc.QString.localeAwareCompare(self.nombre.lower(),
                                          other.nombre.lower())
        
    def precioActivo(self, fecha_precio=datetime.date.today()):
        lstPrecios = set()
        
        #print('FECHA_FILTRO:', fecha_precio)
        #if self.id == 1:
         #   for precio_guardado in self.colPrecioIngred:
          #      print(precio_guardado)
            #print('MAX_PRECIO:', max(self.colPrecioIngred))
        
        for precio_guardado in self.colPrecioIngred:
            if precio_guardado.fecha_ingreso <= fecha_precio:
                lstPrecios.add(precio_guardado)
        
        if len(lstPrecios) > 0:
            self.precio = max(lstPrecios).precio
        else: 
            self.precio = 0.0#self.precio = min(self.colPrecioIngred).precio
        
        return self.precio
        
    def __str__(self):
        return '{}'.format(self.nombre)
        
    @staticmethod
    def data2Object(lstDatos):
        ingred = Ingrediente(lstDatos[NOM_INGRED],  
                            lstDatos[UNIDAD_INGRED], lstDatos[CANT_UNIDAD_INGRED])
        
        ingred.precio = lstDatos[PRECIO_INGREDIENTE]
        
        precioIngred = PrecioIngred(lstDatos[PRECIO_INGREDIENTE], datetime.date.today())
        ingred.colPrecioIngred.append(precioIngred)
        
        return ingred
    
    @staticmethod
    def object2Data(ingred):
        #for pre in ingred.colPrecioIngred:
        #   print(pre.precio)
        precio = 0.0
        if len(ingred.colPrecioIngred) > 0:
            precio = ingred.colPrecioIngred[len(ingred.colPrecioIngred) - 1].precio
             
        return [ingred.nombre, precio, 
            ingred.unidad, ingred.cantUnidad]
    
    @staticmethod
    def editObject(ingred, lstDatos):
        ingred.nombre= lstDatos[NOM_INGRED]
        ingred.precio = lstDatos[PRECIO_INGRED]
        ingred.unidad = lstDatos[UNIDAD_INGRED]
        ingred.cantUnidad = lstDatos[CANT_UNIDAD_INGRED]
        
        precioIngred = PrecioIngred(lstDatos[PRECIO_INGREDIENTE], datetime.date.today())
        ingred.colPrecioIngred.append(precioIngred)
        
    @staticmethod
    def type():
        return Ingrediente
    
INGRED, CANT_INGRED, FECHA_INGRESO_COSTO, PRECIO_INGRED_COSTO = range(4)
class MovCostoIngred(object):
    u"""Clase que representa el costo de un ingrediente."""
    
    precio_unitario = 0.0
    costo = 0.0
    
    def __init__(self, ingrediente, cant, 
                 fecha_ingreso=datetime.date.today()
                 ):
        self.setIngrediente(ingrediente, fecha_ingreso)
        self.cant = cant
        #self.fechaIngreso = fechaIngreso
        #self.precio_ingred = precio_ingred
        #self.ingrediente.precio = precio_ingred
        
    def copy(self):
        movCostoIngred = MovCostoIngred(self.ingrediente, self.cant)
        
        return movCostoIngred

    def setIngrediente(self, ingred, fecha_ingreso=datetime.date.today()):
        self.ingrediente = ingred
        self.setPrecioUnitario(fecha_ingreso)
        
    def setPrecioUnitario(self, fecha_ingreso):        
        self.precio_unitario = round(self.ingrediente.precioActivo(fecha_ingreso), 2)
        
    def calcular(self):
        #print(self.cant, self.ingrediente.cantUnidad, self.precio_unitario, 
        #     round(self.cant/float(self.ingrediente.cantUnidad) * self.precio_unitario, 2))
        cant_unidad = self.ingrediente.cantUnidad
        
        if cant_unidad <= Ingrediente.CANT_UNIDAD_KG_LTS_X1:
            cant_unidad = Ingrediente.LST_CANT_UNIDADADES[cant_unidad + 1]
        
        #self.costo = round(self.cant/float(self.ingrediente.cantUnidad) * self.precio_unitario, 2)
        self.costo = round(self.cant/float(cant_unidad) * self.precio_unitario, 2)
        return self.costo
    
    def __str__(self):
        return '{}-{}'.format(self.ingrediente, self.cant)
        
    @staticmethod
    def data2Object(lstDatos):
        movCostoProd = MovCostoIngred(lstDatos[INGRED, CANT_INGRED])
        if len(lstDatos) > 2 and lstDatos[FECHA_INGRESO_COSTO]:
            movCostoProd.fechaIngreso = lstDatos[FECHA_INGRESO_COSTO]
        movCostoProd.precio_ingred = lstDatos[PRECIO_INGRED_COSTO]
        return movCostoProd
    
    @staticmethod
    def object2Data(movCostoProd):
        return [movCostoProd.ingrediente, movCostoProd.cant, 
                movCostoProd.fechaIngreso, movCostoProd.precio_ingred]
    
    @staticmethod
    def editObject(movCostoProd, lstDatos):
        movCostoProd.ingrediente= lstDatos[INGRED]
        movCostoProd.cant = lstDatos[PRECIO_INGRED_COSTO]
        movCostoProd.fechaIngreso = lstDatos[FECHA_INGRESO_COSTO]
        movCostoProd.precio_ingred = lstDatos[PRECIO_INGRED_COSTO]
        
    @staticmethod
    def type():
        return MovCostoIngred

FECHA_COSTO_X, GASTOS_COSTO_X, CANTIDAD_PROD_X, DESC_COSTO_X = range(4)
class CostoProd(object):
    u"""Clase que representa el costo de un producto."""
    
    def __init__(self, producto, fecha_ingreso=datetime.date.today(), gastos=0.0, cant=0):
        self.producto = producto
        self.fecha_ingreso = fecha_ingreso
        self.gastos = gastos
        self.cant = cant
        self.total = 0.0
        self.desc = ''
        
    def addMovCosto(self, movCosto):
        if movCosto in self.colMovCostoIngred:
            return False

        self.colMovCostoIngred.append(movCosto)
        
        return True
    
    def delMovCosto(self, i):
        del self.colMovCostoIngred[i]
        
    def calcular(self):
        self.total = 0.0
        for mov in self.colMovCostoIngred:
            mov.calcular()
            self.total += mov.costo
            
        
    def __str__(self):
        #return '{}-{}'.format(self.producto, self.cant)
        return '{}'.format(self.fecha_ingreso)
    
    @staticmethod
    def data2Object(lstDatos):
        costoProd = CostoProd(lstDatos[FECHA_COSTO_X], lstDatos[GASTOS_COSTO_X], 
                              lstDatos[CANTIDAD_PROD_X])
        
        costoProd.desc = lstDatos[DESC_COSTO_X]
        
        return costoProd
    
    @staticmethod
    def object2Data(costoProd):
        return [costoProd.fecha_ingreso, costoProd.gastos, 
                costoProd.cant, costoProd.desc]
    
    @staticmethod
    def editObject(costoProd, lstDatos):
        costoProd.ingrediente= lstDatos[FECHA_COSTO_X]
        costoProd.cant = lstDatos[GASTOS_COSTO_X]
        costoProd.fechaIngreso = lstDatos[CANTIDAD_PROD_X]
        costoProd.desc = lstDatos[DESC_COSTO_X]
        
    @staticmethod
    def type():
        return CostoProd
    
PRECIO_INGRED, FECHA_INGRESO_INGRED = range(2)
class PrecioIngred(object):
    u"""Clase que representa el precio de un ingrediente."""
    
    def __init__(self, precio, fecha_ingreso):
        self.precio = precio
        self.fecha_ingreso = fecha_ingreso
        
    def __str__(self):
        return '{}-{}'.format(self.precio, self.fecha_ingreso)
        
    @staticmethod
    def data2Object(lstDatos):
        precioIngred = PrecioIngred(lstDatos[PRECIO_INGRED, FECHA_INGRESO_INGRED])
        return precioIngred
    
    @staticmethod
    def object2Data(precioIngred):
        return [precioIngred.ingrediente, precioIngred.cant]
    
    @staticmethod
    def editObject(precioIngred, lstDatos):
        precioIngred.precio = lstDatos[PRECIO_INGRED]
        precioIngred.fecha_ingreso = lstDatos[FECHA_INGRESO_INGRED]
        
    @staticmethod
    def type():
        return PrecioIngred