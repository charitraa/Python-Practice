x = 4
# global variable
print(x)


def hello():
    global y  # make global
    y = 5
    x = 5
    # local variable
    print("hello world")


hello()
print(y)
