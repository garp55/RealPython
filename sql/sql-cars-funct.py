# SQLite Functions

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT * FROM inventory""")

    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], "\n", r[2], "\n"

        c.execute("""SELECT count(Order_date) FROM orders WHERE Make=? AND Model=?""",(r[0],r[1]))
            
        orderc= c.fetchone()[0]
        print "Aantal orders: ", orderc, "\n"
        
            
