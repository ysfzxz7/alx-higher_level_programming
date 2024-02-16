#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of db  where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username>\
        <mysql password>\
        <database name>\
        <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    for state in cursor.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
