# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgInformesSaldos.ui'
#
# Created: Mon Jun 01 00:31:17 2015
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

class Ui_DlgInformesSaldos(object):
    def setupUi(self, DlgInformesSaldos):
        DlgInformesSaldos.setObjectName(_fromUtf8("DlgInformesSaldos"))
        DlgInformesSaldos.resize(612, 442)
        self.verticalLayout_5 = QtGui.QVBoxLayout(DlgInformesSaldos)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tabInformes = QtGui.QTabWidget(DlgInformesSaldos)
        self.tabInformes.setTabPosition(QtGui.QTabWidget.North)
        self.tabInformes.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabInformes.setElideMode(QtCore.Qt.ElideNone)
        self.tabInformes.setDocumentMode(False)
        self.tabInformes.setObjectName(_fromUtf8("tabInformes"))
        self.tabSemanal = QtGui.QWidget()
        self.tabSemanal.setObjectName(_fromUtf8("tabSemanal"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabSemanal)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.tabSemanal)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.datosSemCombo = QtGui.QComboBox(self.tabSemanal)
        self.datosSemCombo.setObjectName(_fromUtf8("datosSemCombo"))
        self.horizontalLayout.addWidget(self.datosSemCombo)
        self.label = QtGui.QLabel(self.tabSemanal)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.desdeFechaDateEdit = QtGui.QDateEdit(self.tabSemanal)
        self.desdeFechaDateEdit.setCalendarPopup(True)
        self.desdeFechaDateEdit.setObjectName(_fromUtf8("desdeFechaDateEdit"))
        self.horizontalLayout.addWidget(self.desdeFechaDateEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton = QtGui.QPushButton(self.tabSemanal)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.tabSemanal)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.semanaTableView = QtGui.QTableView(self.tabSemanal)
        self.semanaTableView.setObjectName(_fromUtf8("semanaTableView"))
        self.verticalLayout_2.addWidget(self.semanaTableView)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tabInformes.addTab(self.tabSemanal, _fromUtf8(""))
        self.tabMensual = QtGui.QWidget()
        self.tabMensual.setObjectName(_fromUtf8("tabMensual"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabMensual)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.mesFechaDateEdit = QtGui.QDateEdit(self.tabMensual)
        self.mesFechaDateEdit.setCalendarPopup(True)
        self.mesFechaDateEdit.setObjectName(_fromUtf8("mesFechaDateEdit"))
        self.horizontalLayout_3.addWidget(self.mesFechaDateEdit)
        self.datosMesCombo = QtGui.QComboBox(self.tabMensual)
        self.datosMesCombo.setObjectName(_fromUtf8("datosMesCombo"))
        self.horizontalLayout_3.addWidget(self.datosMesCombo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.tabMensual)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.fechaLabel_3 = QtGui.QLabel(self.tabMensual)
        self.fechaLabel_3.setObjectName(_fromUtf8("fechaLabel_3"))
        self.horizontalLayout_3.addWidget(self.fechaLabel_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.mesTableView = QtGui.QTableView(self.tabMensual)
        self.mesTableView.setObjectName(_fromUtf8("mesTableView"))
        self.verticalLayout_4.addWidget(self.mesTableView)
        self.tabInformes.addTab(self.tabMensual, _fromUtf8(""))
        self.tabPersonalizado = QtGui.QWidget()
        self.tabPersonalizado.setObjectName(_fromUtf8("tabPersonalizado"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabPersonalizado)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fechaDateEdit_4 = QtGui.QDateEdit(self.tabPersonalizado)
        self.fechaDateEdit_4.setCalendarPopup(True)
        self.fechaDateEdit_4.setObjectName(_fromUtf8("fechaDateEdit_4"))
        self.horizontalLayout_4.addWidget(self.fechaDateEdit_4)
        self.datosPerCombo = QtGui.QComboBox(self.tabPersonalizado)
        self.datosPerCombo.setObjectName(_fromUtf8("datosPerCombo"))
        self.horizontalLayout_4.addWidget(self.datosPerCombo)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.tabPersonalizado)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.fechaLabel_4 = QtGui.QLabel(self.tabPersonalizado)
        self.fechaLabel_4.setObjectName(_fromUtf8("fechaLabel_4"))
        self.horizontalLayout_4.addWidget(self.fechaLabel_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.personalizadoTableView = QtGui.QTableView(self.tabPersonalizado)
        self.personalizadoTableView.setObjectName(_fromUtf8("personalizadoTableView"))
        self.verticalLayout.addWidget(self.personalizadoTableView)
        self.tabInformes.addTab(self.tabPersonalizado, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabInformes)

        self.retranslateUi(DlgInformesSaldos)
        self.tabInformes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DlgInformesSaldos)

    def retranslateUi(self, DlgInformesSaldos):
        DlgInformesSaldos.setWindowTitle(_translate("DlgInformesSaldos", "Dialog", None))
        self.label_5.setText(_translate("DlgInformesSaldos", "Categoria", None))
        self.label.setText(_translate("DlgInformesSaldos", "Inicio:", None))
        self.desdeFechaDateEdit.setDisplayFormat(_translate("DlgInformesSaldos", "dd-MM-yyyy", None))
        self.pushButton.setText(_translate("DlgInformesSaldos", "Imprimir", None))
        self.pushButton_2.setText(_translate("DlgInformesSaldos", "Abrir en Excel", None))
        self.tabInformes.setTabText(self.tabInformes.indexOf(self.tabSemanal), _translate("DlgInformesSaldos", "Semanal", None))
        self.mesFechaDateEdit.setDisplayFormat(_translate("DlgInformesSaldos", "dd-MM-yyyy", None))
        self.label_3.setText(_translate("DlgInformesSaldos", "Mes:", None))
        self.fechaLabel_3.setText(_translate("DlgInformesSaldos", "FECHA", None))
        self.tabInformes.setTabText(self.tabInformes.indexOf(self.tabMensual), _translate("DlgInformesSaldos", "Mensual", None))
        self.fechaDateEdit_4.setDisplayFormat(_translate("DlgInformesSaldos", "dd-MM-yyyy", None))
        self.label_4.setText(_translate("DlgInformesSaldos", "Fecha:", None))
        self.fechaLabel_4.setText(_translate("DlgInformesSaldos", "FECHA", None))
        self.tabInformes.setTabText(self.tabInformes.indexOf(self.tabPersonalizado), _translate("DlgInformesSaldos", "Personalizado", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgInformesSaldos = QtGui.QDialog()
    ui = Ui_DlgInformesSaldos()
    ui.setupUi(DlgInformesSaldos)
    DlgInformesSaldos.show()
    sys.exit(app.exec_())

