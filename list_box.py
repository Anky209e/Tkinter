from tkinter import *

def add():
    global i
    list_box.insert(ACTIVE,f"{i}")
    i+=1
i = 0
root = Tk()
root.geometry("400x350")
root.title("Listbox")
root.config(bg="grey22")

list_box = Listbox(root)
list_box.pack()
list_box.insert(END,"First Item")

button = Button(root,text="ADD",command=add).pack()


root.mainloop()