# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_mainWindow.ui'
#
# Created: Wed Jul 22 23:20:36 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.verticalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet(_fromUtf8(""))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menu_Base_de_datos = QtGui.QMenu(self.menuArchivo)
        self.menu_Base_de_datos.setObjectName(_fromUtf8("menu_Base_de_datos"))
        self.menu_Tablas = QtGui.QMenu(self.menubar)
        self.menu_Tablas.setObjectName(_fromUtf8("menu_Tablas"))
        self.menu_Ventas = QtGui.QMenu(self.menubar)
        self.menu_Ventas.setObjectName(_fromUtf8("menu_Ventas"))
        self.menu_Informes = QtGui.QMenu(self.menubar)
        self.menu_Informes.setObjectName(_fromUtf8("menu_Informes"))
        self.menu_Costo = QtGui.QMenu(self.menubar)
        self.menu_Costo.setObjectName(_fromUtf8("menu_Costo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileSalirAction = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileSalirAction.setIcon(icon)
        self.fileSalirAction.setObjectName(_fromUtf8("fileSalirAction"))
        self.tablaProductosAction = QtGui.QAction(MainWindow)
        self.tablaProductosAction.setObjectName(_fromUtf8("tablaProductosAction"))
        self.tablaRubrosAction = QtGui.QAction(MainWindow)
        self.tablaRubrosAction.setObjectName(_fromUtf8("tablaRubrosAction"))
        self.action_Egresos = QtGui.QAction(MainWindow)
        self.action_Egresos.setObjectName(_fromUtf8("action_Egresos"))
        self.tablaEgresosAction = QtGui.QAction(MainWindow)
        self.tablaEgresosAction.setObjectName(_fromUtf8("tablaEgresosAction"))
        self.saldoDiarioAction = QtGui.QAction(MainWindow)
        self.saldoDiarioAction.setObjectName(_fromUtf8("saldoDiarioAction"))
        self.repPlanillaDiariaAction = QtGui.QAction(MainWindow)
        self.repPlanillaDiariaAction.setObjectName(_fromUtf8("repPlanillaDiariaAction"))
        self.repVentaDiariaAction = QtGui.QAction(MainWindow)
        self.repVentaDiariaAction.setObjectName(_fromUtf8("repVentaDiariaAction"))
        self.infVendedoresAction = QtGui.QAction(MainWindow)
        self.infVendedoresAction.setObjectName(_fromUtf8("infVendedoresAction"))
        self.infEgresosAction = QtGui.QAction(MainWindow)
        self.infEgresosAction.setObjectName(_fromUtf8("infEgresosAction"))
        self.tablaVentasAction = QtGui.QAction(MainWindow)
        self.tablaVentasAction.setObjectName(_fromUtf8("tablaVentasAction"))
        self.tablaProveedoresAction = QtGui.QAction(MainWindow)
        self.tablaProveedoresAction.setObjectName(_fromUtf8("tablaProveedoresAction"))
        self.tablaIngredientesAction = QtGui.QAction(MainWindow)
        self.tablaIngredientesAction.setObjectName(_fromUtf8("tablaIngredientesAction"))
        self.ventasPlanillaDiariaAction = QtGui.QAction(MainWindow)
        self.ventasPlanillaDiariaAction.setObjectName(_fromUtf8("ventasPlanillaDiariaAction"))
        self.ventasVentasDiariasAction = QtGui.QAction(MainWindow)
        self.ventasVentasDiariasAction.setObjectName(_fromUtf8("ventasVentasDiariasAction"))
        self.ventasResumenFiscalAction = QtGui.QAction(MainWindow)
        self.ventasResumenFiscalAction.setObjectName(_fromUtf8("ventasResumenFiscalAction"))
        self.costosProdAction = QtGui.QAction(MainWindow)
        self.costosProdAction.setObjectName(_fromUtf8("costosProdAction"))
        self.tablaVendedoresProvAction = QtGui.QAction(MainWindow)
        self.tablaVendedoresProvAction.setObjectName(_fromUtf8("tablaVendedoresProvAction"))
        self.fileResguardarAction = QtGui.QAction(MainWindow)
        self.fileResguardarAction.setObjectName(_fromUtf8("fileResguardarAction"))
        self.fileRestaurarAction = QtGui.QAction(MainWindow)
        self.fileRestaurarAction.setObjectName(_fromUtf8("fileRestaurarAction"))
        self.fileResguardarEnAction = QtGui.QAction(MainWindow)
        self.fileResguardarEnAction.setObjectName(_fromUtf8("fileResguardarEnAction"))
        self.costosProdAction_2 = QtGui.QAction(MainWindow)
        self.costosProdAction_2.setObjectName(_fromUtf8("costosProdAction_2"))
        self.menu_Base_de_datos.addAction(self.fileResguardarAction)
        self.menu_Base_de_datos.addAction(self.fileResguardarEnAction)
        self.menu_Base_de_datos.addSeparator()
        self.menu_Base_de_datos.addAction(self.fileRestaurarAction)
        self.menuArchivo.addAction(self.menu_Base_de_datos.menuAction())
        self.menuArchivo.addAction(self.fileSalirAction)
        self.menu_Tablas.addAction(self.tablaProductosAction)
        self.menu_Tablas.addSeparator()
        self.menu_Tablas.addAction(self.tablaVentasAction)
        self.menu_Tablas.addAction(self.tablaEgresosAction)
        self.menu_Tablas.addSeparator()
        self.menu_Tablas.addAction(self.tablaProveedoresAction)
        self.menu_Tablas.addAction(self.tablaVendedoresProvAction)
        self.menu_Tablas.addSeparator()
        self.menu_Tablas.addAction(self.tablaIngredientesAction)
        self.menu_Ventas.addAction(self.ventasPlanillaDiariaAction)
        self.menu_Ventas.addAction(self.ventasVentasDiariasAction)
        self.menu_Ventas.addSeparator()
        self.menu_Ventas.addAction(self.ventasResumenFiscalAction)
        self.menu_Informes.addAction(self.repPlanillaDiariaAction)
        self.menu_Informes.addAction(self.repVentaDiariaAction)
        self.menu_Informes.addSeparator()
        self.menu_Costo.addAction(self.costosProdAction_2)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menu_Tablas.menuAction())
        self.menubar.addAction(self.menu_Ventas.menuAction())
        self.menubar.addAction(self.menu_Costo.menuAction())
        self.menubar.addAction(self.menu_Informes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "..::La Imperial::..", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "&Archivo      ", None))
        self.menu_Base_de_datos.setTitle(_translate("MainWindow", "&Base de datos", None))
        self.menu_Tablas.setTitle(_translate("MainWindow", "&Tablas      ", None))
        self.menu_Ventas.setTitle(_translate("MainWindow", "&Planillas      ", None))
        self.menu_Informes.setTitle(_translate("MainWindow", "&Reportes      ", None))
        self.menu_Costo.setTitle(_translate("MainWindow", "&Costos      ", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.fileSalirAction.setText(_translate("MainWindow", "&Cerrar", None))
        self.fileSalirAction.setShortcut(_translate("MainWindow", "Alt+F4", None))
        self.tablaProductosAction.setText(_translate("MainWindow", "&Productos", None))
        self.tablaRubrosAction.setText(_translate("MainWindow", "&Rubros", None))
        self.action_Egresos.setText(_translate("MainWindow", "&Egresos", None))
        self.tablaEgresosAction.setText(_translate("MainWindow", "&Egresos", None))
        self.saldoDiarioAction.setText(_translate("MainWindow", "S&aldo diario", None))
        self.repPlanillaDiariaAction.setText(_translate("MainWindow", "&Planilla diaria", None))
        self.repVentaDiariaAction.setText(_translate("MainWindow", "&Venta diaria", None))
        self.infVendedoresAction.setText(_translate("MainWindow", "V&endedores", None))
        self.infEgresosAction.setText(_translate("MainWindow", "&Egresos", None))
        self.tablaVentasAction.setText(_translate("MainWindow", "&Ventas", None))
        self.tablaProveedoresAction.setText(_translate("MainWindow", "&Proveedores", None))
        self.tablaIngredientesAction.setText(_translate("MainWindow", "&Ingredientes", None))
        self.ventasPlanillaDiariaAction.setText(_translate("MainWindow", "&Planilla diaria", None))
        self.ventasVentasDiariasAction.setText(_translate("MainWindow", "&Ventas diarias", None))
        self.ventasResumenFiscalAction.setText(_translate("MainWindow", "&Resumen fiscal", None))
        self.costosProdAction.setText(_translate("MainWindow", "Costos...", None))
        self.tablaVendedoresProvAction.setText(_translate("MainWindow", "Vendedores Prov", None))
        self.fileResguardarAction.setText(_translate("MainWindow", "&Resguardar", None))
        self.fileRestaurarAction.setText(_translate("MainWindow", "R&estaurar", None))
        self.fileResguardarEnAction.setText(_translate("MainWindow", "Resguardar en...", None))
        self.costosProdAction_2.setText(_translate("MainWindow", "Ver...      ", None))

import qrc_main_window

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

