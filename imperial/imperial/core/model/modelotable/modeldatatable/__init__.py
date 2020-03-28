#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.core.util import util
from mate.vista import factoria


PATH_MDT = 'mate.dao.'

MDT_NAME = {factoria.ARTICLE_NEW: 'mdtArticle', 
            factoria.ARTICLE_NEW: 'mdtArticle'}

IDX_MDT_ARTICLE = range(1)

def getClaseModelo(tipo):
    return util.import_class(PATH_MDT + MDT_NAME[tipo])