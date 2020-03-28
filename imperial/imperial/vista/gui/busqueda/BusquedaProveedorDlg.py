#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 01/05/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.vista.gui.busqueda.BusquedaGenericaDlg import BusquedaGenericaDlg
import PyQt4.QtGui as _qg

MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class BusquedaProveedorDlg(BusquedaGenericaDlg):
    u"""Diálogo para buscar proveedores."""
    
    def __init__(self, modelo, parent=None):
        super(BusquedaProveedorDlg, self).__init__(modelo, parent)
        
        self.setWindowTitle(u'Búsqueda de proveedores')
        self.busquedaLabel.setText(u'Nombre de proveedor:')
        
        


    