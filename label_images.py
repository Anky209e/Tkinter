from tkinter import *
root = Tk()

#--------------------Creating label-------------------

# label is a widget to write or show text in root(window)
label1 = Label(text="This is our Tkinter gui",background="grey",fg="Blue",relief=SUNKEN)
label1.pack() # you have to always pack a widget to display in tkinter

# --------------------displaying images ---------------------------
aot_image = PhotoImage(file="demo.png")
# we have to put image in label to show it cant be packed
label2 = Label(image=aot_image)
# then pack label
label2.pack()
# -------------------important label atrributes-----------
# text="" - it add text
# bd="color" - add backgroung color
# fg="" - add foreground
# font - sets font
# padx - padding at x
# pady - padding at y
# relief - borderstyle (SUNKEN,RAISED,GROOVE,RIDGE)
# attribute in pack
#  anchor = "sw" direction in window(here "sw" means south-west)



root.mainloop()