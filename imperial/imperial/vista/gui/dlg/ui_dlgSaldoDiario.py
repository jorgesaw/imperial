# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgSaldoDiario.ui'
#
# Created: Thu Jul 16 15:38:17 2015
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

class Ui_DlgSaldoDiario(object):
    def setupUi(self, DlgSaldoDiario):
        DlgSaldoDiario.setObjectName(_fromUtf8("DlgSaldoDiario"))
        DlgSaldoDiario.resize(458, 418)
        self.verticalLayout = QtGui.QVBoxLayout(DlgSaldoDiario)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fechaLabel = QtGui.QLabel(DlgSaldoDiario)
        self.fechaLabel.setObjectName(_fromUtf8("fechaLabel"))
        self.horizontalLayout_2.addWidget(self.fechaLabel)
        self.fechaDateEdit = QtGui.QDateEdit(DlgSaldoDiario)
        self.fechaDateEdit.setCalendarPopup(True)
        self.fechaDateEdit.setObjectName(_fromUtf8("fechaDateEdit"))
        self.horizontalLayout_2.addWidget(self.fechaDateEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(DlgSaldoDiario)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.saldosTableView = QtGui.QTableView(DlgSaldoDiario)
        self.saldosTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.saldosTableView.setObjectName(_fromUtf8("saldosTableView"))
        self.verticalLayout_2.addWidget(self.saldosTableView)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line_3 = QtGui.QFrame(DlgSaldoDiario)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line = QtGui.QFrame(DlgSaldoDiario)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.pushButtonImprimir = QtGui.QPushButton(DlgSaldoDiario)
        self.pushButtonImprimir.setObjectName(_fromUtf8("pushButtonImprimir"))
        self.horizontalLayout.addWidget(self.pushButtonImprimir)
        self.pushButtonImprimirBlanco = QtGui.QPushButton(DlgSaldoDiario)
        self.pushButtonImprimirBlanco.setObjectName(_fromUtf8("pushButtonImprimirBlanco"))
        self.horizontalLayout.addWidget(self.pushButtonImprimirBlanco)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.guardarPushButton = QtGui.QPushButton(DlgSaldoDiario)
        self.guardarPushButton.setObjectName(_fromUtf8("guardarPushButton"))
        self.horizontalLayout.addWidget(self.guardarPushButton)
        self.cerrarPushButton = QtGui.QPushButton(DlgSaldoDiario)
        self.cerrarPushButton.setObjectName(_fromUtf8("cerrarPushButton"))
        self.horizontalLayout.addWidget(self.cerrarPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fechaLabel.setBuddy(self.fechaDateEdit)

        self.retranslateUi(DlgSaldoDiario)
        QtCore.QObject.connect(self.cerrarPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DlgSaldoDiario.accept)
        QtCore.QMetaObject.connectSlotsByName(DlgSaldoDiario)
        DlgSaldoDiario.setTabOrder(self.fechaDateEdit, self.saldosTableView)

    def retranslateUi(self, DlgSaldoDiario):
        DlgSaldoDiario.setWindowTitle(_translate("DlgSaldoDiario", "Saldo diario", None))
        self.fechaLabel.setText(_translate("DlgSaldoDiario", "&Fecha:", None))
        self.fechaDateEdit.setDisplayFormat(_translate("DlgSaldoDiario", "dd-MM-yyyy", None))
        self.pushButtonImprimir.setText(_translate("DlgSaldoDiario", "&Imprimir", None))
        self.pushButtonImprimirBlanco.setText(_translate("DlgSaldoDiario", "I&mprimir en blanco", None))
        self.guardarPushButton.setText(_translate("DlgSaldoDiario", "&Grabar cambios", None))
        self.cerrarPushButton.setText(_translate("DlgSaldoDiario", "&Cerrar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgSaldoDiario = QtGui.QDialog()
    ui = Ui_DlgSaldoDiario()
    ui.setupUi(DlgSaldoDiario)
    DlgSaldoDiario.show()
    sys.exit(app.exec_())

