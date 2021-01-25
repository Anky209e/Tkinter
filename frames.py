# we will create frames in our root window and use them as 
#  seprate small windows in root(window)
from tkinter import *
# here root is our main window
root = Tk()
root.title("Frame Learning")
root.geometry("400x350")

# creating frame f1 in root window
f1 = Frame(root,bg="grey",borderwidth=6)
f1.pack(side=LEFT,fill="y",pady=33)
label_in_f1 = Label(f1,text="f1 frame in root")
label_in_f1.pack()

# creating frame f2 in root
f2 = Frame(root,bg="blue",borderwidth=6)
f2.pack(side=TOP,fill="x",padx=0)
label_f2 = Label(f2,text="frame f2 in root")
label_f2.pack()





root.mainloop()