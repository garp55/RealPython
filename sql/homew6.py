# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3

# create the connection object


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    try:

        updates= [('Ford','Fiesta', 345),('Ford','Focus', 345),('Ford','Capri', 345),('Honda','Civic', 345),('Honda','FRV', 345)]     
        # insert data
        c.executemany("INSERT INTO inventory VALUES(?,?,?)",updates)

        # update data
        c.execute("UPDATE inventory SET Quantity = 999 WHERE Make='Honda'")
       
        

    except sqlite3.OperationalError as error:
        print "Something went wrong, got an errormessage", error

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    print"\n Eerst alles: \n"

    for r in rows:
        print r[0], r[1], r[2]

    c.execute("SELECT * FROM inventory WHERE Make='Ford'")

    rows = c.fetchall()

    print"\n\n Daarna alleen de fordjes \n"

    for r in rows:
        print r[0], r[1], r[2]

  
