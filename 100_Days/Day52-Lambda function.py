
def double(x, value): return x(value)

# double = lambda x: x*2


def cube(x): return x*x*x
# cube = lambda x: x*x*x


print(double(lambda x: x*x*x, 5))
print(double(cube, 5))
