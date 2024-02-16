#!/usr/bin/python3

"""
A script that list all cities from a db called cities
Usage: <username = mysql user>\
        <passwd = mysql password>\
        <db = databse name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = """
    SELECT `c`.`id`, `c`.`name`, `s`.`name`
    FROM `cities` as `c`
    INNER JOIN `states` as `s`
    ON `c`.`state_id` = `s`.`id`
    ORDER BY `c`.`id`
    """
    cursor.execute(query)
    for city in cursor.fetchall():
        print(city)
    cursor.close()
    db.close()
