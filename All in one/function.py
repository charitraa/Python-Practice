# How to Create a Function

import datetime


# How to Create a Function

def dateAndTime():
    "this function show the time and date "
    time = datetime.datetime.now().strftime('%H:%M:%S')
    date = datetime.date.today()

    print(time)
    print(date)


# how to call a function after creating it
dateAndTime()


# Docstring of a Function


# Argument

def Letter(Name, Class, rollNo):
    "this function is Basically show the result of student"
    print(f"{Name} is your name.\n{Name} has Scored 4GPA\n{Name} read in {Class} class\nyour Roll No is {rollNo}")


Letter('ravi', 12, 13)
