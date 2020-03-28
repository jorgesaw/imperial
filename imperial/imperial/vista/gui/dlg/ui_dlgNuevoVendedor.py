# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgNuevoVendedor.ui'
#
# Created: Sun Jun 07 01:22:50 2015
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

class Ui_DlgNuevoVendedor(object):
    def setupUi(self, DlgNuevoVendedor):
        DlgNuevoVendedor.setObjectName(_fromUtf8("DlgNuevoVendedor"))
        DlgNuevoVendedor.resize(389, 118)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DlgNuevoVendedor)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblRubro = QtGui.QLabel(DlgNuevoVendedor)
        self.lblRubro.setObjectName(_fromUtf8("lblRubro"))
        self.verticalLayout.addWidget(self.lblRubro)
        self.lineVendedor = QtGui.QLineEdit(DlgNuevoVendedor)
        self.lineVendedor.setObjectName(_fromUtf8("lineVendedor"))
        self.verticalLayout.addWidget(self.lineVendedor)
        self.checkVendedor = QtGui.QCheckBox(DlgNuevoVendedor)
        self.checkVendedor.setChecked(True)
        self.checkVendedor.setObjectName(_fromUtf8("checkVendedor"))
        self.verticalLayout.addWidget(self.checkVendedor)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(DlgNuevoVendedor)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.buttonBox = QtGui.QDialogButtonBox(DlgNuevoVendedor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DlgNuevoVendedor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgNuevoVendedor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgNuevoVendedor.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgNuevoVendedor)

    def retranslateUi(self, DlgNuevoVendedor):
        DlgNuevoVendedor.setWindowTitle(_translate("DlgNuevoVendedor", "Nuevo Vendedor", None))
        self.lblRubro.setText(_translate("DlgNuevoVendedor", "Nombre Venta:", None))
        self.checkVendedor.setText(_translate("DlgNuevoVendedor", "Es vendedor", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgNuevoVendedor = QtGui.QDialog()
    ui = Ui_DlgNuevoVendedor()
    ui.setupUi(DlgNuevoVendedor)
    DlgNuevoVendedor.show()
    sys.exit(app.exec_())

