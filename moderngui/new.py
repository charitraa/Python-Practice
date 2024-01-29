from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.geometry("300x400")

btn = customtkinter.CTkButton(master=root, text="hello world")
btn.place(x=50, y=50)

root.mainloop()
