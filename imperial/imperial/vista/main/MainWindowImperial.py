#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 03/04/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.factoria.factoriaVentanas import FactoriaVentanas
from imperial.core.gui.Actions import createAction
from imperial.core.gui.MsgBox import MsgBox
from imperial.model.database.DataBase import DataBase
from imperial.util import variables
from imperial.vista.gui.dlg.ProgressFileDlg import ProgressFileDlg
from imperial.vista.main import config_main
from imperial.vista.main.ui_mainWindow import Ui_MainWindow
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import datetime
import logging
logger = logging.getLogger(__name__)

class MainWindowImperial(_qg.QMainWindow, Ui_MainWindow):
    u"""Diálogo para control de stock de productos."""
    
    def __init__(self, app, parent=None):
        super(MainWindowImperial, self).__init__(parent)
        
        self.css = """
QToolButton:hover{background:n #FF00FF}
QToolBar:hover{background:n #FF00FF}
"""
        
        # Crea SIGNAL-SLOTS para conectar widgets del formulario con métodos de nuestra subclase.
        self.setupUi(self)
        
        self.app = app
        
        self.mdiArea.setBackground(_qg.QColor(79, 136, 63))
        self.mdiArea.setAutoFillBackground(False)
        self.setCentralWidget(self.mdiArea)
        
        self.createActions()
        self.createStatusBar()
        self.createToolBar()
        
    def createToolBar(self):
        #self.toolBar.setAutoFillBackground(True)
        #self.toolBar.setBackgroundRole(_qg.QPalette.Highlight)
        #self.toolBar.setStyleSheet(self.css)
        self.toolBar.setToolButtonStyle(_qc.Qt.ToolButtonTextUnderIcon)
        
        left_spacer = _qg.QWidget()
        left_spacer.setSizePolicy(_qg.QSizePolicy.Expanding, _qg.QSizePolicy.Expanding)
        right_spacer = _qg.QWidget()
        right_spacer.setSizePolicy(_qg.QSizePolicy.Expanding, _qg.QSizePolicy.Expanding)
        
        self.toolBar.addWidget(left_spacer)
        self.toolBar.addActions([self.ventasPlanillaDiariaAction, 
                               self.ventasVentasDiariasAction, 
                               self.ventasResumenFiscalAction, 
                               self.costosProdAction_2, 
                               self.tablaProductosAction, 
                               self.tablaIngredientesAction])
        self.toolBar.addWidget(right_spacer)
        
    def createStatusBar(self):
        self.sizeLabel = _qg.QLabel("")
        self.sizeLabel = _qg.QLabel(datetime.date.today().strftime('%d-%m-%Y'))
        self.sizeLabel.setFrameStyle(_qg.QFrame.StyledPanel|_qg.QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Comenzar", 5000)
        
    def createActions(self):
        #uEl orden de las aciones son determina por las constantes del paquete factoria.
        #u factoria.APP_EXIT = 0
        
        self.connect(self.fileResguardarAction, _qc.SIGNAL("triggered()"), self.resguardarDB)
        self.connect(self.fileResguardarEnAction, _qc.SIGNAL("triggered()"), self.resguardarDBEn)
        self.connect(self.fileRestaurarAction, _qc.SIGNAL("triggered()"), self.restaurarDB)
        self.fileResguardarAction.setStatusTip('Resguardar')
        self.fileResguardarEnAction.setStatusTip('Resguardar en...')
        self.fileRestaurarAction.setStatusTip('Restaurar')
        
        self.ventasPlanillaDiariaAction.setIcon(_qg.QIcon(variables.ICON_PATH_PLANILLA))
        self.ventasPlanillaDiariaAction.setStatusTip(u'Planilla diaria')
        self.ventasPlanillaDiariaAction.setIconText(u'PLANILLA DIARIA')
        
        self.ventasVentasDiariasAction.setIcon(_qg.QIcon(variables.ICON_PATH_VENTAS))
        self.ventasVentasDiariasAction.setStatusTip(u'Venta diaria')
        self.ventasVentasDiariasAction.setIconText(u'VENTA DIARIA')
        
        self.ventasResumenFiscalAction.setIcon(_qg.QIcon(variables.ICON_PATH_RESUMEN))
        self.ventasResumenFiscalAction.setStatusTip(u'Resumen Fiscal')
        self.ventasResumenFiscalAction.setIconText(u'RESUMEN FISCAL')
        
        self.costosProdAction_2.setIcon(_qg.QIcon(variables.ICON_PATH_COSTOS))
        self.costosProdAction_2.setStatusTip(u'Costos')
        self.costosProdAction_2.setIconText(u'COSTOS')
        
        self.tablaProductosAction.setIcon(_qg.QIcon(variables.ICON_PATH_PRODUCTOS))
        self.tablaProductosAction.setStatusTip(u'Productos')
        self.tablaProductosAction.setIconText(u'PRODUCTOS')
        
        self.tablaIngredientesAction.setIcon(_qg.QIcon(variables.ICON_PATH_INGREDIENTES))
        self.tablaIngredientesAction.setStatusTip(u'Ingredientes')
        self.tablaIngredientesAction.setIconText(u'INGREDIENTES')
        
        lstActions = [self.fileSalirAction, 
                      
                      self.tablaProductosAction, self.tablaVentasAction, 
                      self.tablaEgresosAction, self.tablaProveedoresAction, 
                      self.tablaVendedoresProvAction, self.tablaIngredientesAction, 
                      
                      self.ventasPlanillaDiariaAction, self.ventasVentasDiariasAction, 
                      self.ventasResumenFiscalAction, self.costosProdAction_2, 
                      
                      self.repPlanillaDiariaAction, self.repVentaDiariaAction, 
                      
                      self.saldoDiarioAction,
                      ]
        
        lstSlot = [self.close,]
        size = len(lstSlot)
        for i in range(len(lstActions) - size):
            lstSlot.append(self.searchWindow)
        
        self.matrizActions = config_main.getActions(self, lstActions, lstSlot)
        #print(self.matrizActions)
        
    def searchWindow(self):
        sender = self.sender().data().toInt()[0]
        #print('SENDER:', sender)
        maximized= False
        focus=True
        self.loadWindow(sender, maximized, focus)
        
    def loadWindow(self, wnd, maximized=False, focus=False):
        gui = FactoriaVentanas.crearVentanaGui(wnd, parent=self.mdiArea)
        #if not self.app.isWindowActived(gui.tipo()):
        dlg = gui.prepararVentana()
        if dlg:
            if not self.app.isWindowActived(type(dlg)):
                _qg.QApplication.setOverrideCursor(_qg.QCursor(_qc.Qt.WaitCursor))
                self.app.showWindow(dlg)
                _qg.QApplication.restoreOverrideCursor()
                if focus:
                    dlg.setFocus()
                if maximized:
                    dlg.showMaximized()
                    
    def resguardarDBEn(self):
        dir_bck = _qg.QFileDialog.getExistingDirectory(self, 'Seleccionar directorio')
        db = DataBase(ProgressFileDlg())
        db.resguardarDbEn(dir_bck)
    
    def resguardarDB(self):
        vista = ProgressFileDlg()
        db = DataBase(vista)
        db.resguardarDb()
        
    def restaurarDB(self):
        vista = ProgressFileDlg()
        vista.msgLabel.setText('Restaurando base de datos...')
        db = DataBase(vista)
        db.restaurarDb()
        
    def closeEvent(self, event):
        #uTambién guardamos la geometria(tamaño) de la ventana de la app.
        if MsgBox.okToContinue(self):
            settings = _qc.QSettings()
            settings.setValue("MainWindow/Size", _qc.QVariant(self.size()))
            settings.setValue("MainWindow/Position", _qc.QVariant(self.pos()))
            settings.setValue("MainWindow/State", _qc.QVariant(self.saveState()))
            #settings.setValue("Geometry", QVariant(self.saveGeometry()))
            logging.info(u'Cerrando la aplicación...')
            event.accept()
        else:
            event.ignore()