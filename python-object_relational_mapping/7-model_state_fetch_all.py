#!/usr/bin/python3
"""lists all State objects from the database"""
import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format\
                           (sys.argv[1], sys.argv[2], sys.argv[3]),\
                           echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_dict = session.query(State).all()

    for state in state_dict:
        print(f"{state.id}: {state.name}")
    session.close()
