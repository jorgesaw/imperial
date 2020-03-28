# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgResumenFiscal.ui'
#
# Created: Wed Jul 22 15:13:49 2015
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

class Ui_DlgResumenFiscal(object):
    def setupUi(self, DlgResumenFiscal):
        DlgResumenFiscal.setObjectName(_fromUtf8("DlgResumenFiscal"))
        DlgResumenFiscal.resize(650, 414)
        self.verticalLayout = QtGui.QVBoxLayout(DlgResumenFiscal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fechaLabel = QtGui.QLabel(DlgResumenFiscal)
        self.fechaLabel.setObjectName(_fromUtf8("fechaLabel"))
        self.horizontalLayout_2.addWidget(self.fechaLabel)
        self.fechaDateEdit = QtGui.QDateEdit(DlgResumenFiscal)
        self.fechaDateEdit.setCalendarPopup(True)
        self.fechaDateEdit.setObjectName(_fromUtf8("fechaDateEdit"))
        self.horizontalLayout_2.addWidget(self.fechaDateEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(DlgResumenFiscal)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.resumenTableView = QtGui.QTableView(DlgResumenFiscal)
        self.resumenTableView.setObjectName(_fromUtf8("resumenTableView"))
        self.verticalLayout_2.addWidget(self.resumenTableView)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.resumenPushButton = QtGui.QPushButton(DlgResumenFiscal)
        self.resumenPushButton.setObjectName(_fromUtf8("resumenPushButton"))
        self.horizontalLayout.addWidget(self.resumenPushButton)
        self.resumenBlancoPushButton = QtGui.QPushButton(DlgResumenFiscal)
        self.resumenBlancoPushButton.setObjectName(_fromUtf8("resumenBlancoPushButton"))
        self.horizontalLayout.addWidget(self.resumenBlancoPushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.guardarPushButton = QtGui.QPushButton(DlgResumenFiscal)
        self.guardarPushButton.setObjectName(_fromUtf8("guardarPushButton"))
        self.horizontalLayout.addWidget(self.guardarPushButton)
        self.cerrarPushButton = QtGui.QPushButton(DlgResumenFiscal)
        self.cerrarPushButton.setObjectName(_fromUtf8("cerrarPushButton"))
        self.horizontalLayout.addWidget(self.cerrarPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fechaLabel.setBuddy(self.fechaDateEdit)

        self.retranslateUi(DlgResumenFiscal)
        QtCore.QObject.connect(self.cerrarPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgResumenFiscal.accept)
        QtCore.QMetaObject.connectSlotsByName(DlgResumenFiscal)
        DlgResumenFiscal.setTabOrder(self.fechaDateEdit, self.resumenTableView)

    def retranslateUi(self, DlgResumenFiscal):
        DlgResumenFiscal.setWindowTitle(_translate("DlgResumenFiscal", "Resumen Fiscal", None))
        self.fechaLabel.setText(_translate("DlgResumenFiscal", "&Fecha:", None))
        self.fechaDateEdit.setDisplayFormat(_translate("DlgResumenFiscal", "MM-yyyy", None))
        self.resumenPushButton.setText(_translate("DlgResumenFiscal", "Imprimir Resumen", None))
        self.resumenBlancoPushButton.setText(_translate("DlgResumenFiscal", "Resumen en blanco", None))
        self.guardarPushButton.setText(_translate("DlgResumenFiscal", "&Grabar cambios", None))
        self.cerrarPushButton.setText(_translate("DlgResumenFiscal", "&Cerrar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgResumenFiscal = QtGui.QDialog()
    ui = Ui_DlgResumenFiscal()
    ui.setupUi(DlgResumenFiscal)
    DlgResumenFiscal.show()
    sys.exit(app.exec_())

