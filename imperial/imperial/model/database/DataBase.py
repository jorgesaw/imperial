#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from imperial.vista.gui.dlg.RestoreDbDlg import RestoreDbDlg
import datetime
import os
import shutil
import tempfile
from imperial.core.gui.MsgBox import MsgBox

class DataBase(object):

    PATH_BCK = '\\BCK\\'
    
    def __init__(self, vistaProgressBar):
        self.formatoFecha='%d-%m-%Y'
        self.fechas = []
        self.vistaProgressBar = vistaProgressBar

    def restaurarDb(self):
        for _dir, subdirectories, files in (os.walk(os.curdir + DataBase.PATH_BCK)):
            for subdir in subdirectories:
                self.fechas.append(unicode(subdir))

        if len(self.fechas) == 0:
            QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Imposible restaurar la base de datos.\n' + \
                                    u'Aún no se creó ninguna copia de seguridad.')
            return
        restoreDlg = RestoreDbDlg()
        self.fechas.reverse()
        restoreDlg.setDatosItems(self.fechas)
        r = restoreDlg.exec_()
        if r:
            if MsgBox.okToContinue(None, 
                u'La Imperial - Restaurar base de datos',
                u'Si continúa se perderán los datos cargados\n' +
                    'después de la fecha seleccionada: ' + restoreDlg.data()[0] + '.\n\n' +
                        u'¿Está seguro que desea restaurar la\n' + 
                            'base de datos a la fecha seleccionada?'):
                self.vistaProgressBar.show()
                self.vistaProgressBar.on_fileProgressBar_valueChanged(10)
                try:
                    shutil.copy(os.curdir + '\\imperial.db', tempfile.mkdtemp() + '\\imperial.db')
                    self.vistaProgressBar.on_fileProgressBar_valueChanged(30)
                    try:
                        dirNuevo = os.curdir + '\\BCK\\' + restoreDlg.data()[0]
                        self.vistaProgressBar.on_fileProgressBar_valueChanged(60)
                        shutil.copy(dirNuevo + '\\imperial.db', os.curdir + '\\imperial.db')
                        self.vistaProgressBar.on_fileProgressBar_valueChanged(100)
                        QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                         u'Copia de seguridad restaurada con éxito.')
                    except:
                        QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Se produjo un error al restaurar la copia de seguridad.')
                except:
                    QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Se produjo un error al restaurar la copia de seguridad.')

    def resguardarDb(self):
        QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Aguarde unos segundos mientras se prepara\n' +
                                     u'una copia de la base de datos.')
        
        fechaActual = datetime.date.today().strftime(self.formatoFecha)
        bck_sub_dir = None  
        fechas = []
        dirEncontrado = False
        
        self.vistaProgressBar.show()
        self.vistaProgressBar.on_fileProgressBar_valueChanged(10)
        
        for _dir, subdirectories, files in (os.walk(os.curdir + DataBase.PATH_BCK)):
            for subdir in subdirectories:
                if subdir == fechaActual:
                    dirEncontrado = True
                self.fechas.append(subdir)
        self.vistaProgressBar.on_fileProgressBar_valueChanged(20)
        if not dirEncontrado:
            try:
                dirNuevo = os.curdir + '\\BCK\\' + datetime.date.today().strftime(self.formatoFecha)
                os.mkdir(dirNuevo)
                self.vistaProgressBar.on_fileProgressBar_valueChanged(40)
                shutil.copy(os.curdir + '\\imperial.db', dirNuevo + '\\imperial.db')
                self.vistaProgressBar.on_fileProgressBar_valueChanged(75)
                if len(self.fechas) > 2:
                    shutil.rmtree(os.curdir + '\\BCK\\' + self.fechas[0])
                self.vistaProgressBar.on_fileProgressBar_valueChanged(100)
                QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Copia de seguridad realizada con éxito.')
                
            except Exception, e:
                print('E:', e)
                QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Se produjo un error al realizar la copia de seguridad.')
        else:   
            if MsgBox.okToContinue(None, u'La Imperial - Resguardar base de datos',
                                  u'Ya se ha realizado una copia de seguridad en el día de la fecha.\n' +
                                         u'¿Desea sobreescribir los datos?'):
                try:
                    self.vistaProgressBar.on_fileProgressBar_valueChanged(40)
                    dirNuevo = os.curdir + '\\BCK\\' + datetime.date.today().strftime(self.formatoFecha)
                    self.vistaProgressBar.on_fileProgressBar_valueChanged(60)
                    shutil.copy(os.curdir + '\\imperial.db', dirNuevo + '\\imperial.db')
                    self.vistaProgressBar.on_fileProgressBar_valueChanged(100)
                    QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Copia de seguridad realizada con éxito.')
                except:
                    QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Se produjo un error al realizar la copia de seguridad.')
        
        self.vistaProgressBar.accept()
        
    def resguardarDbEn(self, dir_bck):
        QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                                     u'Aguarde unos segundos mientras se prepara\n' +
                                     u'una copia de la base de datos.')
        
        fechaActual = datetime.date.today().strftime(self.formatoFecha)
        
        self.vistaProgressBar.show()
        self.vistaProgressBar.on_fileProgressBar_valueChanged(10)
        self.vistaProgressBar.on_fileProgressBar_valueChanged(20)
        
        try:
            self.vistaProgressBar.on_fileProgressBar_valueChanged(40)
            #dir_nuevo = dir_bck + '\\BCK_LA_IMPERIAL\\'
            if not os.path.exists(dir_bck + '\\BCK_LA_IMPERIAL\\'):
                os.mkdir(dir_bck + '\\BCK_LA_IMPERIAL\\')
            if not os.path.exists(dir_bck + '\\BCK_LA_IMPERIAL\\' + datetime.date.today().strftime(self.formatoFecha)):
                os.mkdir(dir_bck + '\\BCK_LA_IMPERIAL\\' + datetime.date.today().strftime(self.formatoFecha))
                
            #dirNuevo = dir_bck + '\\BCK\\' + datetime.date.today().strftime(self.formatoFecha)
            
            #os.mkdir(dir_bck + '\\BCK\\')
            #os.mkdir(dirNuevo)
            
            self.vistaProgressBar.on_fileProgressBar_valueChanged(60)
            shutil.copy(os.curdir + '\\imperial.db', 
                dir_bck + '\\BCK_LA_IMPERIAL\\' + datetime.date.today().strftime(self.formatoFecha) + '\\imperial.db')
            self.vistaProgressBar.on_fileProgressBar_valueChanged(100)
            QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                             u'Copia de seguridad realizada con éxito.')
        except:
            QMessageBox.information(None, u'La Imperial - Resguardar base de datos',
                             u'Se produjo un error al realizar la copia de seguridad.')
        
        self.vistaProgressBar.accept()    

    def okToContinue(self, listaDatos):
        reply = QMessageBox.question(None,
                                     listaDatos[0],
                                     listaDatos[1],
                                     QMessageBox.Yes|QMessageBox.No|
                                     QMessageBox.Cancel)
        if reply != QMessageBox.Yes:
            return False
        return True


         #QMessageBox.question (None, 'titulo', 'texto', button0Text = 'Can',
          #                     button1Text = 'No',
           #                    button2Text = 'Si',
            #                   defaultButtonNumber = 0, escapeButtonNumber = -1)