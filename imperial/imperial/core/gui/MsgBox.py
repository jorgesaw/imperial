#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 13/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
import PyQt4.QtGui as _qg

class MsgBox(object):
    
    @staticmethod
    def okToContinue(parent=None, title=u"Mate TPV - Salir", 
                     msg=u"¿Desea salir de la aplicación?"):
        if parent:
            reply = _qg.QMessageBox.question(parent,
                                    parent.tr(title),
                                    parent.tr(msg),
                                    parent.tr(u'Sí'),
                                    parent.tr(u'No'),
                                    parent.tr(u'Cancelar')
                                    )
        else:
            reply = _qg.QMessageBox.question(parent,
                            title, msg, u'Sí', u'No', u'Cancelar')
        if reply != 0: #uSi no eligió sí
            return False
        return True
    
    @staticmethod
    def ok_NoToContinue(parent=None, title=None, msg=None):
        if parent:
            reply = _qg.QMessageBox.question(parent,
                                    parent.tr(title),
                                    parent.tr(msg),
                                    parent.tr(u'Sí'),
                                    parent.tr(u'No'),
                                    )
        else:
            reply = _qg.QMessageBox.question(parent,
                            title, msg, u'Sí', u'No')
        if reply != 0: #uSi no eligió sí
            return False
        return True