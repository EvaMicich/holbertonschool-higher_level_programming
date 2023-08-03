#!/usr/bin/python3
""" prints the first State object from the database """
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
    first_state = session.query(State).first()
    print(f"{first_state.id}: {first_state.name}")
    session.close()
