#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
import win32api
import win32print

def defaultPrinter(filename):
    win32api.ShellExecute(
    0, 
    "print", 
    filename, 
    #
    #
    #
    #
    '/d:"%s"' % win32print.GetDefaultPrinter(),
    ".",
    0
    )
    
