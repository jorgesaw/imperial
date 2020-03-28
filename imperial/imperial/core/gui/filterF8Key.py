#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

class FilterF8Key(QtCore.QObject):
    def eventFilter(self, source, event):
        if (event.type()==QEvent.KeyPress):
            if event.key()==Qt.Key_F8:
                source.emit(SIGNAL("f8Pressed()"))
        return QtGui.QWidget.eventFilter(self, source, event)
