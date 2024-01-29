def average(a=9, b=1):
    print("The average is ", (a+b)/2)


average(1, 5)
average(a=3)


def name(fname, mname="ravi", lname="shrestha"):
    print("hello,", fname, mname, lname)


name("ravi", "bahadur", "shrestha")


def ave(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i

    print(sum / len(numbers))


ave(5, 10, 15)


def name1(**name):
    print("Hello", name["fname"], name["mname"], name["lname"])


name(mname="ravi", lname="bahadur", fname="shrestha")
