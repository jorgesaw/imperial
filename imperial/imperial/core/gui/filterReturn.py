#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

class FilterReturn(QtCore.QObject):
    def eventFilter(self, source, event):
        if (event.type()==QEvent.KeyPress):
            key = event.key()
            if key==Qt.Key_Return or key==Qt.Key_Enter:
                source.emit(SIGNAL("enterPressed()"))
        return QtGui.QWidget.eventFilter(self, source, event)
    
class FilterESC(QtCore.QObject):
    def eventFilter(self, source, event):
        if (event.type()==QEvent.KeyPress):
            key = event.key()
            #print('KEY:', key)
            #print('ESC:', Qt.Key_Escape)
            if key==Qt.Key_Escape:
                source.emit(SIGNAL("ESCPressed()"))
        return QtGui.QWidget.eventFilter(self, source, event)