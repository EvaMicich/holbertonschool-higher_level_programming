#!/usr/bin/python3
"""deletes the State object contains a"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                                sys.argv[1],
                                                                sys.argv[2],
                                                                sys.argv[3]),
                           echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = session.query(State).filter(State.name.like('%a%'))
    for state in states_with_a:
        session.delete(state)
    session.commit()
    session.close()
