from tkinter import *

rabi = Tk()
# size
rabi.geometry("1000x1000")
# min size
rabi.minsize(300, 300)
# max size
rabi.maxsize(1200, 1200)
# title
rabi.title("Practise")
# label
rabina = Label(text="hello world")
rabina.pack()
rabi.mainloop()
