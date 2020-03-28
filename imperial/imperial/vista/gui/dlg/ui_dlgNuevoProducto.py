# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgNuevoProducto.ui'
#
# Created: Fri Jun 12 22:48:16 2015
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

class Ui_dlgNuevoProducto(object):
    def setupUi(self, dlgNuevoProducto):
        dlgNuevoProducto.setObjectName(_fromUtf8("dlgNuevoProducto"))
        dlgNuevoProducto.resize(470, 160)
        self.verticalLayout = QtGui.QVBoxLayout(dlgNuevoProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblNombre = QtGui.QLabel(dlgNuevoProducto)
        self.lblNombre.setObjectName(_fromUtf8("lblNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblNombre)
        self.lineNombre = QtGui.QLineEdit(dlgNuevoProducto)
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineNombre)
        self.label = QtGui.QLabel(dlgNuevoProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dSpinBoxPrecio = QtGui.QDoubleSpinBox(dlgNuevoProducto)
        self.dSpinBoxPrecio.setMaximum(99999.99)
        self.dSpinBoxPrecio.setObjectName(_fromUtf8("dSpinBoxPrecio"))
        self.horizontalLayout.addWidget(self.dSpinBoxPrecio)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_2 = QtGui.QLabel(dlgNuevoProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lblDesc = QtGui.QLabel(dlgNuevoProducto)
        self.lblDesc.setObjectName(_fromUtf8("lblDesc"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblDesc)
        self.lineDesc = QtGui.QLineEdit(dlgNuevoProducto)
        self.lineDesc.setMaxLength(50)
        self.lineDesc.setObjectName(_fromUtf8("lineDesc"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineDesc)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboRubros = QtGui.QComboBox(dlgNuevoProducto)
        self.comboRubros.setObjectName(_fromUtf8("comboRubros"))
        self.horizontalLayout_2.addWidget(self.comboRubros)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtGui.QFrame(dlgNuevoProducto)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.buttonBox = QtGui.QDialogButtonBox(dlgNuevoProducto)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lblNombre.setBuddy(self.lineNombre)
        self.label.setBuddy(self.dSpinBoxPrecio)
        self.label_2.setBuddy(self.comboRubros)
        self.lblDesc.setBuddy(self.lineDesc)

        self.retranslateUi(dlgNuevoProducto)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dlgNuevoProducto.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dlgNuevoProducto.reject)
        QtCore.QObject.connect(self.lineNombre, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.dSpinBoxPrecio.setFocus)
        QtCore.QObject.connect(self.lineNombre, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.dSpinBoxPrecio.selectAll)
        QtCore.QObject.connect(self.dSpinBoxPrecio, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.comboRubros.setFocus)
        QtCore.QMetaObject.connectSlotsByName(dlgNuevoProducto)
        dlgNuevoProducto.setTabOrder(self.lineNombre, self.dSpinBoxPrecio)
        dlgNuevoProducto.setTabOrder(self.dSpinBoxPrecio, self.comboRubros)
        dlgNuevoProducto.setTabOrder(self.comboRubros, self.lineDesc)
        dlgNuevoProducto.setTabOrder(self.lineDesc, self.buttonBox)

    def retranslateUi(self, dlgNuevoProducto):
        dlgNuevoProducto.setWindowTitle(_translate("dlgNuevoProducto", "Nuevo Producto", None))
        self.lblNombre.setText(_translate("dlgNuevoProducto", "&Nombre", None))
        self.label.setText(_translate("dlgNuevoProducto", "&Precio:", None))
        self.dSpinBoxPrecio.setPrefix(_translate("dlgNuevoProducto", "$ ", None))
        self.label_2.setText(_translate("dlgNuevoProducto", "&Rubro:", None))
        self.lblDesc.setText(_translate("dlgNuevoProducto", "&Descripción:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlgNuevoProducto = QtGui.QDialog()
    ui = Ui_dlgNuevoProducto()
    ui.setupUi(dlgNuevoProducto)
    dlgNuevoProducto.show()
    sys.exit(app.exec_())

