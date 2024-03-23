#!/usr/bin/python3
''' script should take 4 arguments: mysql username, mysql password,
database name and state name searched
(safe from MySQL injection) '''
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE \
                BINARY name = %s ORDER BY states.id ASC", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
