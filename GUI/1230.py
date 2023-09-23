from tkinter import *

rabi = Tk()
# size
rabi.geometry("1000x1000")

# title
rabi.title("Practise")


def hello():
    print("Hello")


frame = Frame(rabi, borderwidth=6, bg="red", relief=SUNKEN)
frame.pack(side="left", anchor="nw")

b1 = Button(frame, fg="red", text="Click!", command=hello)
b1.pack(side="left", padx=20)

rabi.mainloop()
