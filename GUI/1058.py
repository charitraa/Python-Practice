from tkinter import *

rabi = Tk()
rabi.geometry("655x333")
# gui logicr


def getValue():
    print(aa.get())
    print(bb.get())


a = Label(rabi, text="Username")
password = Label(rabi, text="Password")
a.grid()
password.grid(row=1)


aa = Entry(rabi, textvariable=StringVar())
bb = Entry(rabi, textvariable=StringVar())

aa.grid(row=0, column=1)
bb.grid(row=1, column=1)
Button(text="Submit", command=getValue).grid()
rabi.mainloop()
