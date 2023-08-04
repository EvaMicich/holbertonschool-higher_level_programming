#!/usr/bin/python3
"""changes the name of a State object, id2=Mexico"""
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
    state_to_fix = session.query(State).filter(State.id == 2).first()
    state_to_fix.name = "New Mexico"
    session.commit()
    session.close()
