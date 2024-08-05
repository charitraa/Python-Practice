# Concept:
# List comprehensions provide a concise way to create lists. They are more compact and readable than traditional loops and offer a way to generate lists by performing operations on each item in an existing iterable or by filtering items.

# using for loops
squares = []
for i in range(10):
    squares.append(i ** 2)

# using list comprehension

squares = [i ** 2 for i in range(10)]

# output lists
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering with List Comprehensions:

# Suppose you want a list of only the even numbers from 0 to 9.

# Using a for loop:

evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)

# Using list comprehension:
evens = [i for i in range(10) if i % 2 == 0]


# Suppose you want to convert a list of strings to uppercase.

# Using a for loop:
# #

names = ['john', 'doe', 'jane']
upper_case_names = []
for name in names:
    upper_case_names.append(name.upper())


# Using list comprehension:
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]

# using nested for loops:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []
for row in matrix:
    for element in row:
        flattened.append(element)

# using list comprehension with nested loops:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
