import sqlite3
import random

# create the connection object

with sqlite3.connect("numbers.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS numbers")
    c.execute("""CREATE TABLE numbers(numb INT)""")

    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randrange(1,101),))




done = False

while done == False:

    print "G. Gemiddelde van de nummers"
    print "M. Maximum van de nummers"
    print "I. Minimum van de nummers"
    print "S. Totaal van de nummers"
    print "Q. Quit."
    print
   

    player = raw_input("Your choice? : ")

    if player.upper() == "Q":
        done = True

    
    elif player.upper() == "S":
        c.execute("""SELECT SUM(numb) FROM numbers""")
            
        rip= c.fetchone()[0]
        print "Sum van de nummers: ", rip, "\n"
        

    elif player.upper() == "G":
        c.execute("""SELECT AVG(numb) FROM numbers""")
            
        rip= c.fetchone()[0]
        print "Gemidelde nummer: ", rip, "\n"


    elif player.upper() == "M":
        c.execute("""SELECT MAX(numb) FROM numbers""")
            
        rip= c.fetchone()[0]
        print "Maximum nummer: ", rip, "\n"


    elif player.upper() == "I":
        c.execute("""SELECT MIN(numb) FROM numbers""")
            
        rip= c.fetchone()[0]
        print "Minimum nummer: ", rip, "\n"
        
