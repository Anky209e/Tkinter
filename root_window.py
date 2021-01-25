#  creating our root window
from tkinter import *  # importing all
#------------------------------
root = Tk() # (root is name of window you can name any
#  but root is uniform for all programmers)
#------------------------------
root.title("My gui") # for title of app or gui
#------------------------------
# creating geometry of window(root is name of window)
root.geometry("400x350") # width x height of window(root) 

#setting minimum size of window(root)
root.minsize(350,250) # width,height
#setting max size
root.maxsize(600,550) # width,height


root.mainloop()