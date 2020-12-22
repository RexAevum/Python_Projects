import sqlite3

db = r"data\books.db"
# connect to db
def connect():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER UNIQUE)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO Books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()
        return True
    except:
        print("Insert failed")
        conn.commit()
        conn.close()
        return False


def update(id, title, author, year, isbn):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("UPDATE Books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
    return True

def delete(id):
    con = sqlite3.connect(db)
    cur = con.cursor()
    #When using the injection with ?, when querying with only one variable, the touple has to end in a ,
    cur.execute("DELETE FROM Books WHERE id=?", (id,))
    con.commit()
    con.close()
    return True

# Function to search for item in db based on one or more columns
# When using OR all elements have to hav a value or you will get an error so need to set a default value in the search .execute()
def search(title="", author="", year="", isbn=""):
    conn= sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    results = cur.fetchall()
    return results

def view_all():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books")
    results = cur.fetchall()
    conn.close()
    return results


# Call to connect or create db
"""Will be run everytime the library is imported - whenever bookshop is ran """
connect()

# Testing during coding
#insert("Hello World", "John Apple", 1993, 4515464)
#insert("Harry Potter", "J. K. Rowling", 2000, 451546445)
#print(view_all())
#print(search(title="Hello World"))