from tkinter import *

rabi = Tk()
# size
rabi.geometry("1000x1000")

# title
rabi.title("Practise")
# frame
f1 = Frame(rabi, bg="black", borderwidth=3, relief=SUNKEN)
# to add the label in tkinter
f1.pack(side="left", fill="y", pady=200)
f2 = Frame(rabi, bg="black", borderwidth=8, relief=SUNKEN)
f2.pack(side="top", fill="x")
l = Label(f1, text="Project Tkinter")
l.pack(pady=42)
l1 = Label(f2, text="Project Ravi")
l1.pack(pady=42)
rabi.mainloop()
