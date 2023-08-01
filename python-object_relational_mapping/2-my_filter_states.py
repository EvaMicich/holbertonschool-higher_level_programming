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
    state_arg = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
    WHERE name LIKE '{}';".format(state_arg))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
