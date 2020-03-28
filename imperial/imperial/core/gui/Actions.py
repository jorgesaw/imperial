#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

def createAction(self, text, slot=None, shortcut=None, icon=None,
                 tip=None, checkable=None, signal='triggered()'):
    u"""Función que permite crear acciones para un entorno de ventanas."""
    
    action = QAction(text, self)
    if icon is not None:
        action.setIcon(QIcon(':/{0}'.format(icon)))
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if slot is not None:
        self.connect(action, SIGNAL(signal), slot)
    if checkable is not None:
        action.setCheckable(True)
    return action

def addActions(self, target, actions):
    u"""Agrega las acciones de un elemento del menú de la aplicación"""
    for action in actions:
        if action is None:
            target.addSeparator()
        else:
            target.addAction(action)
            
def editAction(self, action, text=None, slot=None, shortcut=None, icon=None,
                 tip=None, checkable=None, signal='triggered()'):
    u"""Función que permite crear acciones para un entorno de ventanas."""
    
    if text:
        action.setText(text)
    if icon is not None:
        action.setIcon(QIcon(':/{0}'.format(icon)))
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    if slot is not None:
        self.connect(action, SIGNAL(signal), slot)
    if checkable is not None:
        action.setCheckable(True)
    return action