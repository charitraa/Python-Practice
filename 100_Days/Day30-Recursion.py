def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))

# to call the function inside the function is call recursion function

# Program to display the Fibonacci sequence up to n-th term

term = int(input("How many terms ?\n\n "))

# first two terms
n1, n2 = 0, 1
i = 0

# check if the number of terms is valid
if term <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif term == 1:
    print("Fibonacci sequence upto", term, ":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while i < term:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1
