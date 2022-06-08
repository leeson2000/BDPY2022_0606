import tkinter
from tkinter import font, Label, Button
from tkinter.font import Font
from pprint import pprint

counter = 0
counter2 = [0]


def func1():
    global counter
    counter = counter + 1
    counter2[0] += 1
    label1.config(text="counter=%d" % counter)
    label2.config(text="counter2=%d" % counter2[0])
    # print("something happen")


def func2():
    global counter
    counter = 0
    counter2[0] = 0
    label1.config(text="counter=%d" % counter)
    label2.config(text="counter2=%d" % counter2[0])


main = tkinter.Tk()
font1 = Font(family='Reem Kufi', size=24)

if __name__ == '__main__':

    for f in font.families():
        pprint(f)

    label1 = Label(main, text="hello gui", font=font1, fg='#C0FFEE', bg='#000', padx=20)
    label2 = Label(main, text="hello gui2", font=font1, fg='#C0EEFF', bg='#000', padx=20)
    button1 = Button(main, text="按了加1", font=font1, fg='#FFC0EE', bg='#444', command=func1)
    button2 = Button(main, text="歸零", font=font1, fg='#FFEEC0', bg='#444', command=func2)
    label1.pack()
    label2.pack()
    button1.pack()
    button2.pack()
    main.minsize(400, 300)
    main.maxsize(400, 300)
    main.mainloop()