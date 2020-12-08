"""
Program will connect to a remote db and access a dictionary table. The user will enter a word and the app will
return defenitions for the word or offer simmilar words in case the word is not correct
"""
# other imports
from difflib import get_close_matches

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

doLoop = True
while doLoop:
    # Get user input for word
    word = input(r"Enter word or '\quit' to quit: > ")
    if word == r'\quit':
        exit()

    # after that, we can perform queries using the cursor
    # Write the query that will be passed to the db
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    
    # Then fetch the results for the query from the db
    results = cursor.fetchall()

    if results:
        for w in results:
            print(w[1])
    else:
        # if no result was found - offer similar words
        print("-> Word does not exist")
        command = "SELECT * FROM Dictionary WHERE Expression LIKE '{}%'".format(word[0])
        similarQuery = cursor.execute(command)
        similarResults = cursor.fetchall()
        # extract first object from each touple for comparison
        altResults = []
        for opt in similarResults:
            if opt[0] not in altResults:
                altResults.append(opt[0])
        #print(similarResults)
        options = get_close_matches(word, altResults, n=5, cutoff=0.8)
        print(options)

        if options:
            print("Did you mean: ")
            for w in options:
                print(">%s" % w)
                
