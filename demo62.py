from demo57 import main, font1
from tkinter import Radiobutton, Label, IntVar, Scale, X, Entry, Button


def display(event):
    print(event)
    l1.config(text=f"input as:{e1.get()}")


l1 = Label(main, font=font1, text="some message")
e1 = Entry(main, font=font1)
b1 = Button(main, font=font1, text="submit")
l1.pack()
e1.pack()
b1.pack()
e1.bind("<Return>", display)
b1.bind("<Button-1>", display)
main.maxsize(400, 300)
main.minsize(400, 300)

main.mainloop()