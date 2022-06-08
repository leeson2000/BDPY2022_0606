from demo57 import main, font1
from tkinter import Label


def func1(ev):
    label2.config(text="leave from:[%d,%d]" % (ev.x, ev.y))


def func2(ev):
    label2.config(text="enter into:[%d,%d]" % (ev.x, ev.y))


label1 = Label(main, text="region", font=font1, bg="#C0FFEE", padx=50, pady=50)
label2 = Label(main, text="display callback", font=font1, fg="#000", bg="#FFFFFF")
label1.pack()
label2.pack()
label1.bind('<Leave>', func1)
label1.bind('<Enter>', func2)
main.minsize(400, 300)
main.maxsize(400, 300)
main.mainloop()