#!/usr/bin/python3
"""a script that takes in the name of a state
as an argument and lists all cities of that state"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    # connect database to python file
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    # create cursor to exec queries using SQL
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities AS c \
                INNER JOIN states AS s ON c.state_id = s.id\
                WHERE s.name = '{}' \
                ORDER BY c.id ASC""".format(argv[4]))
    rows = cur.fetchall()
    for i, row in enumerate(rows, start=0):
        if i != 0:
            print(", ", end="")
        print(row[0], end="")
    print("")
    cur.close()
    db.close()
