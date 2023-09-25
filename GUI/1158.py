from tkinter import *

rabi = Tk()
rabi.geometry("655x333")
rabi.title("My first GUi")


def get():
    rabi = Tk()
    rabi.geometry("300x333")
    name = Label(rabi, text="Name").grid(row=1, column=2)
    phone = Label(rabi, text="Phone").grid(row=2, column=2)
    gender = Label(rabi, text="Gender").grid(row=3, column=2)

    emergency = Label(rabi, text="Emergency").grid(row=4, column=2)

    payment = Label(rabi, text="Payment").grid(row=5, column=2)

    name1 = Entry(rabi, textvariable=StringVar())
    name1.grid(row=1, column=3)
    phone1 = Entry(rabi, textvariable=StringVar())
    phone1.grid(row=2, column=3)
    gender1 = Entry(rabi, textvariable=StringVar())
    gender1.grid(row=3, column=3)
    emergency1 = Entry(rabi, textvariable=StringVar())
    emergency1.grid(row=4, column=3)
    payment1 = Entry(rabi, textvariable=StringVar())
    payment1.grid(row=5, column=3)
    Checkbutton(text="want to prebook your meals",
                variable=IntVar()).grid(row=6, column=3)
    Button(rabi, text="Submit to HArry Tarvels",
           command=get).grid(row=8, column=3)


# gui logic
Label(rabi, text="Welcome to Tarvels",
      font="comicsansms 12 bold").grid(row=0, column=3, pady=20)
name = Label(rabi, text="Name").grid(row=1, column=2)
phone = Label(rabi, text="Phone").grid(row=2, column=2)
gender = Label(rabi, text="Gender").grid(row=3, column=2)

emergency = Label(rabi, text="Emergency").grid(row=4, column=2)

payment = Label(rabi, text="Payment").grid(row=5, column=2)

name1 = Entry(rabi, textvariable=StringVar())
name1.grid(row=1, column=3)
phone1 = Entry(rabi, textvariable=StringVar())
phone1.grid(row=2, column=3)
gender1 = Entry(rabi, textvariable=StringVar())
gender1.grid(row=3, column=3)
emergency1 = Entry(rabi, textvariable=StringVar())
emergency1.grid(row=4, column=3)
payment1 = Entry(rabi, textvariable=StringVar())
payment1.grid(row=5, column=3)
Checkbutton(text="want to prebook your meals",
            variable=IntVar()).grid(row=6, column=3)
Button(rabi, text="Submit",
       command=get).grid(row=8, column=3)


rabi.mainloop()
