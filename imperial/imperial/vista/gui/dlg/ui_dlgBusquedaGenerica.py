# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgBusquedaGenerica.ui'
#
# Created: Fri May 01 17:54:30 2015
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

class Ui_DlgBusquedaGenerica(object):
    def setupUi(self, DlgBusquedaGenerica):
        DlgBusquedaGenerica.setObjectName(_fromUtf8("DlgBusquedaGenerica"))
        DlgBusquedaGenerica.resize(473, 383)
        self.buscarPushButton = QtGui.QPushButton(DlgBusquedaGenerica)
        self.buscarPushButton.setGeometry(QtCore.QRect(200, 30, 75, 23))
        self.buscarPushButton.setObjectName(_fromUtf8("buscarPushButton"))
        self.busquedaLineEdit = QtGui.QLineEdit(DlgBusquedaGenerica)
        self.busquedaLineEdit.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.busquedaLineEdit.setMaxLength(13)
        self.busquedaLineEdit.setObjectName(_fromUtf8("busquedaLineEdit"))
        self.busquedaLabel = QtGui.QLabel(DlgBusquedaGenerica)
        self.busquedaLabel.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.busquedaLabel.setObjectName(_fromUtf8("busquedaLabel"))
        self.busquedaTableView = QtGui.QTableView(DlgBusquedaGenerica)
        self.busquedaTableView.setGeometry(QtCore.QRect(10, 80, 451, 291))
        self.busquedaTableView.setObjectName(_fromUtf8("busquedaTableView"))
        self.line = QtGui.QFrame(DlgBusquedaGenerica)
        self.line.setGeometry(QtCore.QRect(10, 60, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(DlgBusquedaGenerica)
        QtCore.QMetaObject.connectSlotsByName(DlgBusquedaGenerica)
        DlgBusquedaGenerica.setTabOrder(self.busquedaLineEdit, self.buscarPushButton)
        DlgBusquedaGenerica.setTabOrder(self.buscarPushButton, self.busquedaTableView)

    def retranslateUi(self, DlgBusquedaGenerica):
        DlgBusquedaGenerica.setWindowTitle(_translate("DlgBusquedaGenerica", "Seleccionar ciudad", None))
        self.buscarPushButton.setText(_translate("DlgBusquedaGenerica", "&Buscar", None))
        self.busquedaLabel.setText(_translate("DlgBusquedaGenerica", "TITULO:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgBusquedaGenerica = QtGui.QDialog()
    ui = Ui_DlgBusquedaGenerica()
    ui.setupUi(DlgBusquedaGenerica)
    DlgBusquedaGenerica.show()
    sys.exit(app.exec_())

