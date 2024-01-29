# No.2
import math
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
sum = a + b
print("The sum of two number : ", sum)

# No.3
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

average = (a + b + c) / 3
print("The average of three number : ", average)

# No.4

a = input("Enter the string: ")
if a == "":
    print("The string has null value")

else:
    print("The string has value")


# No.5

a = int(input("Enter the degree temperature to convert fahrenheit: "))
b = (a*(9/5)+32)
print(" The temperature in fahrenheit is: ", b)

# No.6

a = int(input("enter the base of triangle :"))
b = int(input("Enter the height of the triangle:"))

c = 0.5 * a * b
print("The area of the triangle: ", c)

# No.7
a = int(input("enter the minutes to convert to hrs: "))
b = a / 60
print("The hours is ", b)

# No. 8
a = float(input("enter a number:"))
if a > 0:
    print(f"the given number {a} is positive")
elif a < 0:
    print(f"the given number {a} is negative")
else:
    print(f"the given number {a} is zero")

 # No. 9
a = float(input("enter your weight"))
b = float(input("enter your height"))

bmi = a/(b**2)
if bmi < 18.5:
    print(f"the described weight is underweight")
elif bmi > 18.5 and bmi < 24.9:
    print(f"the described weight is healthy range")
elif bmi > 25 and bmi < 29.9:
    print(f"the described weight is over-weight")

elif bmi > 30 and bmi < 39.9:
    print(f"the described weight is obesity")
elif bmi > 40:
    print(f"the descirbed weght is severe obesity")

# No. 10
a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
if a > b and a > c:
    print(f"{a} is greater number among three numbers")
elif b > c and b > a:
    print(f"{b} is greater number among three numbers")
elif c > a and c > b:
    print(f"{c} is greater number among three numbers")

# No. 11
radius = float(input("enter radius"))
area = math.pi*(radius**2)
print(f"the area of circle is {area}")
