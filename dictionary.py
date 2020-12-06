# Need to import json
import json
filePath = "db/data.json"
# Can access all of the info in the json file - will hold the dictionary
data = json.load(open(filePath))

while True: 
    # get specific data based on input key
    word = input("The definition of the word (type '\quit' to exit): ")
    foundDef = ""
    # find the word in the data(db) and print it
    if word == r"\quit" :
        exit()
    elif word in data:
        foundDef = data[word.lower()]
    else:
        print("The word does not exist in dictionary")

    # does not account for different items -> can return a list
    lineNum = 0
    for item in foundDef:
        lineNum = lineNum + 1
        print("%s) %s" % (lineNum, item))

    lineNum = 0