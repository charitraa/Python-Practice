
from tkinter import *
from PIL import ImageTk, Image


from tkinter import *
# from PIL import ImageTk, Image


def submit():
    # Get values from entry widgets and variables
    full_name = enter_1.get()
    email = enter_3.get()
    gender = "Male" if vars.get() == 1 else "Female"
    country = cv.get()
    language_english = "english" if vars1.get() == 1 else ""
    language_nepali = "Nepali" if vars2.get() == 1 else ""

# Display the valuss in the current page(optional)
    result_label.config(
        text=f"Full name: {full_name}\n Email:{email}\nGender: {gender}\nCountry: {country}\n Languages: {language_english}, {language_nepali}")

   # Open a new window for the next page
    new_window = Toplevel(root)
    new_window.title("Next Page")

    # Display the vlaues in the new window
    result_label_next_page = Label(
        new_window, text=f"Full Name: {full_name}\nEmail: {email}\nGender: {gender}\nCountry: {country}\n Languages: {language_english},{language_nepali} ")
    result_label_next_page.pack()


# Creating the object 'root' of the Tk()
root = Tk()

# Using the Geometry method to set certain dimensions
root.geometry("550x550")

# Using title method to give the title to the window
root.title('Registration form')

# Now, we will use 'Label' method to add a widget in the Registration Form and also use place() method to set its position.
lbl_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
lbl_0.place(x=90, y=60)

# Using 'Label' widget to create Full name label and using place() method to set its position.
lbl_1 = Label(root, text="FullName", width=20, font=("bold", 10))
lbl_1.place(x=80, y=130)

# Using Entry widget to make a text entry box for accepting the input string in text from the user.
enter_1 = Entry(root)
enter_1.place(x=240, y=130)

# Using 'Label' widget to create Email label and using place() method to set its position.
lbl_3 = Label(root, text="Email", width=20, font=("bold", 10))
lbl_3.place(x=68, y=180)

# Using Entry widget to make a text entry box for accepting the input string in text from the user.
enter_3 = Entry(root)
enter_3.place(x=240, y=180)

# Using 'Label' widget to create Gender label and using place() method to set its position.
lbl_4 = Label(root, text="Gender", width=20, font=("bold", 10))
lbl_4.place(x=70, y=230)

# Using variable 'vars' to store the integer value, which by default is 0
vars = IntVar()

# Using Radio button widget to create an option choosing button and using place() method to set its position.
Radiobutton(root, text="Male", padx=5, variable=vars,
            value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20,
            variable=vars, value=2).place(x=290, y=230)

# Using 'Label' widget to create Countries label and using place() method, set its position.
lbl_5 = Label(root, text="Country", width=20, font=("bold", 11))
lbl_5.place(x=70, y=280)

# This creates a list of countries available in the dropdown list.
list_of_cntry = ['Nepal', 'Canada', 'US', 'Germany', 'UK']

# The variable 'cv' is introduced to store the String Value, which by default is (empty) ""
cv = StringVar()
drplist = OptionMenu(root, cv, *list_of_cntry)
drplist.config(width=15)
cv.set('Select your Country')
drplist.place(x=240, y=280)

# Using 'Label' widget to create Language label and using place() method, set its position.
lbl_6 = Label(root, text="Language", width=20, font=('bold', 10))
lbl_6.place(x=75, y=330)

# The new variable 'vars1' is created to store Integer Value, which by default is 0.
vars1 = IntVar()
vars2 = IntVar()

# Using the Checkbutton widget to create a button and using place() method to set its position.
Checkbutton(root, text="English", variable=vars1).place(x=230, y=330)
Checkbutton(root, text="Neepali", variable=vars2).place(x=300, y=330)

# Using the Button widget, we get to create a button for submitting all the data that has been entered in the entry boxes of the form by the user.
submit_button = Button(root, text='Submit', width=20,
                       bg="black", fg='white', command=submit)
submit_button.place(x=180, y=380)

# Adding a label to display the result
result_label = Label(root, text="", font=("bold", 12))
result_label.place(x=180, y=420)

# Calling the mainloop method to execute the entire program.
root.mainloop()
