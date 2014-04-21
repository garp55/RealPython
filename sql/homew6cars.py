# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3

# create the connection object


with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS orders")

    c.execute("""CREATE TABLE orders(Make TEXT, Model TEXT, Order_date DATETIME)""")


    corders=[
            ('Ford','Fiesta','2014-01-15'),
            ('Ford','Fiesta','2014-01-25'),
            ('Ford','Fiesta','2014-01-25'),
            ('Ford','Focus','2014-02-11'),
            ('Ford','Focus','2014-02-11'),
            ('Ford','Focus','2014-02-12'),
            ('Ford','Capri','2014-04-15'),
            ('Ford','Capri','2014-05-16'),
            ('Ford','Capri','2014-06-17'),
            ('Honda','Civic','2014-07-15'),
            ('Honda','Civic','2014-07-16'),
            ('Honda','Civic','2014-07-17'),
            ('Honda','FRV','2014-12-15'),
            ('Honda','FRV','2014-12-23'),
            ('Honda','FRV','2014-12-25')
           ] 

    c.executemany("INSERT INTO orders VALUES(?, ?, ? )", corders)

    # retrieve data
    c.execute("SELECT * FROM inventory")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        # output the car make, model and quantity to screen
        print r[0], r[1], "\n", r[2]

        # retrieve order_date for the current car make and model
        c.execute("SELECT order_date FROM orders WHERE make=? and model=?",
                (r[0], r[1]))

        # fetchall() retrieves all records from the query
        order_dates = c.fetchall()

        # output each order_date to the screen
        for order_date in order_dates:
            print order_date[0]
