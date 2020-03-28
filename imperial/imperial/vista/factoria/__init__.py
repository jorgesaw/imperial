#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 31/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.dao.DAOQueryAlchemy import DAOQueryAlchemy
from imperial.core.model.genericmodel.genericModel import Model
from imperial.core.model.genericmodel.modeloGenBusqueda import ModeloGenBusqueda
from imperial.core.model.modelotable.modeloTabla import ModeloTabla
from imperial.core.model.modelotable.modeloTablaBusqueda import \
    ModeloTablaBusqueda
from imperial.dao.DAOCategory import DAOCategory
from imperial.dao.DAOCiudad import DAOCiudad
from imperial.dao.DAOCostosProd import DAOCostosProd
from imperial.dao.DAOEgreso import DAOEgreso
from imperial.dao.DAOIngrediente import DAOIngrediente
from imperial.dao.DAOMovVentaProd import DAOMovVentaProd
from imperial.dao.DAOProducto import DAOProducto
from imperial.dao.DAOProveedor import DAOProveedor
from imperial.dao.DAOResumenFiscal import DAOResumenFiscal
from imperial.dao.DAOSaldos import DAOSaldos
from imperial.dao.DAOVendedor import DAOVendedor
from imperial.dao.DAOVendedorProv import DAOVendedorProv
from imperial.dao.DAOVenta import DAOVenta
from imperial.model.ModeloVentaDiaria import ModeloVentaDiaria
from imperial.model.modeloReportesSaldos import ModeloReportesSaldos
from imperial.model.models import Product, Category, Egreso, Vendedor, Proveedor, \
    Ciudad, ResumenFiscal, Ingrediente, VENDEDOR, MovEgreso, SaldoDiario, Venta, \
    VendedorProv
from imperial.model.modeltable.modeldatatable.mdtBusquedaVendedorProv import \
    MDTBusquedaVendedorProv
from imperial.model.modeltable.modeldatatable.mdtCategory import \
    ModeloDatosTablaCategory
from imperial.model.modeltable.modeldatatable.mdtCiudad import \
    ModeloDatosTablaCiudad
from imperial.model.modeltable.modeldatatable.mdtEgreso import \
    ModeloDatosTablaEgreso
from imperial.model.modeltable.modeldatatable.mdtInformeSaldoSemanal import \
    MDTInformeSaldoSemanal
from imperial.model.modeltable.modeldatatable.mdtIngrediente import \
    ModeloDatosTablaIngred
from imperial.model.modeltable.modeldatatable.mdtProduct import \
    ModeloDatosTablaProduct
from imperial.model.modeltable.modeldatatable.mdtProveedor import \
    ModeloDatosTablaProveedor
from imperial.model.modeltable.modeldatatable.mdtVendedor import \
    ModeloDatosTablaVendedor
from imperial.model.modeltable.modeldatatable.mdtVendedorProv import \
    MDTVendedorProv
from imperial.model.modeltable.modeldatatable.tmVentaDiariaVariedades import \
    TMVentaDiariaVariedades
from imperial.model.modeltable.tableModelCostosProd import TableModelCostosProd
from imperial.model.modeltable.tableModelProductIngred import \
    TableModelProductIngred
from imperial.model.modeltable.tableModelResumenFiscal import \
    TableModelResumenFiscal
from imperial.model.modeltable.tableModelSaldoDiario import \
    TableModelSaldoDiario
from imperial.model.modeltable.tableReporteSaldoDiario import \
    TableReporteSaldoDiario
from imperial.vista.gui.busqueda import BusquedaEgresoDlg
from imperial.vista.gui.busqueda.BusquedaCiudadDlg import BusquedaCiudadDlg
from imperial.vista.gui.busqueda.BusquedaGenericaDlg import BusquedaGenericaDlg
from imperial.vista.gui.busqueda.BusquedaProductoDlg import BusquedaProductoDlg
from imperial.vista.gui.busqueda.BusquedaProveedorDlg import \
    BusquedaProveedorDlg
from imperial.vista.gui.busqueda.BusquedaVendedorDlg import BusquedaVendedorDlg
from imperial.vista.gui.crud.crudCategoryDlg import CrudCategoryDlg
from imperial.vista.gui.crud.crudEgresoDlg import CrudEgresoDlg
from imperial.vista.gui.crud.crudIngredienteDlg import CrudIngredienteDlg
from imperial.vista.gui.crud.crudProductDlg import CrudProductDlg
from imperial.vista.gui.crud.crudProveedoresDlg import CrudProveedoresDlg
from imperial.vista.gui.crud.crudVendedorDlg import CrudVendedorDlg
from imperial.vista.gui.crud.crudVendedoresProvDlg import CrudVendedoresProvDlg
from imperial.vista.gui.dlg.CostoProduccionDlg import CostoProduccionDlg
from imperial.vista.gui.dlg.InformesSaldosDlg import InformesSaldoDlg
from imperial.vista.gui.dlg.ResumenFiscalDlg import ResumenFiscalDlg
from imperial.vista.gui.dlg.SaldoDiarioDlg import SaldoDiarioDlg
from imperial.vista.gui.dlg.VentaDiariaDlg import VentaDiariaDlg


APP_EXIT, PRODUCTOS_SHOW, \
    VENTAS_SHOW, EGRESOS_SHOW, \
    PROVEEDORES_SHOW, VENDEDORES_PROV_SHOW, INGREDIENTES_SHOW, \
    PLANILLA_DIARIA, VENTA_DIARIA, \
    RESUMEN_FISCAL, COSTOS_PROD, REP_PLANILLA_DIARIA, \
    REP_VENTA_DIARIA = range(13)
    
LST_GENERIC_WINDOW = [APP_EXIT, PRODUCTOS_SHOW, 
                      VENTAS_SHOW, EGRESOS_SHOW,
                      PROVEEDORES_SHOW, VENDEDORES_PROV_SHOW, 
                      INGREDIENTES_SHOW, PLANILLA_DIARIA, VENTA_DIARIA, 
                      RESUMEN_FISCAL, COSTOS_PROD, 
                      REP_PLANILLA_DIARIA, REP_VENTA_DIARIA]

SEARCH_PROD, SEARCH_VENDEDOR, SEARCH_EGRESO, SEARCH_PROVEEDORES, \
SEARCH_CIUDAD, SEARCH_INGREDIENTE, SEARCH_VENDEDOR_PROV = range(7)

LST_GENERIC_SEARCH = [SEARCH_PROD, SEARCH_VENDEDOR, SEARCH_EGRESO, 
                      SEARCH_PROVEEDORES, SEARCH_CIUDAD, SEARCH_INGREDIENTE, 
                      SEARCH_VENDEDOR_PROV]

DIC_LIST_CLASES = { 
    PRODUCTOS_SHOW: {'clase_modelo': Product,#getClaseModelo(PATH_MODELS, 'Product'), 
                   'dao': DAOProducto,#getClaseModelo(PATH_DAO + 'DAOProducto.', 'DAOProducto'), 
                   'modelo': ModeloGenBusqueda,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': ModeloDatosTablaProduct, #getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtProduct.', 
                                                        #'ModeloDatosTablaProduct'),
                   'modelo_tabla': TableModelProductIngred, #ModeloTabla,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': CrudProductDlg,#getClaseModelo(PATH_CRUD + 'crudProductDlg.', 'CrudProductDlg')
    },
    VENTAS_SHOW: {'clase_modelo': Vendedor,#getClaseModelo(PATH_MODELS, 'Category'), 
                   'dao': DAOVendedor,#getClaseModelo(PATH_DAO + 'DAOCategory.', 'DAOCategory'), 
                   'modelo': ModeloGenBusqueda,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': ModeloDatosTablaVendedor,#getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtCategory.', 
                                                        #'ModeloDatosTablaCategory'),
                   'modelo_tabla': ModeloTablaBusqueda,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': CrudVendedorDlg,#getClaseModelo(PATH_CRUD + 'crudCategoryDlg.', 'CrudCategoryDlg')
    },
    EGRESOS_SHOW: {'clase_modelo': Egreso,#getClaseModelo(PATH_MODELS, 'Category'), 
                   'dao': DAOEgreso,#getClaseModelo(PATH_DAO + 'DAOCategory.', 'DAOCategory'), 
                   'modelo': ModeloGenBusqueda,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': ModeloDatosTablaEgreso,#getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtCategory.', 
                                                        #'ModeloDatosTablaCategory'),
                   'modelo_tabla': ModeloTablaBusqueda,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': CrudEgresoDlg,#getClaseModelo(PATH_CRUD + 'crudCategoryDlg.', 'CrudCategoryDlg')
    },
    PROVEEDORES_SHOW: {'clase_modelo': Proveedor,#getClaseModelo(PATH_MODELS, 'Category'), 
                   'dao': DAOProveedor,#getClaseModelo(PATH_DAO + 'DAOCategory.', 'DAOCategory'), 
                   'modelo': Model,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': ModeloDatosTablaProveedor,#getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtCategory.', 
                                                        #'ModeloDatosTablaCategory'),
                   'modelo_tabla': ModeloTabla,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': CrudProveedoresDlg,#getClaseModelo(PATH_CRUD + 'crudCategoryDlg.', 'CrudCategoryDlg')
    }, 
    VENDEDORES_PROV_SHOW: {'clase_modelo': VendedorProv, 
                   'dao': DAOVendedorProv, 
                   'modelo': Model, 
                   'modelo_datos_tabla': MDTVendedorProv, 
                   'modelo_tabla': ModeloTabla, 
                   'ventana': CrudVendedoresProvDlg,     
    }, 
    INGREDIENTES_SHOW: {'clase_modelo': Ingrediente,  
                   'dao': DAOIngrediente, 
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': ModeloDatosTablaIngred, 
                   'modelo_tabla': TableModelProductIngred, #ModeloTabla, 
                   'ventana': CrudIngredienteDlg, 
    }, 
    PLANILLA_DIARIA: {'clase_modelo': Egreso,#getClaseModelo(PATH_MODELS, 'Category'), 
                   'dao': DAOSaldos, #DAOQueryAlchemy,#getClaseModelo(PATH_DAO + 'DAOCategory.', 'DAOCategory'), 
                   'modelo': Model,#getClaseModelo(PATH_CRUD_MODELO, 'Model'),
                   'modelo_datos_tabla': None, #ModeloDatosTablaEgreso,#getClaseModelo(PATH_CRUD_MODELO_DATOS_TABLA + 'mdtCategory.', 
                                                        #'ModeloDatosTablaCategory'),
                   'modelo_tabla': TableModelSaldoDiario,#ModeloTabla,#getClaseModelo(PATH_CRUD_MODELO_TABLA, 'ModeloTabla'),
                   'ventana': SaldoDiarioDlg,#getClaseModelo(PATH_CRUD + 'crudCategoryDlg.', 'CrudCategoryDlg')
    },
    RESUMEN_FISCAL: {'clase_modelo': ResumenFiscal,  
                   'dao': DAOResumenFiscal, 
                   'modelo': Model, 
                   'modelo_datos_tabla': None, 
                   'modelo_tabla': TableModelResumenFiscal, 
                   'ventana': ResumenFiscalDlg, 
    },
    VENTA_DIARIA: {'clase_modelo': Venta, #MovVentaProd,  
                   'dao': DAOVenta, #DAOMovVentaProd, 
                   'modelo': Model, 
                   'modelo_datos_tabla': None, 
                   'modelo_tabla': ModeloVentaDiaria, #TMVentaDiariaVariedades, 
                   'ventana': VentaDiariaDlg, 
    }, 
    COSTOS_PROD: {'clase_modelo': Ingrediente, 
                   'dao': DAOCostosProd, 
                   'modelo': Model, 
                   'modelo_datos_tabla': None, 
                   'modelo_tabla': TableModelCostosProd, 
                   'ventana': CostoProduccionDlg, 
    }, 
    REP_PLANILLA_DIARIA: {'clase_modelo': SaldoDiario, 
                   'dao': DAOSaldos, 
                   'modelo': ModeloReportesSaldos, #ModeloGenBusqueda, 
                   'modelo_datos_tabla': MDTInformeSaldoSemanal, 
                   'modelo_tabla': TableReporteSaldoDiario, #TableModelCostosProd, 
                   'ventana': InformesSaldoDlg, 
    }, 
}

DICT_LIST_CLASES_SEARCH = {
    SEARCH_PROD : {'clase_modelo': Product,
                   'dao': DAOProducto,  
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': ModeloDatosTablaProduct, 
                   'modelo_tabla': ModeloTablaBusqueda, 
                   'ventana': BusquedaProductoDlg, 
    }, 
    SEARCH_VENDEDOR : {'clase_modelo': Vendedor,
                   'dao': DAOVendedor,  
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': ModeloDatosTablaVendedor, 
                   'modelo_tabla': ModeloTablaBusqueda, 
                   'ventana': BusquedaVendedorDlg, 
    },
    SEARCH_EGRESO : {'clase_modelo': Egreso,
                   'dao': DAOEgreso,  
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': ModeloDatosTablaEgreso, 
                   'modelo_tabla': ModeloTablaBusqueda, 
                   'ventana': BusquedaEgresoDlg, 
    }, 
    SEARCH_PROVEEDORES : {'clase_modelo': Proveedor,
                   'dao': DAOProveedor,  
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': ModeloDatosTablaProveedor, 
                   'modelo_tabla': ModeloTablaBusqueda, 
                   'ventana': BusquedaProveedorDlg, 
    }, 
    SEARCH_CIUDAD : {'clase_modelo': Ciudad,
                   'dao': DAOCiudad,  
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': ModeloDatosTablaCiudad, 
                   'modelo_tabla': ModeloTablaBusqueda, 
                   'ventana': BusquedaCiudadDlg, 
    }, 
    SEARCH_INGREDIENTE: {'clase_modelo': Ingrediente,
                   'dao': DAOIngrediente,  
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': ModeloDatosTablaIngred, 
                   'modelo_tabla': ModeloTablaBusqueda, 
                   'ventana': BusquedaVendedorDlg, 
    }, 
    SEARCH_VENDEDOR_PROV: {'clase_modelo': VendedorProv,
                   'dao': DAOVendedorProv,  
                   'modelo': ModeloGenBusqueda, 
                   'modelo_datos_tabla': MDTBusquedaVendedorProv, 
                   'modelo_tabla': ModeloTablaBusqueda, 
                   'ventana': BusquedaVendedorDlg, 
    }
}

def getDicConfigClases(tipo):
    return DIC_LIST_CLASES.get(tipo)

def getDicConfigClasesSearch(tipo):
    return DICT_LIST_CLASES_SEARCH.get(tipo)