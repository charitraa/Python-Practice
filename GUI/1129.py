from tkinter import *
from PIL import Image, ImageTk
a = Tk()
a.title("challenge")
a.geometry("1000x1000")
# add image file
b = PhotoImage(
    file="P:\\Code\\Python\\Python Practise\\GUI\\Untitled design (12).png")
# add image to label to show
ccc = Label(image=b)
ccc.pack()

# for jpg image

image = Image.open(
    "P:\\Code\\Python\\Python Practise\\GUI\\Untitled design (12).png")
photo = ImageTk.PhotoImage(image)
ccc = Label(image=photo)
ccc.pack()

a.mainloop()
