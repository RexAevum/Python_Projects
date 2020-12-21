"""
The program will cover how to connect to a postgreSQL and psycopg2 db and how to perform basic actions - create, insert, delete, update
Code is very simmilar to the sqlite code, except using psycopg2 insted of sqlite3

MAIN DIFFERENCE:
    1) Uses port to connect to db insted of file like SQLite --> have to have infor of the server to connect
    2) When using variables for sql injection, cannot use '?' but instead have to use '%s' to inject values
"""
import psycopg2
# To connect to postgresql database the given info is needed
    # dbname='Test_db' --> The name of the DB that you are connecting to
    # user='postgres' --> The user name of the db holder in postgreSQL
    # password='admin2020' --> The paswrod to access the db
    # host='localhost' --> The ip address of the server you are connecting to (localhost - runnin on current computer)
    # port='5432' --> the specified port on which to connect to the server
db = "dbname='Test_db' user='postgres' password='admin2020' host='localhost' port='5432'"

"""Create a table """
def create_table():
    # 1)Connect to DB - a remote db, insted of a file   
    con = psycopg2.connect(db)
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
        con = psycopg2.connect(db)
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS %s" % name)
        con.commit()
        con.close()

def delete(item):
    con = psycopg2.connect(db)
    cur = con.cursor()
    #When using the injection with ?, when querying with only one variable, the touple has to end in a ,
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    con.commit()
    con.close()

def update(item, quantity, price):
    con = psycopg2.connect(db)
    cur = con.cursor()
    cur.execute("UPDATE store SET amount=%s, price=%s WHERE item=%s", (quantity, price, item))
    con.commit()
    con.close()

"""Insert new itmes into the created table """
def insert_item(item="New Item", quantity=0, price=0.0):
    con = psycopg2.connect(db)
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    # To get data from the query 
    rows = cur.fetchall()
    con.close()
    return rows

# interact with db
create_table()
insert_item("Coffee", 10, 3.75)
insert_item("Orange", 2, 0.40)
insert_item("Car", 100, 10000.0)
update("Car", 50, 20000.0)
delete("Coffe")
print(view())