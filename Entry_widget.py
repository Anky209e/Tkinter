from tkinter import *


# function of submit button

def submit():
    pass
    


root = Tk()
#-----creating entry widget-----
# variables in tkinter
# StringVar,DoubleVar,IntVar,BooleanVar

userid = StringVar()
passid = StringVar()
# label
userlabel = Label(root,text="Username").grid()
passlabel = Label(root,text="Password").grid()

#----widget 
userentry = Entry(root,textvariable=userlabel).grid(row=0,column=1)
passentry = Entry(root,textvariable=passlabel).grid(row=1,column=1)

# ---submit--
srchbtn = Button(root,text="Submit",command=submit).grid(row=3,column=1)

# label for userinfo
label1 = Label(root,text="Enter above details").grid(row=4,column=0)





root.mainloop()