#!/usr/bin/python3
"""a script that changes the name of a State object from
the database hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    myState = session.query(State).filter(State.id == 2).first()
    myState.name = "New Mexico"
    session.commit()
    session.close()