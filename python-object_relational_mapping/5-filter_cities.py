#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
table that match the argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
    FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name LIKE %s\
    ORDER BY cities.id;", (sys.argv[4],))
    rows = cur.fetchall()
    cities_list = [word for row in rows for word in row]
    if len(cities_list) == 0:
        print()
    elif len(cities_list) == 1:
        print(cities_list[1])
    else:
        print(', '.join(cities_list))

    cur.close()
    db.close()
