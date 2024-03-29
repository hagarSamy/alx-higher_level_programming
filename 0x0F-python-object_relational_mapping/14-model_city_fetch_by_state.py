#!/usr/bin/python3
"""a script that prints all City objects'
from the database hbtn_0e_14_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    myStatesCities = session.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in myStatesCities:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.commit()
    session.close()
