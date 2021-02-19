from tkinter import *
root = Tk()
root.geometry("450x400")
root.title("Scrollbar")
root.config(bg="grey22")
scrollbar = Scrollbar(root)


list_box = Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    list_box.insert(END,str(i))
list_box.pack()
scrollbar.config(command=list_box.yview)
scrollbar.pack(fill=Y,side=RIGHT)

root.mainloop()