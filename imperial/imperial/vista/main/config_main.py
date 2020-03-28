#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 13/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.Actions import addActions, createAction, editAction
from imperial.vista import factoria
import PyQt4.QtCore as _qc

BCK_IMAGE = ':/fondo_abstracto.png'

MENUS = [u"&Archivo", u"&Productos", u"&Rubros", "&Informes", "&Ventas", "P&unto de venta"]

actSalir = ["&Salir", "Alt+F4", "quit.png", u"Salir de la aplicación", "triggered()"]

MATRIZ_ACTIONS_POR_MENU = [
            [
                ["&Exit", "Alt+F4", "quit.png", u"Exit the app", "triggered()"],  
        
            ], 
            [
                ["&Nuevo...", "", "article.png", u"Nuevo producto", "triggered()"], 
                ["&Mostrar", "", "", u"Mostrar productos", "triggered()"], 
                #["&Limits", "", "", u"Limits", "triggered()"]
            ],
            [
                ["&Nuevo...", "", "article.png", u"Nuevo rubro", "triggered()"], 
                ["&Mostrar", "", "", u"Mostrar rubros", "triggered()"]
            ], 
            [
                ["&Control de stock", "", "", u"Control de stock", "triggered()"],  
        
            ], 
            [
                ["&Informe de Ventas", "", "", u"Informe de Ventas", "triggered()"],  
        
            ], 
            [
                ["&Mostrar...", "", "", u"Mostrar TPV", "triggered()"],  
        
            ], 
        ]


def getActions(window, lst_var_actions, lstSlot):
    
    for action, slot, value in zip(lst_var_actions, lstSlot, factoria.LST_GENERIC_WINDOW):
        window.connect(action, _qc.SIGNAL("triggered()"), slot)
        
        action.setData(value)
    
def getMenus(window, lstMenus, matrizActions, menus=MENUS):
    for menu_string, menu_var, lstActions in zip(menus, lstMenus, matrizActions):
        menu_var = window.menuBar().addMenu(window.tr(menu_string))
        
        addActions(window, menu_var, lstActions)