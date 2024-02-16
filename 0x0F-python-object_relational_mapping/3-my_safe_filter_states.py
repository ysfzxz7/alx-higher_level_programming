#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states table\
        of hbtn_0e_0_usa where name matches the argument.\
        But this time, write one that is safe from MySQL injections!
Usage: ./3-my_safe_filter_states.py <mysql username> \
                                    <mysql password> \
                                    <database name> \
                                    <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
