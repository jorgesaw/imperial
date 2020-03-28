#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 31/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.core.util import rc_style
import PyQt4
import PyQt4.QtCore as _qc
import PyQt4.QtGui as _qg
import ctypes
import logging
import logging.config
import imperial.model.mapper.mapeador
import imperial.qrc_main_window
import os
import sys
from imperial.vista.main.MainWindowImperial import MainWindowImperial

#myappid = 'jorgesaw.Mate_TPV.Mate_TPV.0.6'
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

__version__ = '1.0.0'

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)

class App(_qg.QApplication):
    
    def __init__(self):
        super(App, self).__init__(sys.argv)
        
        self.setOrganizationName("Uno.x Inc.")
        self.setOrganizationDomain("unox.com.ar")
        self.setApplicationName(u"La Imperial Sistema")
        self.setWindowIcon(_qg.QIcon(":/favicon.png"))
        
        #self.codec = _qc.QTextCodec.codecForName("UTF-8".encode("ascii", "ignore"))
        
        #_qc.QTextCodec.setCodecForTr(self.codec)
        #_qc.QTextCodec.setCodecForCStrings(self.codec)
        #_qc.QTextCodec.setCodecForLocale(self.codec)
        #self.translators = []
        
        #VERRRRRRRRRRRRRRRR
        #loads all the translations
        #locale = _qc.QLocale.system().name()
        #for tr_name in ( locale, 'qt_'+locale):
        #    if not self.loadTranslation(tr_name):
                #new_tr_name = tr_name.rsplit('_', 1)[0]#If en_GB doesnt load, try to load en
                #self.loadTranslation(new_tr_name)
        #        pass
        
        #print(QtCore.QTextCodec.codecForCStrings().name())
        #test the translation
        #dont use unicode
        logger.info(self.tr("Loading ...".encode('utf-8')))
        
        #I've decided that is better to have consistence than pain
        #_qc.QLocale.setDefault(_qc.QLocale.c())
        
        #sets a style (which is not the same as stylesheet)
        #the default style (windows) doesn't allow to use transparent background on widgets
        #self.setStyle("plastique")
        #Some built-in stylesheets
        
        #Some built-in stylesheets
        self.style = 0
        #self.styles = ( ":/data/darkorange.qss", ":/data/style.qss",":/data/levelfour.qss", 'user.qss')
        self.styles = {'Por defecto': None, 
                       "darkorange": ":/data/darkorange.qss", }
        #sets the first stylesheet
        #self.changeStyle()
        
        self.window = MainWindowImperial(self)
    
    def run(self):
        #Enters the main loop
        self.window.showMaximized()
        return self.exec_()    
        
    def changeStyle(self):
        if self.sender():
            if self.sender().data():
                self.syle = int(self.sender().data())
        style = rc_style.cargarStyleSheet(self.styles.values()[self.style])
        self.setStyleSheet(style)
        
    def loadTranslation(self, name, path=':/data/trans/'):
        """Loads a translation file, it must be a ".qm" file
        by default it loads it from resource file
        it only loads ONE translation
        """
        return
        logger.info("Loading translation '%s' in '%s'"%(name, path))
        trans = _qc.QTranslator()

        if trans.load(name, path):
            self.installTranslator(trans)
            self.translators.append(trans)
            logger.info("Translation loaded ok")
            return True
        else:
            logger.error("Couldn't load translator %s"%name)
            return False
        
    def showWindow(self, wnd):
        if len(self.window.mdiArea.subWindowList()) > 0:
            self.window.mdiArea.closeAllSubWindows()
        self.window.mdiArea.addSubWindow(wnd)
        wnd.show()
        
    def isWindowActived(self, tipo):
        u""""""
        for wnd in self.window.mdiArea.subWindowList():
            if isinstance(wnd, tipo):
                return True
        return False
    
def runApp():
    return App().run()
    
def run():
    return runApp()
        
if __name__=='__main__':
    sys.exit(run())