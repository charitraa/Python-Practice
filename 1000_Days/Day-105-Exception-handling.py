# Concept:
# Exception handling in Python is a way to manage errors or exceptions that occur during the execution of a program. Instead of letting the program crash, you can use exception handling to gracefully manage the error and keep the program running.

# Basic Keywords:

# try:

# The code that might throw an exception is placed inside the try block.

# try:
#     # code that might raise an exception
# except:

# If an exception occurs in the try block, the except block is executed.

# except:
#     # code to handle the exception
# else:

# The else block is executed if no exception occurs in the try block.

# else:
#     # code to execute if no exception occurs
# finally:

# The finally block is executed no matter what, whether an exception occurs or not . It is often used for cleanup actions.

# finally:
# code that will run no matter what
# Basic Example:


try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid integer.")
else:
    print(f"The result is {y}.")
finally:
    print("This will run no matter what.")
