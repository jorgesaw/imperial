#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialogButtonBox
from imperial.model import models
from imperial.vista.gui.dlg.NewProveedorDlg import NewProveedorDlg
import sys
sys.path.append('./')


class EditProveedorDlg(NewProveedorDlg):
    u"""Diálogo para editar los datos de una institución."""

    def __init__(self, modelo=None, parent=None):
        super(EditProveedorDlg, self).__init__(modelo, parent)

        self.setWindowTitle(u"Editar Proveedor")
        self.buttonBox.button(QDialogButtonBox.Ok).setText("&Editar")
        
        self.setWindowTitle(u'Editar Proveedor')
        
    def setData(self, listaData):
        self.nombreLineEdit.setText(str(listaData[models.NAME_PROV]))

        self.direccionLineEdit.setText(listaData[models.DIRECCION_PROV])
        self.alturaLineEdit.setText(listaData[models.ALTURA_PROV])
        self.barrioLineEdit.setText(listaData[models.BARRIO_PROV])
        
        self.pisoLineEdit.setText(listaData[models.PISO_PROV])
        self.deptoLineEdit.setText(listaData[models.DEPTO_PROV])

        self.ciudad = listaData[models.CIUDAD_PROV]
        self.ciudadLineEdit.setText(listaData[models.CIUDAD_PROV].nomCiudad)
        self.provLineEdit.setText(str(listaData[models.PROVINCIA_PROV]))
        self.telefonoLineEdit.setText(str(listaData[models.TELEFONO_PROV]))
        self.celularLineEdit.setText(str(listaData[models.CELULAR_PROV]))
        
        if listaData[models.VENDEDOR_PROV]:
            self.vendedor = listaData[models.VENDEDOR_PROV]
            self.vendedorLineEdit.setText(listaData[models.VENDEDOR_PROV].nombre)
        