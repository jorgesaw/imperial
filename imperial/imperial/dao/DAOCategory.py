'''
Created on 15/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, unicode_literals, print_function
from imperial.core.dao.DAOAlchemy import DAOAlchemy

class DAOCategory(DAOAlchemy):

    def __init__(self, cerrarSesion=True):
        super(DAOCategory, self).__init__(cerrarSesion)