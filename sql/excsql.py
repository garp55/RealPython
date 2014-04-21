# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3

# create the connection object

conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()
try:

    updates= [('Ford','Fiesta', 345),('Ford','Focus', 345),('Ford','Capri', 345),('Honda','Civic', 345),('Honda','FRV', 345)]     
    # insert data
    cursor.executemany("INSERT INTO inventory VALUES(?,?,?)",updates)

    # update data
    c.execute("UPDATE inventory SET Quantity = 999 WHERE Make='Honda'")
       
    # commit the changes
    conn.commit()

    c.execute("SELECT * FROM inventory")

    c.execute("SELECT * FROM inventory WHERE Make='Ford'")

except sqlite3.OperationalError as error:
    print "Something went wrong, got an errormessage", error

# close the database connection
conn.close()
