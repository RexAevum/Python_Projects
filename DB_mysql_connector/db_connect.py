# librarry to connect to a mysql data base
import mysql.connector

# First need to establish the connection with db
con = mysql.connector.connect(
    # Give the credentials for connectiong to db
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# After establishing a connection, need to create a cursor to interact with the tables in the db
cursor = con.cursor()

# after that, we can perform queries using the cursor
# Write the query that will be passed to the db
query = cursor.execute("SELECT * FROM Dictionary")
# Then fetch the results for the query from the db
results = cursor.fetchall()

print(results)