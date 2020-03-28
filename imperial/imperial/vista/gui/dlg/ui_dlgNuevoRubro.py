# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mate/ui/ui_dlgNuevoRubro.ui'
#
# Created: Sun Mar 22 23:24:18 2015
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

class Ui_DlgNuevoRubro(object):
    def setupUi(self, DlgNuevoRubro):
        DlgNuevoRubro.setObjectName(_fromUtf8("DlgNuevoRubro"))
        DlgNuevoRubro.resize(389, 88)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DlgNuevoRubro)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblRubro = QtGui.QLabel(DlgNuevoRubro)
        self.lblRubro.setObjectName(_fromUtf8("lblRubro"))
        self.verticalLayout.addWidget(self.lblRubro)
        self.lineRubro = QtGui.QLineEdit(DlgNuevoRubro)
        self.lineRubro.setObjectName(_fromUtf8("lineRubro"))
        self.verticalLayout.addWidget(self.lineRubro)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(DlgNuevoRubro)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.buttonBox = QtGui.QDialogButtonBox(DlgNuevoRubro)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DlgNuevoRubro)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgNuevoRubro.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgNuevoRubro.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgNuevoRubro)

    def retranslateUi(self, DlgNuevoRubro):
        DlgNuevoRubro.setWindowTitle(_translate("DlgNuevoRubro", "Nuevo Rubro", None))
        self.lblRubro.setText(_translate("DlgNuevoRubro", "Rubro:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgNuevoRubro = QtGui.QDialog()
    ui = Ui_DlgNuevoRubro()
    ui.setupUi(DlgNuevoRubro)
    DlgNuevoRubro.show()
    sys.exit(app.exec_())

