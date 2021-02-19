from tkinter import *
from typing import ContextManager

root = Tk()
def myfunction():
    pass


root.geometry("500x450")
root.config(bg="grey22")
root.title("Menu and submenu")
#------------------------------------------------
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myfunction)
# mymenu.add_command(label="Exit",command=myfunction)
# root.config(menu=mymenu)
#-----------------------------------------

youmenubar = Menu(root,bg="grey22")

m1 = Menu(youmenubar,tearoff=0)
m1.add_command(label="Save",command=myfunction)
m1.add_command(label="Save as",command=myfunction)
m1.add_separator()
m1.add_command(label="Print",command=myfunction)
youmenubar.add_cascade(label="File",menu=m1)



m2 = Menu(youmenubar,tearoff=0)
m2.add_command(label="Cut",command=myfunction)
m2.add_command(label="Copy",command=myfunction)
m2.add_command(label="Paste",command=myfunction)
m2.add_separator()
m2.add_command(label="Insert",command=myfunction)
m2.add_command(label="Draw",command=myfunction)

youmenubar.add_cascade(label="Edit",menu=m2)
root.config(menu=youmenubar)




root.mainloop()