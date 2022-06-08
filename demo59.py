from demo57 import main, font1
from tkinter import Label, Message


def motion(ev):
    message1.config(text="move to:[%d,%d]" % (ev.x, ev.y))


label1 = Label(main, text="region", font=font1, bg="#C0FFEE", padx=130, pady=50)
message1 = Message(main, text="display callback", font=font1, fg="#000", bg="#FFFFFF")
label1.pack()
message1.pack()
label1.bind("<Motion>", motion)
main.minsize(400, 300)
main.maxsize(400, 300)
main.mainloop()