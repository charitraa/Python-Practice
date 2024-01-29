from tkinter import *
a = Tk()
a.title("Attribute")
a.geometry("733x433")
# Label Attribute

b = Label(text="Welcome to Pycham Welcome to PychamWelcome to  \nPychamWelcome to PychamWelcome to  \nPychamWelcome to PychamWelcome to \nPycham",
          bg="black", foreground="white", padx=30, pady=30, font=("Arial", 20, "bold"), borderwidth=10, relief=SUNKEN)

# side
b.pack(side="left", anchor="sw", fill="y", padx=100, pady=100)


a.mainloop()
