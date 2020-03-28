# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imperial/ui/ui_dlgNuevoIngrediente.ui'
#
# Created: Fri Jun 12 22:45:35 2015
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

class Ui_DlgNuevoIngrediente(object):
    def setupUi(self, DlgNuevoIngrediente):
        DlgNuevoIngrediente.setObjectName(_fromUtf8("DlgNuevoIngrediente"))
        DlgNuevoIngrediente.resize(525, 228)
        self.verticalLayout = QtGui.QVBoxLayout(DlgNuevoIngrediente)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblIngred = QtGui.QLabel(DlgNuevoIngrediente)
        self.lblIngred.setObjectName(_fromUtf8("lblIngred"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lblIngred)
        self.lineIngred = QtGui.QLineEdit(DlgNuevoIngrediente)
        self.lineIngred.setMaxLength(50)
        self.lineIngred.setObjectName(_fromUtf8("lineIngred"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineIngred)
        self.lblPrecio = QtGui.QLabel(DlgNuevoIngrediente)
        self.lblPrecio.setObjectName(_fromUtf8("lblPrecio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblPrecio)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dsPrecio = QtGui.QDoubleSpinBox(DlgNuevoIngrediente)
        self.dsPrecio.setMaximum(99999.99)
        self.dsPrecio.setObjectName(_fromUtf8("dsPrecio"))
        self.horizontalLayout.addWidget(self.dsPrecio)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_2 = QtGui.QFrame(DlgNuevoIngrediente)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.groupBox = QtGui.QGroupBox(DlgNuevoIngrediente)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioKg = QtGui.QRadioButton(self.groupBox)
        self.radioKg.setChecked(True)
        self.radioKg.setObjectName(_fromUtf8("radioKg"))
        self.horizontalLayout_2.addWidget(self.radioKg)
        self.radioLts = QtGui.QRadioButton(self.groupBox)
        self.radioLts.setObjectName(_fromUtf8("radioLts"))
        self.horizontalLayout_2.addWidget(self.radioLts)
        self.radioOtros = QtGui.QRadioButton(self.groupBox)
        self.radioOtros.setObjectName(_fromUtf8("radioOtros"))
        self.horizontalLayout_2.addWidget(self.radioOtros)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lblCant = QtGui.QLabel(self.groupBox)
        self.lblCant.setObjectName(_fromUtf8("lblCant"))
        self.horizontalLayout_3.addWidget(self.lblCant)
        self.spinBoxCantidad = QtGui.QSpinBox(self.groupBox)
        self.spinBoxCantidad.setEnabled(False)
        self.spinBoxCantidad.setMinimum(1)
        self.spinBoxCantidad.setMaximum(999)
        self.spinBoxCantidad.setObjectName(_fromUtf8("spinBoxCantidad"))
        self.horizontalLayout_3.addWidget(self.spinBoxCantidad)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DlgNuevoIngrediente)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioGrmsCm3 = QtGui.QRadioButton(self.groupBox_2)
        self.radioGrmsCm3.setChecked(True)
        self.radioGrmsCm3.setObjectName(_fromUtf8("radioGrmsCm3"))
        self.horizontalLayout_4.addWidget(self.radioGrmsCm3)
        self.radioKgLts = QtGui.QRadioButton(self.groupBox_2)
        self.radioKgLts.setChecked(False)
        self.radioKgLts.setObjectName(_fromUtf8("radioKgLts"))
        self.horizontalLayout_4.addWidget(self.radioKgLts)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(DlgNuevoIngrediente)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.lblIngred.setBuddy(self.lineIngred)
        self.lblPrecio.setBuddy(self.dsPrecio)
        self.lblCant.setBuddy(self.spinBoxCantidad)

        self.retranslateUi(DlgNuevoIngrediente)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgNuevoIngrediente.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgNuevoIngrediente.reject)
        QtCore.QObject.connect(self.radioOtros, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinBoxCantidad.setEnabled)
        QtCore.QObject.connect(self.lineIngred, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.dsPrecio.setFocus)
        QtCore.QObject.connect(self.lineIngred, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.dsPrecio.selectAll)
        QtCore.QMetaObject.connectSlotsByName(DlgNuevoIngrediente)
        DlgNuevoIngrediente.setTabOrder(self.lineIngred, self.dsPrecio)
        DlgNuevoIngrediente.setTabOrder(self.dsPrecio, self.radioKg)
        DlgNuevoIngrediente.setTabOrder(self.radioKg, self.radioLts)
        DlgNuevoIngrediente.setTabOrder(self.radioLts, self.radioOtros)
        DlgNuevoIngrediente.setTabOrder(self.radioOtros, self.spinBoxCantidad)
        DlgNuevoIngrediente.setTabOrder(self.spinBoxCantidad, self.buttonBox)

    def retranslateUi(self, DlgNuevoIngrediente):
        DlgNuevoIngrediente.setWindowTitle(_translate("DlgNuevoIngrediente", "Nuevo Ingrediente", None))
        self.lblIngred.setText(_translate("DlgNuevoIngrediente", "&INGREDIENTE:", None))
        self.lblPrecio.setText(_translate("DlgNuevoIngrediente", "&PRECIO:", None))
        self.groupBox.setTitle(_translate("DlgNuevoIngrediente", "UNIDAD DE MEDIDA:", None))
        self.radioKg.setText(_translate("DlgNuevoIngrediente", "Kilogramo (Kg.)", None))
        self.radioLts.setText(_translate("DlgNuevoIngrediente", "Litros (Lts.)", None))
        self.radioOtros.setText(_translate("DlgNuevoIngrediente", "Otros", None))
        self.lblCant.setText(_translate("DlgNuevoIngrediente", "&Cantidad:", None))
        self.groupBox_2.setTitle(_translate("DlgNuevoIngrediente", "PESAMOS POR:", None))
        self.radioGrmsCm3.setText(_translate("DlgNuevoIngrediente", "GRMS/CM3", None))
        self.radioKgLts.setText(_translate("DlgNuevoIngrediente", "kG./lTS.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgNuevoIngrediente = QtGui.QDialog()
    ui = Ui_DlgNuevoIngrediente()
    ui.setupUi(DlgNuevoIngrediente)
    DlgNuevoIngrediente.show()
    sys.exit(app.exec_())

