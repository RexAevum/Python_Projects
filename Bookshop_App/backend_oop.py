import sqlite3
data = r"data\books.db"

class Database:
    # Class variiables
    db = None
    con = None
    cur = None

    # This method is run once a Database object is created
    def __init__(self, path=data):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER UNIQUE)")
        self.con.commit()

    def insert(self, title, author, year, isbn):
        try:
            self.cur.execute("INSERT INTO Books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
            self.con.commit()
            return True
        except:
            print("Insert failed")
            return False


    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE Books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.con.commit()
        return True

    def delete(self, id):
        #When using the injection with ?, when querying with only one variable, the touple has to end in a ,
        self.cur.execute("DELETE FROM Books WHERE id=?", (id,))
        self.con.commit()
        return True

    # Function to search for item in db based on one or more columns
    # When using OR all elements have to hav a value or you will get an error so need to set a default value in the search .execute()
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM Books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        results = self.cur.fetchall()
        return results

    def view_all(self):
        self.cur.execute("SELECT * FROM Books")
        results = self.cur.fetchall()
        return results

    # This method is run once the Database object is destroyed 
    def __del__(self):
        self.con.close()
    