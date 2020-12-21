"""
The program will store book information on a db.
The information stored in the db:
    title - name of book
    Author - author of book
    Year - year of publication
    ISBN - unique id

User will be able to:
    View all record
    Search for an entry
    Add entry
    Update entry
    remove entry 
    close program

 """
from tkinter import *
import backend


"""
Wraper functions 
"""
def view_all():
    # Clear field so you do not get duplicates
    resultList.delete(0, END)
    # Get info from db
    results = backend.view_all()
    for x in results:
        resultList.insert(END, x)
def search():
    resultList.delete(0, END)
    # Since the Entry field returns a StringVar() object, before it can be passed to do query need to use the
    # .get() command to the correct type which is just str(), not StringVar()
    results = backend.search(nameValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
    for x in results:
        resultList.insert(END, x)
def insert():
    return None
def update():
    return None
def delete():
    return None

# create a window
window = Tk(className=" Bookshop")

# Create The elements of the UI
# labels
nameLabel = Label(window, text="Name:")
nameLabel.grid(row=0, column=0)

authorLabel = Label(window, text="Author:")
authorLabel.grid(row= 1, column=0)

yearLabel = Label(window, text="Year:")
yearLabel.grid(row= 2, column=0)

isbnLabel = Label(window, text="ISBN:")
isbnLabel.grid(row= 3, column=0)

# Buttons
viewAllButton = Button(window, text="View All", command=view_all, width=22)
viewAllButton.grid(row= 0, column=2, columnspan=2)

searchButton = Button(window, text='Search Entry', command=search, width=22)
searchButton.grid(row= 1, column=2, columnspan=2)

addButton = Button(window, text="Add", command=insert, width=11)
addButton.grid(row= 2, column=2)

updateButton = Button(window, text="Update", command=update, width=11)
updateButton.grid(row= 3, column=2)

deleteButton = Button(window, text="Delete", command=delete, width=11)
deleteButton.grid(row= 2, column=3)

closeButton = Button(window, text="Close", command=exit, width=11)
closeButton.grid(row= 3, column=3)

# Entry field
nameValue = StringVar()
nameEntry = Entry(window, textvariable=nameValue)
nameEntry.grid(row= 0, column=1)

authorValue = StringVar()
authorEntry = Entry(window, textvariable=authorValue)
authorEntry.grid(row= 1, column=1)

yearValue = StringVar()
yearEntry = Entry(window, textvariable=yearValue)
yearEntry.grid(row= 2, column=1)

isbnValue = StringVar()
isbnEntry = Entry(window, textvariable=isbnValue)
isbnEntry.grid(row= 3, column=1)

# List box
resultList = Listbox(window, height=12, width=60)
resultList.grid(row= 4, column=0, columnspan=3)

# Scroll
resultScroll = Scrollbar(window)
resultScroll.grid(row=4, column=3)

# Connecting scrollbar to the list
resultList.configure(yscrollcommand=resultScroll.set)
resultScroll.configure(command=resultList.yview)

# Close window
window.mainloop()

