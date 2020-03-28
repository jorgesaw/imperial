# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgVentaDiaria.ui'
#
# Created: Thu Jul 16 19:06:14 2015
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

class Ui_DlgVentaDiaria(object):
    def setupUi(self, DlgVentaDiaria):
        DlgVentaDiaria.setObjectName(_fromUtf8("DlgVentaDiaria"))
        DlgVentaDiaria.resize(650, 439)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DlgVentaDiaria)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fechaLabel_2 = QtGui.QLabel(DlgVentaDiaria)
        self.fechaLabel_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 161, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Sans\";"))
        self.fechaLabel_2.setObjectName(_fromUtf8("fechaLabel_2"))
        self.horizontalLayout_2.addWidget(self.fechaLabel_2)
        self.lblTotVarios = QtGui.QLabel(DlgVentaDiaria)
        self.lblTotVarios.setStyleSheet(_fromUtf8("background-color: rgb(0, 161, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Sans\";"))
        self.lblTotVarios.setObjectName(_fromUtf8("lblTotVarios"))
        self.horizontalLayout_2.addWidget(self.lblTotVarios)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtGui.QLabel(DlgVentaDiaria)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.vendedoresComboBox = QtGui.QComboBox(DlgVentaDiaria)
        self.vendedoresComboBox.setObjectName(_fromUtf8("vendedoresComboBox"))
        self.horizontalLayout_2.addWidget(self.vendedoresComboBox)
        self.fechaLabel = QtGui.QLabel(DlgVentaDiaria)
        self.fechaLabel.setObjectName(_fromUtf8("fechaLabel"))
        self.horizontalLayout_2.addWidget(self.fechaLabel)
        self.fechaDateEdit = QtGui.QDateEdit(DlgVentaDiaria)
        self.fechaDateEdit.setCalendarPopup(True)
        self.fechaDateEdit.setObjectName(_fromUtf8("fechaDateEdit"))
        self.horizontalLayout_2.addWidget(self.fechaDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(DlgVentaDiaria)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.ventaVariosTableView = QtGui.QTableView(DlgVentaDiaria)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ventaVariosTableView.sizePolicy().hasHeightForWidth())
        self.ventaVariosTableView.setSizePolicy(sizePolicy)
        self.ventaVariosTableView.setFrameShadow(QtGui.QFrame.Sunken)
        self.ventaVariosTableView.setLineWidth(1)
        self.ventaVariosTableView.setObjectName(_fromUtf8("ventaVariosTableView"))
        self.ventaVariosTableView.horizontalHeader().setSortIndicatorShown(False)
        self.ventaVariosTableView.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.ventaVariosTableView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(DlgVentaDiaria)
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 161, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Sans\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lblTotPan = QtGui.QLabel(DlgVentaDiaria)
        self.lblTotPan.setStyleSheet(_fromUtf8("background-color: rgb(0, 161, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Sans\";"))
        self.lblTotPan.setObjectName(_fromUtf8("lblTotPan"))
        self.horizontalLayout_4.addWidget(self.lblTotPan)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.ventaPanesTableView = QtGui.QTableView(DlgVentaDiaria)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ventaPanesTableView.sizePolicy().hasHeightForWidth())
        self.ventaPanesTableView.setSizePolicy(sizePolicy)
        self.ventaPanesTableView.setFrameShadow(QtGui.QFrame.Sunken)
        self.ventaPanesTableView.setLineWidth(1)
        self.ventaPanesTableView.setObjectName(_fromUtf8("ventaPanesTableView"))
        self.ventaPanesTableView.horizontalHeader().setSortIndicatorShown(False)
        self.verticalLayout_2.addWidget(self.ventaPanesTableView)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fechaLabel_3 = QtGui.QLabel(DlgVentaDiaria)
        self.fechaLabel_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 161, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Sans\";"))
        self.fechaLabel_3.setObjectName(_fromUtf8("fechaLabel_3"))
        self.horizontalLayout_3.addWidget(self.fechaLabel_3)
        self.lblTotal = QtGui.QLabel(DlgVentaDiaria)
        self.lblTotal.setStyleSheet(_fromUtf8("background-color: rgb(0, 161, 118);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Lucida Sans\";"))
        self.lblTotal.setObjectName(_fromUtf8("lblTotal"))
        self.horizontalLayout_3.addWidget(self.lblTotal)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButtonImprimir = QtGui.QPushButton(DlgVentaDiaria)
        self.pushButtonImprimir.setObjectName(_fromUtf8("pushButtonImprimir"))
        self.horizontalLayout_3.addWidget(self.pushButtonImprimir)
        self.line = QtGui.QFrame(DlgVentaDiaria)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.guardarPushButton = QtGui.QPushButton(DlgVentaDiaria)
        self.guardarPushButton.setObjectName(_fromUtf8("guardarPushButton"))
        self.horizontalLayout_3.addWidget(self.guardarPushButton)
        self.cerrarPushButton = QtGui.QPushButton(DlgVentaDiaria)
        self.cerrarPushButton.setObjectName(_fromUtf8("cerrarPushButton"))
        self.horizontalLayout_3.addWidget(self.cerrarPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.fechaLabel_2.setBuddy(self.fechaDateEdit)
        self.fechaLabel.setBuddy(self.fechaDateEdit)
        self.fechaLabel_3.setBuddy(self.fechaDateEdit)

        self.retranslateUi(DlgVentaDiaria)
        QtCore.QObject.connect(self.cerrarPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgVentaDiaria.accept)
        QtCore.QMetaObject.connectSlotsByName(DlgVentaDiaria)
        DlgVentaDiaria.setTabOrder(self.fechaDateEdit, self.ventaVariosTableView)

    def retranslateUi(self, DlgVentaDiaria):
        DlgVentaDiaria.setWindowTitle(_translate("DlgVentaDiaria", "Venta diaria", None))
        self.fechaLabel_2.setText(_translate("DlgVentaDiaria", "&Venta Varios:", None))
        self.lblTotVarios.setText(_translate("DlgVentaDiaria", "0.0", None))
        self.label.setText(_translate("DlgVentaDiaria", "Vendedor:", None))
        self.fechaLabel.setText(_translate("DlgVentaDiaria", "&Fecha:", None))
        self.fechaDateEdit.setDisplayFormat(_translate("DlgVentaDiaria", "dd-MM-yyyy", None))
        self.label_4.setText(_translate("DlgVentaDiaria", "Venta Pan:", None))
        self.lblTotPan.setText(_translate("DlgVentaDiaria", "0.0", None))
        self.fechaLabel_3.setText(_translate("DlgVentaDiaria", "Total Ventas", None))
        self.lblTotal.setText(_translate("DlgVentaDiaria", "0.0", None))
        self.pushButtonImprimir.setText(_translate("DlgVentaDiaria", "&Imprimir", None))
        self.guardarPushButton.setText(_translate("DlgVentaDiaria", "&Grabar cambios", None))
        self.cerrarPushButton.setText(_translate("DlgVentaDiaria", "&Cerrar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgVentaDiaria = QtGui.QDialog()
    ui = Ui_DlgVentaDiaria()
    ui.setupUi(DlgVentaDiaria)
    DlgVentaDiaria.show()
    sys.exit(app.exec_())

