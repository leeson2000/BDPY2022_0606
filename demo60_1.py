from demo57 import main, font1
from tkinter import Radiobutton, Label


def func1():
    label1.config(text='.net core mvc')


def func2():
    label1.config(text="spring boot")


rb1 = Radiobutton(main, text="C#", value=1, font=font1, command=func1)
rb2 = Radiobutton(main, text="Java", value=2, font=font1, command=func2)
label1 = Label(main, font=font1, text="status")
main.maxsize(400, 300)
main.minsize(400, 300)
rb1.pack()
rb2.pack()
label1.pack()
main.mainloop()
