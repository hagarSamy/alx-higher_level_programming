#!/usr/bin/python3
"""a script that adds the State object “Louisiana” to
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
    newObj = State(name="Louisiana")
    myState = session.add(newObj)
    session.commit()
    print(f'{newObj.id}')
    session.close()
