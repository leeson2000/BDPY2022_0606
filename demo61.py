from demo57 import main, font1
from tkinter import Radiobutton, Label, IntVar, Scale, X


def func1(ev):
    # print("ev=", ev)
    label1.config(text="value=%d" % int(ev))


scale1 = Scale(main, label="volumn", orient='horizontal', from_=0, to=1200, font=font1, command=func1)
label1 = Label(main, text="display value", font=font1)
label1.pack()
scale1.pack(fill=X)
main.maxsize(400, 300)
main.minsize(400, 300)

main.mainloop()