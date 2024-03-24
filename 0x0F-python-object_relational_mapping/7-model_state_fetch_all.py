#!/usr/bin/python3
"""a script that lists all State objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.name).all()
    i = 1
    for state in states:
        print(f'{i}: {state.name}')
        i += 1

    ''''
    enumerates returns two tubles constaining idxs and values
    of the itteratable passed to it
    for i, state in enumerate(states, start=1):
            print(f'{i}: {state.name}')'''
