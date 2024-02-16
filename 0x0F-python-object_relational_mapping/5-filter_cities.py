#!/usr/bin/python3
"""
    filter_cities Module.
    this program lists cities of a given state.

    usage: ./5-filter_cities 1 2 3 4
    args:
        1: mysql username
        2: mysql password
        3: database name
        4: state name
"""
import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    state_name = sys.argv[4]
    query = """SELECT cities.name
            FROM states
            INNER JOIN cities ON states.id = cities.state_id
            Where states.name = %s
            ORDER BY cities.id ASC"""
    c.execute(query, (state_name, ))
    rows = c.fetchall()
    print(", ".join([city[0] for city in rows]))
    c.close()
    db.close()
