# we will learn to create buttons 
# remember when we click button it calls a function that we have to create
from tkinter import *
# creating function for our button
def mybuttonfunction():
    print("You clicked me") # this will print in console not on gui.
root = Tk()
# creating button b1
b1 = Button(root,text="Click here",command=mybuttonfunction)
b1.pack()

root.mainloop()