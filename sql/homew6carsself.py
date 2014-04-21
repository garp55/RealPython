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


    c.execute("""SELECT * FROM inventory""")

    rows= c.fetchall()
 
    for r in rows:
         print "Make and Model: "+ r[0], r[1]  
         print "Quanity: " + str(r[2]) + "\n"
         

         c.execute("""SELECT Order_date FROM orders WHERE Make = ? AND Model=?""",(r[0],r[1]))
    

         ruws= c.fetchall()

         for r in ruws:
             print "Orderdate: "+ r[0]

         print "\n"
    
             

              

        
