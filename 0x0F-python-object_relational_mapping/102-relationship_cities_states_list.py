#!/usr/bin/python3
"""a script that lists all City objects from the database hbtn_0e_101_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    allSt = session.query(State).all()
    for state in allSt:
        for city in state.cities:
            print(f'{city.id}: {city.name} -> {state.name}')
    session.close()
