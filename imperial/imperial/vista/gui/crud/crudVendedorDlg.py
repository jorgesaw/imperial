'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.Actions import createAction, addActions
from imperial.core.vista.crud.CRUD import CRUD
from imperial.model.modeltable.delegate.delegate import VendedorDelegate
from imperial.vista.gui.dlg.EditVendedorDlg import EditVendedorDlg
from imperial.vista.gui.dlg.NewVendedorDlg import NewVendedorDlg
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
from imperial.model.modeltable.modeldatatable.mdtVendedor import ModeloDatosTablaVendedor

class CrudVendedorDlg(CRUD):
    u"""Dialogo CRUD de vendedores."""

    def __init__(self, modelo, parent=None):
        super(CrudVendedorDlg, self).__init__(modelo, parent)

        self.datosTableView.setItemDelegate(VendedorDelegate())
        self.updateUi()
        #CRUD.resizeColumns(self, (ModeloDatosCiudad.NOMBRE, ModeloDatosCiudad.COD_POSTAL,
        #ModeloDatosCiudad.DDN, ModeloDatosCiudad.PROVINCIA))
        self.datosTableView.setStyleSheet('background-color: rgb(153, 153, 80);')
        
        lst_width_col = [360, 70, 70, 70]
        for i, width in enumerate(lst_width_col):
            self.datosTableView.setColumnWidth(i, width)
        
        #self.datosTableView.horizontalHeader().setResizeMode(_qg.QHeaderView.Stretch)
        self.datosTableView.horizontalHeader().setStretchLastSection(True)
        self.setMinimumSize(650, 550)
        
        self.editAction = createAction(self, "&Edit", slot=self.on_editPushButton_clicked,
                                       shortcut=_qg.QKeySequence("Ctrl+E"), signal="triggered()")
        self.removeAction = createAction(self, "&Remove", slot=self.on_delPushButton_clicked,
                                         shortcut=_qg.QKeySequence("Del"), signal="triggered()")
        
        addActions(None, self, (self.editAction, self.removeAction))
        
        self.ciudadesLabel.setText('VENDEDORES')
        self.setWindowTitle("CRUD Vendedores")
        CRUD.listData(self)
        
    def on_datosTableView_clicked(self, index):
        if index.column() == ModeloDatosTablaVendedor.EDITAR:
            self.on_editPushButton_clicked()
        elif index.column() == ModeloDatosTablaVendedor.ELIMINAR:
            self.on_delPushButton_clicked()

    @_qc.pyqtSlot()
    def on_newPushButton_clicked(self):
        addDlg = NewVendedorDlg(self.modelo)
        CRUD.addData(self, addDlg)
        self.modelo.sortByColumn()

    @_qc.pyqtSlot()
    def on_editPushButton_clicked(self):
        editDlg = EditVendedorDlg(self.modelo)
        CRUD.editData(self, editDlg)
        self.modelo.sortByColumn()

    @_qc.pyqtSlot()
    def on_listPushButton_clicked(self):
        CRUD.listData(self)

    @_qc.pyqtSlot()
    def on_searchPushButton_clicked(self):
        from imperial.vista import factoria
        CRUD.searchData(self, factoria.SEARCH_VENDEDOR)

    def updateUi(self):
        CRUD.updateUi(self)