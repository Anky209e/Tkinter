from tkinter import *


root = Tk()

root.geometry("500x450")
root.title("Sliders")
root.config(bg="grey22")

myslide_vertical = Scale(root,from_ =0,to=100)
myslide_vertical.pack()

myslider_Horizontal = Scale(root,from_=0,to=100,orient=HORIZONTAL,bg="grey22")
myslider_Horizontal.set(15)
myslider_Horizontal.pack()


root.mainloop()