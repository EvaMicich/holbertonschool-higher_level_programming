#!/usr/bin/python3
"""lists all cities objects of the database hbtn_0e_14_usa"""
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                                sys.argv[1],
                                                                sys.argv[2],
                                                                sys.argv[3]),
                           echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    joint_table = session.query(City, State).join(State)
    for city, state in joint_table:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
