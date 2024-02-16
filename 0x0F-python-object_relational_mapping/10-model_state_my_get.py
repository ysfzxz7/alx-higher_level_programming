#!/usr/bin/python3
"""
    A script that prints the State object with the name passed as an argument
    from hbtn_0e_6_usa
    Username, password, dbname and name to search
    will be passed as arguments to the script.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], argv[2], argv[3]),
                pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    states = session.query(State).filter(
        State.name == argv[4]
    ).one_or_none()

    if states is None:
        print("Not found")
    else:
        print(states.id)
    session.close()
