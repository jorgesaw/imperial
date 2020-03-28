'''
Created on 20/03/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from imperial.core.dao.DAOAlchemy import DAOAlchemy
from imperial.core.model.listmodel.datosListModel import DatosListModel

def getListaDatos(tipo, seleccionar=False):
    dao = DAOAlchemy(False)
    
    lista = dao.getAll(tipo)
    return DatosListModel(lista, seleccionar) if len(lista) > 0 \
                         else None
                         
