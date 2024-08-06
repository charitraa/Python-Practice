# Concept:
# Lambda functions in Python are small anonymous functions defined with the lambda keyword. Unlike regular functions defined using def, lambda functions can have any number of arguments but only a single expression. They are often used for short, throwaway functions and are handy in situations where you need a simple function for a short period of time.


# Examples:
# Basic Lambda Function:

# A simple lambda function that adds 10 to the input.

def add_ten(x): return x + 10


print(add_ten(5))  # Output: 15

# Lambda Function with Multiple Arguments:

# A lambda function that multiplies two inputs.


def multiply(x, y): return x * y


print(multiply(3, 4))  # Output: 12

# Using Lambda with map():

# The map() function applies a given function to all items in an input list.


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Using Lambda with filter():

# The filter() function creates a list of elements for which a function returns true.


numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Using Lambda with sorted():

# The sorted() function can take a key argument that specifies a function to be called on each list element before making comparisons.


words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['apple', 'cherry', 'banana']
