#!/usr/bin/python3
''' A module defining a City class that inherits from Base'''
from sqlalchemy import Integer, Column, String, ForeignKey
from model_state import Base
# from sqlalchemy.orm import relationship


class City(Base):
    ''' A class that inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # states = relationship('State', backpopulates='cities')
