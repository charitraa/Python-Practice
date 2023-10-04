from tkinter import *

rabi = Tk()
# size
rabi.geometry("1000x1000")


def happy(event):
    print(f"{event.x}, {event.y}")


# title
rabi.title("Practise")

a = Button(rabi, text="Click me")
a.pack()
a.bind('<Button-1>', happy)
rabi.mainloop()
