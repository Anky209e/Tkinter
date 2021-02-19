from tkinter import *
import tkinter.messagebox as tmsg

def food():
    tmsg.showinfo("Order recieved",f"We have have recived your order of {radio_var.get()}")


root = Tk()
root.title("Radio buttons")
root.geometry("400x350")
root.config(bg="grey22")

radio_var = StringVar()
radio_var.set("radio")

label = Label(root,text="What do you like?",justify=LEFT).pack()
radio = Radiobutton(root,text="Apple",variable=radio_var,value="apple",padx=10).pack()
radio = Radiobutton(root,text="Mango",variable=radio_var,value="mango",padx=10).pack()
radio = Radiobutton(root,text="Banana",variable=radio_var,value="Banana",padx=10).pack()

button = Button(root,text="GET NOW",command=food).pack()
root.mainloop()