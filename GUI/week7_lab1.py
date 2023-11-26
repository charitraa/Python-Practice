from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("My Ui")
window.configure(bg="gray")

label = Label(window, text="Registration Form", fg="Black",
              bg="gray", font=("Times New Roman", 20))
label.place(x=160, y=20)


label2 = Label(window, text="FullName", bg="gray",
               fg="Black", font=("Times New Roman", 10))
label2.place(x=80, y=60)

entry = Entry()
entry.place(x=190, y=60)

label2 = Label(window, text="Email", fg="Black",
               bg="gray", font=("Times New Roman", 10))
label2.place(x=80, y=100)

entry1 = Entry()
entry1.place(x=190, y=100)

label3 = Label(window, text="Gender", fg="Black",
               bg="gray", font=("Times New Roman", 10))
label3.place(x=80, y=140)

check_button = Checkbutton(window, text="Male")
check_button.place(x=190, y=140)

check_button1 = Checkbutton(window, text="Female")
check_button1.place(x=250, y=140)

label4 = Label(window, text="Country", fg="Black",
               bg="gray", font=("Times New Roman", 10))
label4.place(x=80, y=180)

variable = StringVar(window)
variable.set("Select Country")

option = OptionMenu(window, variable, "Nepal",
                    "India",
                    "China",
                    "Japan")
option.place(x=190, y=180)
label5 = Label(window, text="Language", fg="Black",
               bg="gray", font=("Times New Roman", 10))
label5.place(x=80, y=220)
check_button3 = Checkbutton(window, text="English")
check_button3.place(x=190, y=220)

check_button4 = Checkbutton(window, text="Nepali")
check_button4.place(x=250, y=220)

button = Button(window, text="Submitt", bg="black", fg="green",
                activebackground="black", activeforeground="green", state=ACTIVE)
button.place(x=200, y=300)


window.geometry("500x500")
window.mainloop()
