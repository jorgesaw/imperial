# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgCrud.ui'
#
# Created: Fri Apr 03 04:06:14 2015
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

class Ui_DlgCrud(object):
    def setupUi(self, DlgCrud):
        DlgCrud.setObjectName(_fromUtf8("DlgCrud"))
        DlgCrud.resize(679, 439)
        self.verticalLayout = QtGui.QVBoxLayout(DlgCrud)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ciudadesLabel = QtGui.QLabel(DlgCrud)
        self.ciudadesLabel.setObjectName(_fromUtf8("ciudadesLabel"))
        self.gridLayout.addWidget(self.ciudadesLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(488, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.listPushButton = QtGui.QPushButton(DlgCrud)
        self.listPushButton.setObjectName(_fromUtf8("listPushButton"))
        self.gridLayout.addWidget(self.listPushButton, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.datosTableView = QtGui.QTableView(DlgCrud)
        self.datosTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.datosTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.datosTableView.setSortingEnabled(True)
        self.datosTableView.setObjectName(_fromUtf8("datosTableView"))
        self.gridLayout_2.addWidget(self.datosTableView, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(DlgCrud)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line = QtGui.QFrame(DlgCrud)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.buscarLineEdit = QtGui.QLineEdit(DlgCrud)
        self.buscarLineEdit.setMaxLength(13)
        self.buscarLineEdit.setObjectName(_fromUtf8("buscarLineEdit"))
        self.horizontalLayout_3.addWidget(self.buscarLineEdit)
        self.searchPushButton = QtGui.QPushButton(DlgCrud)
        self.searchPushButton.setStyleSheet(_fromUtf8(""))
        self.searchPushButton.setObjectName(_fromUtf8("searchPushButton"))
        self.horizontalLayout_3.addWidget(self.searchPushButton)
        self.line_3 = QtGui.QFrame(DlgCrud)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_3.addWidget(self.line_3)
        self.delPushButton = QtGui.QPushButton(DlgCrud)
        self.delPushButton.setObjectName(_fromUtf8("delPushButton"))
        self.horizontalLayout_3.addWidget(self.delPushButton)
        spacerItem1 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.editPushButton = QtGui.QPushButton(DlgCrud)
        self.editPushButton.setObjectName(_fromUtf8("editPushButton"))
        self.horizontalLayout_3.addWidget(self.editPushButton)
        spacerItem2 = QtGui.QSpacerItem(158, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.newPushButton = QtGui.QPushButton(DlgCrud)
        self.newPushButton.setObjectName(_fromUtf8("newPushButton"))
        self.horizontalLayout_3.addWidget(self.newPushButton)
        spacerItem3 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.quitPushButton = QtGui.QPushButton(DlgCrud)
        self.quitPushButton.setObjectName(_fromUtf8("quitPushButton"))
        self.horizontalLayout_3.addWidget(self.quitPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.ciudadesLabel.setBuddy(self.datosTableView)

        self.retranslateUi(DlgCrud)
        QtCore.QObject.connect(self.buscarLineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.searchPushButton.click)
        QtCore.QMetaObject.connectSlotsByName(DlgCrud)
        DlgCrud.setTabOrder(self.listPushButton, self.datosTableView)
        DlgCrud.setTabOrder(self.datosTableView, self.buscarLineEdit)
        DlgCrud.setTabOrder(self.buscarLineEdit, self.searchPushButton)
        DlgCrud.setTabOrder(self.searchPushButton, self.delPushButton)
        DlgCrud.setTabOrder(self.delPushButton, self.editPushButton)
        DlgCrud.setTabOrder(self.editPushButton, self.newPushButton)
        DlgCrud.setTabOrder(self.newPushButton, self.quitPushButton)

    def retranslateUi(self, DlgCrud):
        DlgCrud.setWindowTitle(_translate("DlgCrud", "Dialog", None))
        self.ciudadesLabel.setText(_translate("DlgCrud", "Ciudades", None))
        self.listPushButton.setText(_translate("DlgCrud", "&Listar", None))
        self.buscarLineEdit.setPlaceholderText(_translate("DlgCrud", "Buscar...", None))
        self.searchPushButton.setText(_translate("DlgCrud", "Buscar", None))
        self.delPushButton.setText(_translate("DlgCrud", "&Eliminar", None))
        self.editPushButton.setText(_translate("DlgCrud", "&Actualizar", None))
        self.newPushButton.setText(_translate("DlgCrud", "&Nuevo", None))
        self.quitPushButton.setText(_translate("DlgCrud", "&Cerrar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgCrud = QtGui.QDialog()
    ui = Ui_DlgCrud()
    ui.setupUi(DlgCrud)
    DlgCrud.show()
    sys.exit(app.exec_())

