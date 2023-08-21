def cube(x):
    return x*x*x


print(cube(2))

# map
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# newl = list(map(cube, l))
newl = list(map(lambda x: x*x*x, l))
print(newl)


def filter_function(a):
    return a > 3


# filter
newl2 = list(filter(filter_function, l))

print(newl2)
