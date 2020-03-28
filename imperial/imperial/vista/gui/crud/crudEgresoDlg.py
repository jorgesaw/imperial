'''
Created on 19/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.gui.Actions import createAction, addActions
from imperial.core.vista.crud.CRUD import CRUD
from imperial.model.modeltable.delegate.delegate import EgresoDelegate
from imperial.vista.gui.dlg.EditEgresoDlg import EditEgresoDlg
from imperial.vista.gui.dlg.NewEgresoDlg import NewEgresoDlg
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
from imperial.model.modeltable.modeldatatable.mdtEgreso import ModeloDatosTablaEgreso

class CrudEgresoDlg(CRUD):
    u"""Dialogo CRUD de rubros."""

    def __init__(self, modelo, parent=None):
        super(CrudEgresoDlg, self).__init__(modelo, parent)

        self.datosTableView.setItemDelegate(EgresoDelegate())
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
        
        self.ciudadesLabel.setText('EGRESOS')
        self.setWindowTitle("CRUD Egresos")
        CRUD.listData(self)
        
    def on_datosTableView_clicked(self, index):
        if index.column() == ModeloDatosTablaEgreso.EDITAR:
            self.on_editPushButton_clicked()
        elif index.column() == ModeloDatosTablaEgreso.ELIMINAR:
            self.on_delPushButton_clicked()

    @_qc.pyqtSlot()
    def on_newPushButton_clicked(self):
        addDlg = NewEgresoDlg(self.modelo)
        CRUD.addData(self, addDlg)
        self.modelo.sortByColumn()

    @_qc.pyqtSlot()
    def on_editPushButton_clicked(self):
        editDlg = EditEgresoDlg(self.modelo)
        CRUD.editData(self, editDlg)
        self.modelo.sortByColumn()

    @_qc.pyqtSlot()
    def on_listPushButton_clicked(self):
        CRUD.listData(self)

    @_qc.pyqtSlot()
    def on_searchPushButton_clicked(self):
        from imperial.vista import factoria
        CRUD.searchData(self, factoria.SEARCH_EGRESO)

    def updateUi(self):
        CRUD.updateUi(self)