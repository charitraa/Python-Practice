def greet(fx):
    def mfx(*a, **b):
        print("Hello")
        fx(*a, **b)
        print("thanks")
    return mfx


@greet
def hello():
    print("hello world")


@greet
def add(a, b):
    print(a+b)


hello()
add(1, 2)
