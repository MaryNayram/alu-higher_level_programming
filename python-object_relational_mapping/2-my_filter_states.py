#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC""".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
