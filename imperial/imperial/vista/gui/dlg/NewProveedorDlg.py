#!/usr/bin/env python
# -*- coding: utf-8 -*-

from imperial.core.factoria.factoriaVentanasSearch import FactoriaVentanasSearch
from imperial.core.gui.filterF8Key import FilterF8Key
from imperial.core.gui.filterReturn import FilterReturn
from imperial.vista.gui.dlg import ui_dlgAddProveedor
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime


MAC = hasattr(_qg, "qt_mac_set_native_menubar")

class NewProveedorDlg(_qg.QDialog,
                   ui_dlgAddProveedor.Ui_DlgAddProveedor):
    u"""Diálogo para agregar los datos de un proveedor."""

    def __init__(self, modelo=None, parent=None):
        super(NewProveedorDlg, self).__init__(parent)

        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.ciudad = None
        #self.ciudadVendedor = None
        
        self.vendedor = None
        
        self.modelo = modelo        
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setText("&Agregar")
        self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setText("&Cancelar")

        filterCiudad = FilterF8Key()
        self.ciudadLineEdit.setMouseTracking(True)
        self.ciudadLineEdit.installEventFilter(filterCiudad)
        self.connect(self.ciudadLineEdit, _qc.SIGNAL("f8Pressed()"), self.buscarCiudad)
        
        #filterCiudadVend = FilterF8Key()
        #self.ciudadLineEditVend.setMouseTracking(True)
        #self.ciudadLineEditVend.installEventFilter(filterCiudadVend)
        #self.connect(self.ciudadLineEditVend, _qc.SIGNAL("f8Pressed()"), 
        #            self.buscarCiudadVendedor)
        
        if not MAC: 
            self.buttonBox.button(_qg.QDialogButtonBox.Ok).setFocusPolicy(_qc.Qt.NoFocus)
            self.buttonBox.button(_qg.QDialogButtonBox.Cancel).setFocusPolicy(_qc.Qt.NoFocus)
         
        self.filterReturn = FilterReturn()       
        self.emailLineEdit.installEventFilter(self.filterReturn)
        self.connect(self.emailLineEdit, _qc.SIGNAL("enterPressed()"), 
                     self.selectAceptar)
        
        self.updateUi()
        
    def selectAceptar(self):
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setDefault(True)
        
    def buscarCiudad(self):
        from imperial.vista import factoria
        busqueda = FactoriaVentanasSearch.crearVentanaGui(factoria.SEARCH_CIUDAD, self, 
              {'carga_previa': False})
        ciudad = busqueda.datoBuscado()
        
        if ciudad:
            self.ciudad = ciudad
            self.ciudadLineEdit.setText(self.ciudad.nomCiudad)
            self.provLineEdit.setText(self.ciudad.provincia.nombre)
            self.updateUi()
            for line in (self.telefonoLineEdit, self.celularLineEdit):
                line.setText(self.ciudad.DDN + '-' + line.text())
        self.updateUi()
        self.telefonoLineEdit.setFocus()
        self.telefonoLineEdit.selectAll()
        
    def buscarVendedor(self):
        from imperial.vista import factoria
        busqueda = FactoriaVentanasSearch.crearVentanaGui(factoria.SEARCH_VENDEDOR_PROV, self, 
              {'carga_previa': False})
        vendedor = busqueda.datoBuscado()
        
        if vendedor:
            self.vendedor = vendedor
            self.vendedorLineEdit.setText(self.vendedor.nombre)
        
    #def buscarCiudadVendedor(self):
    #    from imperial.vista import factoria
    #    busqueda = FactoriaVentanasSearch.crearVentanaGui(factoria.SEARCH_CIUDAD, self, 
    #          {'carga_previa': False})
    #    ciudad = busqueda.datoBuscado()
    #    
    #    if ciudad:
    #        self.ciudadVendedor = ciudad
    #        self.ciudadLineEditVend.setText(self.ciudadVendedor.nomCiudad)
    #        self.provLineEditVend.setText(self.ciudadVendedor.provincia.nombre)
    #        self.updateUi()
    #       for line in (self.telefonoLineEditVend, self.celularLineEditVend):
    #            line.setText(self.ciudadVendedor.DDN + '-' + line.text())
    #    self.updateUi()
    #   self.telefonoLineEditVend.setFocus()
    #   self.telefonoLineEditVend.selectAll()
        
    @_qc.pyqtSlot("QString")
    def on_nombreLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_aliasLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_categoriaLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_direccionLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_alturaLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_pisoLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_deptoLineEdit_textEdited(self, text):
        self.updateUi()
        
    @_qc.pyqtSlot("QString")
    def on_barrioLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_telefonoLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot("QString")
    def on_celularLineEdit_textEdited(self, text):
        self.updateUi()
    
    @_qc.pyqtSlot("QString")
    def on_emailLineEdit_textEdited(self, text):
        self.updateUi()

    @_qc.pyqtSlot()
    def on_ciudadPushButton_clicked(self):
        self.buscarCiudad()
        
    @_qc.pyqtSlot()
    def on_vendedorPushButton_clicked(self):
        self.buscarVendedor()
    
    #@_qc.pyqtSlot()
    #def on_ciudadPushButtonVend_clicked(self):
    #    self.buscarCiudadVendedor()
        
    def data(self):
        lstDatosProv = [unicode(self.nombreLineEdit.text()), unicode(self.emailLineEdit.text()),  
                unicode(self.direccionLineEdit.text()), unicode(self.barrioLineEdit.text()),
                self.ciudad,
                unicode(self.telefonoLineEdit.text()), unicode(self.celularLineEdit.text()),
                unicode(self.alturaLineEdit.text()), unicode(self.pisoLineEdit.text()),
                unicode(self.deptoLineEdit.text()), None, 
                datetime.date.today(), self.vendedor]
        
        #lstDatosVendedorProv = [unicode(self.nombreLineEditVend.text()), unicode(self.emailLineEditVend.text()),  
        #        unicode(self.direccionLineEditVend.text()), unicode(self.barrioLineEditVend.text()),
        #        self.ciudadVendedor, None,
        #        unicode(self.telefonoLineEditVend.text()), unicode(self.celularLineEditVend.text()),
        #        unicode(self.alturaLineEditVend.text()), unicode(self.pisoLineEditVend.text()),
        #        unicode(self.deptoLineEditVend.text())]
        return lstDatosProv #[lstDatosProv, lstDatosVendedorProv]
    
    def resetValues(self):
        self.nombreLineEdit.clear()
        self.direccionLineEdit.clear()
        self.alturaLineEdit.clear()
        self.pisoLineEdit.clear()
        self.deptoLineEdit.clear()
        self.barrioLineEdit.clear()
        self.ciudadLineEdit.clear()
        self.ciudad = None
        self.provinciaLineEdit.clear()
        self.telefonoLineEdit.clear()
        self.celularLineEdit.clear()
        self.emailLineEdit.clear()

    def updateUi(self):
        enable = not (self.nombreLineEdit.text().isEmpty() 
                      or \
                      self.direccionLineEdit.text().isEmpty() or \
                      self.alturaLineEdit.text().isEmpty() or self.telefonoLineEdit.text().isEmpty() or \
                      self.barrioLineEdit.text().isEmpty() or \
                      self.celularLineEdit.text().isEmpty() or self.ciudad is None
                      )
        self.buttonBox.button(_qg.QDialogButtonBox.Ok).setEnabled(enable)
