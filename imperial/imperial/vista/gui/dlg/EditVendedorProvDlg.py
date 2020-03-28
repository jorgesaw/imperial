#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialogButtonBox
from imperial.model import models
import sys
from imperial.vista.gui.dlg.NewVendedorProvDlg import NewVendedorProvDlg
sys.path.append('./')


class EditVendedorProvDlg(NewVendedorProvDlg):
    u"""Diálogo para editar los datos de una institución."""

    def __init__(self, modelo=None, parent=None):
        super(EditVendedorProvDlg, self).__init__(modelo, parent)

        self.setWindowTitle(u"Editar Vendedor - Proveedor")
        self.buttonBox.button(QDialogButtonBox.Ok).setText("&Editar")
        
        self.setWindowTitle(u'Editar Vendedor - Proveedor')
        
    def setData(self, listaData):
        self.nombreLineEdit.setText(str(listaData[models.NAME_VEND_PROV]))

        self.direccionLineEdit.setText(listaData[models.DIRECCION_VEND_PROV])
        self.alturaLineEdit.setText(listaData[models.ALTURA_VEND_PROV])
        self.barrioLineEdit.setText(listaData[models.BARRIO_VEND_PROV])
        
        self.pisoLineEdit.setText(listaData[models.PISO_VEND_PROV])
        self.deptoLineEdit.setText(listaData[models.DEPTO_VEND_PROV])

        self.ciudad = listaData[models.CIUDAD_VEND_PROV]
        self.ciudadLineEdit.setText(listaData[models.CIUDAD_VEND_PROV].nomCiudad)
        self.provLineEdit.setText(str(listaData[models.PROVINCIA_VEND_PROV]))
        self.telefonoLineEdit.setText(str(listaData[models.TELEFONO_VEND_PROV]))
        self.celularLineEdit.setText(str(listaData[models.CELULAR_VEND_PROV]))
        
        if listaData[models.PROVEEDOR_VEND] and len(list(listaData[models.PROVEEDOR_VEND])) > 0:
            self.proveedor = listaData[models.PROVEEDOR_VEND][0]
            self.vendedorLineEdit.setText(listaData[models.PROVEEDOR_VEND][0].nombre)
        