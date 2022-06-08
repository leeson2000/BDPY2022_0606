from demo57 import main, font1
from tkinter import Radiobutton, Label, IntVar


def func1():
    label1.config(text='.net core mvc')


def func2():
    label1.config(text="spring boot")


def funcX():
    if sel1.get() == 1:
        label1.config(text='.net core mvc.......')
        ##pass
    elif sel1.get() == 2:
        label1.config(text="spring boot.......")
        ##pass

sel1 = IntVar()
sel1.set(1)
rb1 = Radiobutton(main, text="C#", value=1, font=font1, variable=sel1, command=funcX)
rb2 = Radiobutton(main, text="Java", value=2, font=font1, variable=sel1, command=funcX)
label1 = Label(main, font=font1, text="status")
main.maxsize(400, 300)
main.minsize(400, 300)
rb1.pack()
rb2.pack()
label1.pack()
main.mainloop()
