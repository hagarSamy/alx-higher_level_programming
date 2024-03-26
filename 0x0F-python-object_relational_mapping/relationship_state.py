#!/usr/bin/python3
''' A module defining a State as an instance of Base'''
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    ''' A class that inherits from Base'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="states")
