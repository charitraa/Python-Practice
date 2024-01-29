from tkinter import *

rabi = Tk()
# size
rabi.geometry("1000x1000")

# title
rabi.title("Practise")

can_widget = Canvas(rabi, width=500, height=500)
can_widget.pack()
can_widget.create_line(20, 100, 500, 100, fill="red")
can_widget.create_text(200, 200, text="python")
rabi.mainloop()
