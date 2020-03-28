# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'megachance/ui/ui_dlgProgressFile.ui'
#
# Created: Sat Jun 28 06:48:08 2014
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

class Ui_DlgProgressFile(object):
    def setupUi(self, DlgProgressFile):
        DlgProgressFile.setObjectName(_fromUtf8("DlgProgressFile"))
        DlgProgressFile.resize(334, 58)
        self.verticalLayout = QtGui.QVBoxLayout(DlgProgressFile)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.msgLabel = QtGui.QLabel(DlgProgressFile)
        self.msgLabel.setObjectName(_fromUtf8("msgLabel"))
        self.verticalLayout.addWidget(self.msgLabel)
        self.fileProgressBar = QtGui.QProgressBar(DlgProgressFile)
        self.fileProgressBar.setProperty("value", 0)
        self.fileProgressBar.setTextVisible(False)
        self.fileProgressBar.setInvertedAppearance(False)
        self.fileProgressBar.setObjectName(_fromUtf8("fileProgressBar"))
        self.verticalLayout.addWidget(self.fileProgressBar)

        self.retranslateUi(DlgProgressFile)
        QtCore.QMetaObject.connectSlotsByName(DlgProgressFile)

    def retranslateUi(self, DlgProgressFile):
        DlgProgressFile.setWindowTitle(_translate("DlgProgressFile", "Dialog", None))
        self.msgLabel.setText(_translate("DlgProgressFile", "Copiando base de datos...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgProgressFile = QtGui.QDialog()
    ui = Ui_DlgProgressFile()
    ui.setupUi(DlgProgressFile)
    DlgProgressFile.show()
    sys.exit(app.exec_())

