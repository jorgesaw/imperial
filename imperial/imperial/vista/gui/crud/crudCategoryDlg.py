'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.vista.crud.CRUD import CRUD
from imperial.vista.gui.dlg.EditCategoryDlg import EditCategoryDlg
from imperial.vista.gui.dlg.NewCategoryDlg import NewCategoryDlg
import PyQt4.QtCore as _qc

class CrudCategoryDlg(CRUD):
    u"""Dialogo CRUD de rubros."""

    def __init__(self, modelo, parent=None):
        super(CrudCategoryDlg, self).__init__(modelo, parent)

        #self.datosTableView.setItemDelegate(CiudadesDelegate())
        self.updateUi()
        #CRUD.resizeColumns(self, (ModeloDatosCiudad.NOMBRE, ModeloDatosCiudad.COD_POSTAL,
        #ModeloDatosCiudad.DDN, ModeloDatosCiudad.PROVINCIA))
        self.datosTableView.setStyleSheet('background-color: rgb(156, 156, 156);')
        self.setWindowTitle("CRUD Rubros")

    @_qc.pyqtSlot()
    def on_newPushButton_clicked(self):
        addDlg = NewCategoryDlg()
        CRUD.addData(self, addDlg)

    @_qc.pyqtSlot()
    def on_editPushButton_clicked(self):
        editDlg = EditCategoryDlg()
        CRUD.editData(self, editDlg)

    @_qc.pyqtSlot()
    def on_listPushButton_clicked(self):
        CRUD.listData(self)

    @_qc.pyqtSlot()
    def on_searchPushButton_clicked(self):
        pass#CRUD.searchData(self, BusquedaGui.INSTIT)

    def updateUi(self):
        CRUD.updateUi(self)