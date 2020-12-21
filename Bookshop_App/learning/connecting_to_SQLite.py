"""
The program will cover how to connect to a SQLite db file and how to perform basic actions - create, insert, delete, update
"""

import sqlite3

"""Create a table """
def create_table():
    # 1)Connect to DB
    # .connect({name of db file}) woll either open the db or create new one with the given name
    con = sqlite3.connect("lite.db")

    # 2) Create a cursor object
    cursor = con.cursor()

    # 3) Write an SQL query
    # Creating a table woth the specified columns
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, amount INTEGER, price REAL)")

    # Add items to the existing table - make sure the same items is not readded every time ->> place it in its own function
    """cursor.execute("INSERT INTO store VALUES ('Wine Glass', 2, 10.99)")"""


    # 4) Commit changes - only when data is updated
    con.commit()

    # 5) Close db connection
    con.close()

def delete_table(name):
    if not ";" in name: # To prevent the injecting of additional instructions
        con = sqlite3.connect("lite.db")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS %s" % name)
        con.commit()
        con.close()

def delete(item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    #When using the injection with ?, when querying with only one variable, the touple has to end in a ,
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    con.commit()
    con.close()

def update(item, quantity, price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET amount=?, price=? WHERE item=?", (quantity, price, item))
    con.commit()
    con.close()

"""Insert new itmes into the created table """
def insert_item(item="New Item", quantity=0, price=0.0):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")

    # To get data from the query 
    rows = cur.fetchall()
    con.close()
    return rows


delete_table('store')
create_table()
insert_item(item="Water Bottle", quantity=10, price=2.00)
print(view())
#delete("Water Bottle")
update("Water Bottle", 20, 1.00)
print(view())