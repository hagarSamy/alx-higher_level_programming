#!/usr/bin/python3
''' class definition of a State and an instance of Base'''
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
import sys


db = sys.argv[1]
usname = sys.argv[2]
pswd = sys.argv[3]
Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(db, usname, pswd))


class State(Base):
    ''' A class that inherits from Base'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
