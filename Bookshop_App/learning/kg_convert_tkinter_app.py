from tkinter import * # lib for GUI

# init the GUI
# Start by creating a window
window = Tk(className=" KG Converter")

# The main functionality goes here --------------------------------

# a dunction to excecute when a button is pressed
def press():
    print(entry1_value.get())
    textGrams.insert(END, entry1_value.get())
    entry1.delete(1.0, END)

def clear():
    """ To reset the text field using the .delete(first, last) command , for start need to use 1.0 to start from the first char"""
    textGrams.delete(1.0, END)
    textPounds.delete(1.0, END)
    textOunces.delete(1.0, END)

def convert():
    # Covert km to miles
    # .get() returns a string
    try:
        # Get value from entry field
        kg = float(entry1_value.get())
    except:
        kg = 0.0

    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274

    # Inster into text fields after clearing the data
    clear()
    textGrams.insert(index=END, chars=grams)
    textPounds.insert(index=END, chars=pounds)
    textOunces.insert(index=END, chars=ounces)

# Create a button
button1 = Button(window, text="Convert", command=convert)
# Adjust the layout of the button on the window
button1.grid(row=0, column=2)

# Create a user input field
# Need to create a container for the entered strings for referencing 
entry1_value = StringVar()
entry1 = Entry(window, textvariable=entry1_value)
entry1.grid(row=0, column=1)

# Create a text widget/field
textGrams = Text(window, height=1, width=20)
textGrams.grid(row=2, column=0)

textPounds = Text(window, height=1, width=20)
textPounds.grid(row=2, column=1)

textOunces = Text(window, height=1, width=20)
textOunces.grid(row=2, column=2)

# Create a label
label = Label(window, text="KG -->>")
label.grid(row=0, column=0)

labelGrams = Label(window, text="Grams (g)")
labelGrams.grid(row=1, column=0)

labelPounds = Label(window, text="Pounds (lb)")
labelPounds.grid(row=1, column=1)

labelOunces = Label(window, text="Ounces (oz)")
labelOunces.grid(row=1, column=2)

#-------------------------------------------------------------------------------
# To make sure the window stays on screen till user closeses it 
# Is always lokated at the end of code
window.mainloop()