#!/usr/bin/python3
''' a script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa '''
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    stName = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=dbname)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states\
                    ON states.id = cities.state_id\
                        WHERE states.name = %s\
                            ORDER BY cities.id ASC", (stName,))
    rows = cur.fetchall()
    first = True
    for row in rows:
        for col in row:
            if not first:
                print(', ', end='')
            print(col, end="")
            first = False
    print()
    cur.close()
    db.close()
