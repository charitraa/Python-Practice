from tkinter import *

rabi = Tk()
rabi.geometry("655x333")
# gui logicr

a = Label(rabi, text="Username")
password = Label(rabi, text="Password")
a.grid()
password.grid(row=1)

c = StringVar()
d = StringVar()

aa = Entry(rabi, textvariable=c)
bb = Entry(rabi, textvariable=d)

rabi.mainloop()
