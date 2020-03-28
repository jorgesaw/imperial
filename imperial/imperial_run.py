#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 31/03/2015

@author: jorgesaw
'''

"""
Runs La imperial
"""
import ctypes
myappid = 'jorgesaw.Sistema.La Imperial Sistema.0.7'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import imperial

imperial.run()