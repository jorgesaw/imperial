#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 14/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.model.models import Category, Product, Proveedor, Ciudad, \
    Provincia, Direccion, Egreso, MovEgreso, Venta, Vendedor, VentaProd, CargaProd, \
    ResumenFiscal, Ingrediente, PrecioIngred, MovCostoIngred, CostoProd, PrecioProd, \
    SaldoDiario, VendedorExterno, VendedorInterno, VendedorProv
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Boolean, \
    Time, ForeignKey, Table, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import mapper, relationship, backref
from sqlalchemy.sql.sqltypes import Text

meta = MetaData()

provinciaTabla = Table('PROVINCIAS', meta,
    Column('id_prov', Integer, primary_key=True),
    Column('nom_prov', String(30), nullable=False),
    mysql_engine='InnoDB'
)

mapper(Provincia, provinciaTabla, properties={
    'id': provinciaTabla.c.id_prov,
    'nombre': provinciaTabla.c.nom_prov,
    'colCiudades': relationship(Ciudad, 
                             lazy="dynamic",
                             cascade="all, delete-orphan")
})

ciudadTabla = Table("CIUDADES", meta, 
    Column('id_ciudad', Integer, primary_key=True),
    Column('nom_ciudad', String(40), nullable=False),
    Column('cod_postal', String(12), nullable=False),
    Column('DDN', String(10), nullable=False),
    Column('id_prov', Integer,
           ForeignKey('PROVINCIAS.id_prov', ondelete="CASCADE")),
    mysql_engine='InnoDB'
)

mapper(Ciudad, ciudadTabla, properties={
    'id': ciudadTabla.c.id_ciudad,
    'nomCiudad': ciudadTabla.c.nom_ciudad,
    'codPostal': ciudadTabla.c.cod_postal,
    'DDN': ciudadTabla.c.DDN,
    'provincia': relationship(Provincia,
                         backref='PROVINCIAS',
                         lazy="joined") # Carga la provincia al momento de buscar la mascota en la DB.
})

direccionTabla = Table("DIRECCIONES", meta,
    Column('id_direccion', Integer, primary_key=True),
    Column('calle', String(40), nullable=False),
    Column('altura', String(8), nullable=False),
    Column('piso', String(3), nullable=True),
    Column('depto', String(5), nullable=True),
    Column('barrio', String(30)), 
    mysql_engine='InnoDB'
)

mapper(Direccion, direccionTabla, properties={
    'id': direccionTabla.c.id_direccion,
    'calle': direccionTabla.c.calle, 
    'altura': direccionTabla.c.altura, 
    'piso': direccionTabla.c.piso,
    'depto': direccionTabla.c.depto,
    'barrio': direccionTabla.c.barrio
})

#categoriaTabla = Table('CATEGORIAS', meta,
 #   Column('id_category', Integer, primary_key=True),
  #  Column('name', String(50), nullable=False),
   # mysql_engine='InnoDB'
#)

#mapper(Category, categoriaTabla, properties={
    #   'id': categoriaTabla.c.id_category,
    #  'name': categoriaTabla.c.name,
    # 'products': relationship(Product, 
    #                         lazy="dynamic",
    #                        cascade="all, delete-orphan")
#})

productoTabla = Table("PRODUCTOS", meta,
    Column('id_product', Integer, primary_key=True),
    Column('name', String(50), nullable=False, index=True),
    Column('precio', Float, nullable=False),
    Column('description', String(100)),
    Column('categoria', Integer, nullable=False),
    Column('activo', Boolean, default=True),
    #       ForeignKey('CATEGORIAS.id_category', ondelete="CASCADE", onupdate="CASCADE")), 
    mysql_engine='InnoDB'
)
mapper(Product, productoTabla, properties={
    'id': productoTabla.c.id_product, 
    'name': productoTabla.c.name, 
    'precio': productoTabla.c.precio, 
    'description': productoTabla.c.description, 
    'categoria': productoTabla.c.categoria, 
    'activo': productoTabla.c.activo, 
    'colPrecioProd': relationship(PrecioProd, 
                             lazy="joined",
                             cascade="all, delete-orphan"), 
    'colCostosProd': relationship(CostoProd, 
                             lazy="joined",
                             cascade="all, delete-orphan"), 
})

precioProdTabla = Table('PRECIO_PROD', meta,
    Column('id_precio_prod', Integer, primary_key=True),
    Column('precio', Float, nullable=False),
    Column('fecha_ingreso', Date, nullable=False),
    Column('id_product', Integer, ForeignKey('PRODUCTOS.id_product')),
    mysql_engine='InnoDB'
)
mapper(PrecioProd, precioProdTabla, properties={
    'id': precioProdTabla.c.id_precio_prod,
    'precio': precioProdTabla.c.precio,
    'fecha_ingreso': precioProdTabla.c.fecha_ingreso,
    'producto': relationship(Product,
                         backref='PRODUCTOS',
                         lazy="joined") 
})

proveedorTabla = Table("PROVEEDORES", meta, 
    Column('id_prov', Integer, primary_key=True),              
    Column('nombre', String(50), nullable=False),
    Column('fecha_alta', Date, nullable=False),
    Column('email', String(50), nullable=True),
    Column('telefono', String(18), nullable=True),
    Column('celular', String(18), nullable=True),
    Column('id_vendedor_prov', Integer, ForeignKey('VENDEDOR_PROV.id_vendedor_prov')), 
    Column('id_ciudad', Integer, ForeignKey('CIUDADES.id_ciudad')),                   
    Column('id_direccion', Integer, ForeignKey('DIRECCIONES.id_direccion')),
    mysql_engine='InnoDB'
)

mapper(Proveedor, proveedorTabla, properties={
    'id': proveedorTabla.c.id_prov,
    'nombre': proveedorTabla.c.nombre,
    'fecha_alta': proveedorTabla.c.fecha_alta, 
    'email': proveedorTabla.c.email, 
    'telefono': proveedorTabla.c.telefono,
    'celular': proveedorTabla.c.celular,
    'vendedorProv': relationship(VendedorProv,
                         uselist=False), 
    'direccion': relationship(Direccion,
                         uselist=False), 
    'ciudad': relationship(Ciudad,
            lazy="joined")
})

vendedorProvTabla = Table("VENDEDOR_PROV", meta, 
    Column('id_vendedor_prov', Integer, primary_key=True),              
    Column('nombre', String(50), nullable=False),
    Column('fecha_alta', Date, nullable=False),
    Column('email', String(50), nullable=True),
    Column('telefono', String(18), nullable=True),
    Column('celular', String(18), nullable=True),
    Column('id_ciudad', Integer, ForeignKey('CIUDADES.id_ciudad')),                   
    Column('id_direccion', Integer, ForeignKey('DIRECCIONES.id_direccion')),
    mysql_engine='InnoDB'
)

mapper(VendedorProv, vendedorProvTabla, properties={
    'id': vendedorProvTabla.c.id_vendedor_prov,
    'nombre': vendedorProvTabla.c.nombre,
    'fecha_alta': vendedorProvTabla.c.fecha_alta, 
    'email': vendedorProvTabla.c.email, 
    'telefono': vendedorProvTabla.c.telefono,
    'celular': vendedorProvTabla.c.celular,
    'proveedor': relationship(Proveedor,
                         backref='PROVEEDORES',
                         lazy="dynamic"), 
    'direccion': relationship(Direccion,
                         uselist=False), 
    'ciudad': relationship(Ciudad,
            lazy="joined")
})

saldosTabla = Table('SALDOS', meta,
    Column('id_saldo', Integer, primary_key=True),
    Column('fecha_saldo', Date, nullable=False),
    mysql_engine='InnoDB'
)

mapper(SaldoDiario, saldosTabla, properties={
    'id': saldosTabla.c.id_saldo,
    'fecha_saldo': saldosTabla.c.fecha_saldo,  
    'colMovEgresos': relationship(lambda: MovEgreso,
                        lazy="joined",
                        #order_by=lambda: MovEgreso.id, 
                        cascade="all, delete-orphan"), 
    'colVentas': relationship(lambda: Venta,
                        lazy="joined",
                        #order_by=lambda: Venta.id, 
                        cascade="all, delete-orphan"), 
    #'colMovVentasProd': relationship(MovVentaProd, 
     #                        lazy="joined",
      #                       cascade="all, delete-orphan")
})

egresoTabla = Table('EGRESOS', meta,
    Column('id_egreso', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('activo', Boolean, default=True),
    mysql_engine='InnoDB'
)

mapper(Egreso, egresoTabla, properties={
    'id': egresoTabla.c.id_egreso,
    'nombre': egresoTabla.c.name, 
    'activo': egresoTabla.c.activo
})

mov_egresoTabla = Table('MOV_EGRESOS', meta,
    Column('id_mov_egreso', Integer, primary_key=True),
    #Column('valor_mov', Float, nullable=False),
    Column('saldo_parcial', Float, nullable=False),
    Column('fecha_mov', Date, nullable=False),
    Column('id_egreso', Integer, ForeignKey('EGRESOS.id_egreso')),
    Column('id_saldo', Integer, ForeignKey('SALDOS.id_saldo')),
    mysql_engine='InnoDB'
)

mapper(MovEgreso, mov_egresoTabla, properties={
    'id': mov_egresoTabla.c.id_mov_egreso,
    #'valor': mov_egresoTabla.c.valor_mov, 
    'saldo_parcial': mov_egresoTabla.c.saldo_parcial, 
    'fecha': mov_egresoTabla.c.fecha_mov, 
    'egreso': relationship(Egreso,
                         uselist=False, 
                         lazy="joined"), 
    #'saldo': relationship(SaldoDiario,
     #                    backref='SALDOS',
      #                   lazy="joined"),
})

vendedorTabla = Table('VENDEDORES', meta,
    Column('id_vendedor', Integer, primary_key=True),
    Column('nombre', String(50), nullable=False),
    Column('tipo', String(20)),
    Column('activo', Boolean, default=True),
    mysql_engine='InnoDB'
)

mapperVendedor = mapper(Vendedor, vendedorTabla, properties={
    'id': vendedorTabla.c.id_vendedor,
    'nombre': vendedorTabla.c.nombre,
    'tipo': vendedorTabla.c.tipo, 
    'activo': vendedorTabla.c.activo
}, 
    polymorphic_on=vendedorTabla.c.tipo,
    polymorphic_identity='vendedor'
)

vendedorExternoMapper = mapper(VendedorExterno, inherits=mapperVendedor,
        polymorphic_identity='vendedor_ext'
)

vendedorInternoMapper = mapper(VendedorInterno, inherits=mapperVendedor,
        polymorphic_identity='vendedor_int'
)

ventasTabla = Table('VENTAS', meta,
    Column('id_venta', Integer, primary_key=True),
    #Column('valor_venta', Float, nullable=False),
    Column('fecha_venta', Date, nullable=False),
    Column('subtotal', Float, default=0.0),
    Column('saldo_parcial', Float, default=0.0),
    Column('id_vendedor', Integer, ForeignKey('VENDEDORES.id_vendedor')),
    Column('id_saldo', Integer, ForeignKey('SALDOS.id_saldo')),
    mysql_engine='InnoDB'
)

mapper(Venta, ventasTabla, properties={
    'id': ventasTabla.c.id_venta,
    #'valor': ventasTabla.c.valor_venta,
    'fecha': ventasTabla.c.fecha_venta,  
    'subtotal': ventasTabla.c.subtotal, 
    'saldo_parcial': ventasTabla.c.saldo_parcial, 
    'vendedor': relationship(Vendedor,
                         uselist=False, 
                         lazy="joined"), 
    'colVentasProd': relationship(VentaProd, 
                             lazy="joined", 
                             cascade="all, delete-orphan"),
    #'saldo': relationship(SaldoDiario,
     #                    backref='SALDOS',
      #                   lazy="joined"), 
})

rfTabla = Table('RESUMENES_FISCALES', meta,
    Column('id_rf', Integer, primary_key=True),
    Column('fecha', Date, nullable=False),
    Column('prom_venta', Float, nullable=False),
    Column('cant_pers', Integer, nullable=False),
    Column('caja_abajo', Float, nullable=False),
    mysql_engine='InnoDB'
)

mapper(ResumenFiscal, rfTabla, properties={
    'id': rfTabla.c.id_rf,
    'fecha': rfTabla.c.fecha, 
    'prom_venta': rfTabla.c.prom_venta, 
    'cant_pers': rfTabla.c.cant_pers,
    'caja_abajo': rfTabla.c.caja_abajo,
})

#movVentaProdTabla = Table('MOV_VENTAS_PRODUCTO', meta, 
#    Column('id_mov_venta_prod', Integer, primary_key=True),
#    Column('fecha', Date, nullable=False),
#    Column('id_vendedor', Integer, ForeignKey('VENDEDORES.id_vendedor')),
#    Column('id_saldo', Integer, ForeignKey('SALDOS.id_saldo')),
#    mysql_engine='InnoDB'
#)
#mapper(MovVentaProd, movVentaProdTabla, properties={
#    'id': movVentaProdTabla.c.id_mov_venta_prod,
#    'fecha': movVentaProdTabla.c.fecha,
#    'vendedor': relationship(Vendedor,
#                         uselist=False, 
#                         lazy="joined"), 
#    'colVentasProd': relationship(VentaProd, 
#                            lazy="dynamic",
#                             cascade="all, delete-orphan")
#})

ventasProdTabla = Table('VENTAS_PRODUCTO', meta, 
    Column('id_venta_prod', Integer, primary_key=True),
    #Column('cant_inicial', Integer, nullable=False),
    Column('devoluciones', Float),
    Column('id_product', Integer, ForeignKey('PRODUCTOS.id_product')),
    Column('id_venta', Integer,
           ForeignKey('VENTAS.id_venta', ondelete="CASCADE")),
    mysql_engine='InnoDB'
)

mapper(VentaProd, ventasProdTabla, properties={
    'id': ventasProdTabla.c.id_venta_prod,
    #'cant_inicial': ventasProdTabla.c.cant_inicial, 
    'devoluciones': ventasProdTabla.c.devoluciones, 
    'producto': relationship(Product,
                         uselist=False), 
    'venta': relationship(Venta,
                         backref='VENTAS',
                         lazy="joined"), 
    'colCargaProd': relationship(CargaProd, 
                             lazy="joined",
                             cascade="all, delete-orphan")
})

cargaProdTabla = Table("CARGA_PRODUCTOS", meta, 
    Column('id_carga_prod', Integer, primary_key=True),
    Column('fecha_hora', DateTime, nullable=False),
    Column('cant', Float),
    Column('id_venta_prod', Integer,
           ForeignKey('VENTAS_PRODUCTO.id_venta_prod', ondelete="CASCADE")),
    mysql_engine='InnoDB'
)

mapper(CargaProd, cargaProdTabla, properties={
    'id': cargaProdTabla.c.id_carga_prod,
    'fecha_hora': cargaProdTabla.c.fecha_hora,
    'cant': cargaProdTabla.c.cant,
    'ventaProd': relationship(VentaProd,
                         backref='VENTAS_PRODUCTO',
                         lazy="joined") 
})

ingredienteTabla = Table('INGREDIENTES', meta,
    Column('id_ingrediente', Integer, primary_key=True),
    Column('nombre', String(50), nullable=False),
    #Column('precio', Float, nullable=False),
    Column('unidad', Integer, nullable=False),
    Column('cantUnidad', Integer),
    Column('activo', Boolean, default=True),
    mysql_engine='InnoDB'
)

mapper(Ingrediente, ingredienteTabla, properties={
    'id': ingredienteTabla.c.id_ingrediente,
    'nombre': ingredienteTabla.c.nombre, 
    #'precio': ingredienteTabla.c.precio, 
    'unidad': ingredienteTabla.c.unidad, 
    'cantUnidad': ingredienteTabla.c.cantUnidad, 
    'activo': ingredienteTabla.c.activo, 
    'colPrecioIngred': relationship(PrecioIngred, 
                             lazy="joined",
                             cascade="all, delete-orphan")
})

precioIngredTabla = Table('PRECIO_INGREDIENTES', meta,
    Column('id_precio_ingred', Integer, primary_key=True),
    Column('precio', Float, nullable=False),
    Column('fecha_ingreso', Date, nullable=False),
    Column('id_ingred', Integer, ForeignKey('INGREDIENTES.id_ingrediente')),
    mysql_engine='InnoDB'
)
mapper(PrecioIngred, precioIngredTabla, properties={
    'id': precioIngredTabla.c.id_precio_ingred,
    'precio': precioIngredTabla.c.precio,
    'fecha_ingreso': precioIngredTabla.c.fecha_ingreso,
    'ingrediente': relationship(Ingrediente,
                         backref='INGREDIENTES',
                         lazy="joined") 
})

movCostoIngred = Table("MOV_COSTO_INGRED", meta, 
    Column('id_mov_costo', Integer, primary_key=True),
    Column('cant', Integer),
    #Column('fecha_ingreso', DateTime, nullable=False),
    Column('id_ingred', Integer, ForeignKey('INGREDIENTES.id_ingrediente')),
    Column('id_costo_prod', Integer, ForeignKey('COSTOS_PROD.id_costo_prod')),
    mysql_engine='InnoDB'
)

mapper(MovCostoIngred, movCostoIngred, properties={
    'id': movCostoIngred.c.id_mov_costo,
    'cant': movCostoIngred.c.cant,
    #'fecha_ingreso': movCostoIngred.c.fecha_ingreso,
    'ingrediente': relationship(Ingrediente,
                         uselist=False), 
    #'precio_ingred': relationship(PrecioIngred,
     #                    uselist=False) 
     'costoProd': relationship(CostoProd,
                         backref='COSTOS_PROD',
                         lazy="joined"), 
})

costoProdTabla = Table("COSTOS_PROD", meta, 
    Column('id_costo_prod', Integer, primary_key=True),
    Column('gastos', Float, nullable=False),
    Column('cant', Float, nullable=False),
    Column('fecha_ingreso', Date, nullable=False),
    Column('desc', Text(1300)),
    Column('id_product', Integer, ForeignKey('PRODUCTOS.id_product')),
    mysql_engine='InnoDB'
)

mapper(CostoProd, costoProdTabla, properties={
    'id': costoProdTabla.c.id_costo_prod,
    'gastos': costoProdTabla.c.gastos,
    'cant': costoProdTabla.c.cant,
    'fecha_ingreso': costoProdTabla.c.fecha_ingreso,
    'desc': costoProdTabla.c.desc,
    'producto': relationship(Product,
                             lazy="joined",
                         uselist=False), 
    'colMovCostoIngred': relationship(MovCostoIngred, 
                             lazy="joined",
                             cascade="all, delete-orphan"), 
    #'producto': relationship(Product,
     #                    backref='PRODUCTOS',
      #                   lazy="joined"), 
})

def main():
    import imperial.core.dao.config as config
    
    engine = create_engine(config.cargarConfig())
    meta.drop_all(engine)
    meta.create_all(engine)
    
    print(u"Se crearon las tablas con éxito")

if __name__ == '__main__':
    main()