#!/usr/bin/python3
''' a script that lists all cities from the database hbtn_0e_4_usa '''
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
    cur.execute("SELECT id, city.name, state.name FROM cities \
                INNER JOIN states \
                    WHERE states.id = cities.states_id \
                        ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
