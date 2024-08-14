# Concept:
# Modules and packages are essential in Python for organizing and reusing code. A module is a single file containing Python code, while a package is a collection of modules organized in directories. Using modules and packages helps in keeping code organized, modular, and maintainable.

# 1. Modules:

# A module is simply a Python file with a .py extension that contains Python code, such as functions, classes, or variables.
# You can import a module into your script using the import keyword.


# Example:

# Let's say you have a module named my_module.py with the following content:

# my_module.py
# import my_module
# import my_module as mm
# from my_module import greet


def greet(name):
    return f"Hello, {name}!"
# You can import and use this module in another Python file:


# message = my_module.greet("Babita")
# print(message)  # Output: Hello, Babita!
# Alternative Import Methods:

# Import specific functions or classes from a module:


# message = greet("Babita")
# print(message)
# Use an alias for a module:


# message = mm.greet("Babita")
# print(message)

# Standard Library Modules:

# Python comes with a rich standard library that provides a wide range of modules for various tasks.
# Some commonly used standard library modules:
# math: Provides mathematical functions.
# os: Provides functions for interacting with the operating system.
# sys: Provides access to some variables and functions that interact with the Python interpreter.
# random: Provides functions for generating random numbers.
# datetime: Provides classes for working with dates and times.
