# Day 9: Iterators and Generators
# Concept:
# Today, we'll explore iterators and generators in Python, which are powerful tools for handling sequences of data.

# 1. Iterators:

# An iterator is an object that contains a countable number of values and can be iterated upon, meaning you can traverse through all the values.
# In Python, an iterator must implement two methods: __iter__() and __next__().
# Example:


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  # Output: 1
print(next(myiter))  # Output: 2

# 2. Generators:

# Generators are a simple way of creating iterators using a function that yields a value one at a time.
# The yield keyword is used instead of return to produce a value and pause the function's execution.
# Example:


def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)  # Output: 1 2 3

# 3. Differences Between Iterators and Generators:

# Memory Efficiency: Generators are more memory efficient as they yield items one at a time, rather than creating and storing the entire sequence in memory.
# Simplicity: Generators are simpler to implement and use compared to custom iterator classes.
# 4. Generator Expressions:

# Like list comprehensions, generator expressions provide a compact syntax for creating generators.
# The main difference is that generator expressions use parentheses () instead of square brackets [].
# Example:

my_gen = (x * x for x in range(5))
for value in my_gen:
    print(value)  # Output: 0 1 4 9 16
# 5. Use Cases for Generators:

# Generators are useful when working with large datasets or streams of data where you don’t need to store all the data at once.
# They are often used in tasks like reading large files, processing data in chunks, or producing infinite sequences.
