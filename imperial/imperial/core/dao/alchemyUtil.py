#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from contextlib import contextmanager
import imperial.core.dao.config as config

u"""Módulo factoría para crear una sesión en SQLAlchemy.
    :author: Jorge Adrián Gonzalez
    :version: 1.0.0"""

__docformat__ = "reestructuredtext"

__version__ = "1.0.0"


cadenaConexion = config.cargarConfig()
engine = create_engine(cadenaConexion, echo=True)
#Session = sessionmaker(bind=engine)
session_factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(session_factory)
    
def session():
    u"""Clase que crea una sesión para realizar las transacciones."""
    session = Session() 
    return session

def conn():
    u"""Clase que crea una conexión para realizar las transacciones."""
    conn = engine.connect()
    return conn

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

#with session_scope() as session:
#    print(session)

