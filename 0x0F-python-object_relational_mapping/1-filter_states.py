#!/usr/bin/python3
'''
a script that lists all states with a
name starting with N (upper N) from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)

    cur = db.cursor()
    ''' LIKE isn't case sensiteive, so i used
     BINARY that will handle case sensitivity '''
    cur.execute("SELECT * FROM states WHERE \
                BINARY name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
