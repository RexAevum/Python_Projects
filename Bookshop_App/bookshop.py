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
from tkinter import Entry, Label, Listbox, Button, Scrollbar, StringVar, END, Tk
import backend

"""
Wraper functions 
"""
def get_selected_row(event):
    try:
        # Get the index of currently selected item in the list box
        index = resultList.curselection() # return format is a tuple (x, )
        # To prevent an error due to not having an event passed in, meaning so that the method 
        # does not need to be called in code, just access the global variable
        global itemResult 
        itemResult = resultList.get(index[0])
        # Update the entrie fields with info from selected item in Listbox
        nameEntry.delete(0, END)
        nameEntry.insert(END, itemResult[1])
        authorEntry.delete(0, END)
        authorEntry.insert(END, itemResult[2])
        yearEntry.delete(0, END)
        yearEntry.insert(END, itemResult[3])
        isbnEntry.delete(0, END)
        isbnEntry.insert(END, itemResult[4])
    except IndexError:
        pass


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
    status = backend.insert(nameValue.get(), authorValue.get(), yearValue.get(), isbnValue.get())
    if status:
        view_all()
        nameEntry.delete(0, END)
        authorEntry.delete(0, END)
        yearEntry.delete(0, END)
        isbnEntry.delete(0, END)
    window.update()

def update():
    # Update in the database
    id = itemResult[0]
    status = backend.update(id, nameValue.get(), authorValue.get(), yearEntry.get(), isbnEntry.get())
    if status:
        print("Item {} has been updated".format(id))
        view_all()

def delete():
    """ 
    Another way without using a Listbox event but has the issue that if the user selects the item 
    in the list first, then presses something else and only then presses the delete button, will get
    an index out of bounds/range error. So using the event is safer agains errors but if the user forgets 
    what they selected pressing the delete button could casue the user to delete valid info

    # Get the info from the item selected by user
    index = resultList.curselection() # index start from 0
    item = resultList.get(index[0])
    # Delete the item from db
    status = backend.delete(item[0])
    """
    status = backend.delete(itemResult[0])
    if status:
        print("Item of index {} has been deleted".format(itemResult[0])) # For validation, user will not see
        view_all()

def end():
    exit()
# create a window
window = Tk(className=" Bookshop")

# Create The elements of the UI
# labels
nameLabel = Label(window, text="Title:")
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

closeButton = Button(window, text="Close", command=end, width=11)
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

# Binding a function to a widget event, currently when an item from the Listbox is selected
resultList.bind("<<ListboxSelect>>", get_selected_row)
# Scroll
resultScroll = Scrollbar(window)
resultScroll.grid(row=4, column=3)

# Connecting scrollbar to the list
resultList.configure(yscrollcommand=resultScroll.set)
resultScroll.configure(command=resultList.yview)

view_all()
# Close window
window.mainloop()

