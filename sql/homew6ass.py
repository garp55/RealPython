import sqlite3
import random

# create the connection object

with sqlite3.connect("numbers.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS numbers")
    c.execute("""CREATE TABLE numbers(numb INT)""")

    numl=[]
    for i in range(100):
        number=random.randrange(1,101)
        numl.append(number)
    
    c.executemany("INSERT INTO numbers VALUES(?)", numl)
