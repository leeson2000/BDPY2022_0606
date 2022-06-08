import tkinter

import tkinter
from tkinter import font, Label
from tkinter.font import Font
from pprint import pprint

main = tkinter.Tk()
for f in font.families():
    pprint(f)

font1 = Font(family='Reem Kufi', size=24)

label1 = Label(main, text="hello gui", font=font1)
label1.pack()
main.mainloop()