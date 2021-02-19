from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.config(bg="grey22")
root.geometry("500x450")
root.title("Dialouge boxes")
#------------------------------------------
# There are functions or methods available in the messagebox widget.

# showinfo(): Show some relevant information to the user.
# showwarning(): Display the warning to the user.
# showerror(): Display the error message to the user.
# askquestion(): Ask question and user has to answered in yes or no.
# askokcancel(): Confirm the user’s action regarding some application activity.
# askyesno(): User can answer in yes or no for some action.
# askretrycancel(): Ask the user about doing a particular task again or not.

#----------------------------------------------------

def myfunction():
    pass

def helpfunction():
    tmsg.showinfo(title="Help",message="This is your help.")

youmenubar = Menu(root,bg="grey22")
m2 = Menu(youmenubar,tearoff=0)

m2.add_command(label="Help",command=helpfunction)

youmenubar.add_cascade(label="Edit",menu=m2)
root.config(menu=youmenubar)


root.mainloop()