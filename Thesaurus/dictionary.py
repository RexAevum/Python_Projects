# Need to import json to be able to access the info in the db
import json
filePath = "db/data.json"
# Can access all of the info in the json file - will hold the dictionary
data = json.load(open(filePath))
print(len(data.keys()))

# Need to import the difflib - used to compare strings and can be used to find simmilar strings to the one provided
# This will be used to suggest other "real" words to the user in case they have entered a word incorrectly 
from difflib import get_close_matches
from typing import Final

# Variables
# Check the number of valid options
NR_OF_OPTIONS: Final = 4
valid = list(range(1, NR_OF_OPTIONS + 1))
doLoop = True

# Function that will print several lines and enumarate them
def printOther (words):
    nr = 0
    for w in words:
        nr = nr + 1
        print("%s) %s" % (nr, w))

# Main loop, that will keep asking user for input until user chooses to exit
while doLoop: 
    # get specific data based on input key, set it to lower case to find a match in data
    word = input(">Find definition of the word (type '\quit' to exit): ")
    foundDef = ""
    # find the word in the data(db) and print it
    if word == r"\quit" :
        # Quit program
        exit()
    elif word.lower() in data: # First need to check if the entered word is in the dic
        # Get the definition from the jason file
        foundDef = data[word.lower()]
    elif word.upper() in data: # accounting for words like NATO
        foundDef = data[word.upper()]
    elif word.title() in data: # accounting for titles
        foundDef = data[word.title()]
    else:
        # if the entered key is not found -> inform user
        #print("The word does not exist in dictionary")

        # Find words that are similar and offer/print to user
        # get_close_matches finds similar strings in a given list
        similarWords = get_close_matches(word, data.keys(), n = NR_OF_OPTIONS)
        print("Word not found!!!", end='\n')
        
        if similarWords != []:
            # Need to account for compleaty wrong input
            while True:
                print("Did you mean:", end='\n')
                printOther(similarWords)
            
                # Get input from user on which option they want to select
                choice = input(">I meant (enter number for option or 'n' for no): ").lower()
                # Check if user wants to exit
                if choice == 'n':
                    break
                # Check if user entered a number
                elif choice.isnumeric():
                    # Check if the entered number is valid
                    if int(choice) in valid and len(similarWords) >= int(choice):
                        altWord = similarWords[int(choice)-1]
                        foundDef = data[altWord]
                        break
                    else:
                        print('The word %s is not a valid option' % choice)
                else:
                    print("--->Invalid input!\n")
            



    # does not account for different items -> can return a list
    # Print the definitions of the entered word
    printOther(foundDef)

    #END


