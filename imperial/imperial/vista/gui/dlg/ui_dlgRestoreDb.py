# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'megachance/ui/ui_dlgRestoreDb.ui'
#
# Created: Thu Jun 26 01:57:00 2014
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

class Ui_DlgRestoreDb(object):
    def setupUi(self, DlgRestoreDb):
        DlgRestoreDb.setObjectName(_fromUtf8("DlgRestoreDb"))
        DlgRestoreDb.resize(230, 169)
        self.verticalLayout = QtGui.QVBoxLayout(DlgRestoreDb)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelCopia = QtGui.QLabel(DlgRestoreDb)
        self.labelCopia.setObjectName(_fromUtf8("labelCopia"))
        self.verticalLayout.addWidget(self.labelCopia)
        self.copiasListWidget = QtGui.QListWidget(DlgRestoreDb)
        self.copiasListWidget.setStyleSheet(_fromUtf8("font: 14pt \"Lucida Sans\";"))
        self.copiasListWidget.setObjectName(_fromUtf8("copiasListWidget"))
        self.verticalLayout.addWidget(self.copiasListWidget)
        self.line = QtGui.QFrame(DlgRestoreDb)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.restorePushButton = QtGui.QPushButton(DlgRestoreDb)
        self.restorePushButton.setObjectName(_fromUtf8("restorePushButton"))
        self.verticalLayout.addWidget(self.restorePushButton)
        self.labelCopia.setBuddy(self.copiasListWidget)

        self.retranslateUi(DlgRestoreDb)
        QtCore.QMetaObject.connectSlotsByName(DlgRestoreDb)

    def retranslateUi(self, DlgRestoreDb):
        DlgRestoreDb.setWindowTitle(_translate("DlgRestoreDb", "Restaurar Base de Datos", None))
        self.labelCopia.setText(_translate("DlgRestoreDb", "Copias de &seguridad", None))
        self.restorePushButton.setText(_translate("DlgRestoreDb", "Restaurar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgRestoreDb = QtGui.QDialog()
    ui = Ui_DlgRestoreDb()
    ui.setupUi(DlgRestoreDb)
    DlgRestoreDb.show()
    sys.exit(app.exec_())

