#1. Write a Python `for` loop that prints the numbers from 1 to 5.
# for num in range(1,6):
#  print(num)

# #2.Create a Python `for` loop that calculates the sum of all numbers from 1 to 10.
# total_sum = 0
# for num in range(1, 11):
#     total_sum += num
# print( total_sum)

# #3. Write a Python `for` loop to iterate over a list of fruits and print each fruit's name.
# fruits=["apple","banana","mango","cherry"]
# sorted_fruits=sorted(fruits)
# print(sorted_fruits)

# #4. Create a Python `for` loop that counts the number of vowels (a, e, i, o, u) in a given string. (Also
# #use upper()or lower())

# input_string = "Happy,Dashain!"
# vowel_count = 0
# lowercase_string = input_string.lower()
# for char in lowercase_string:
#     if char in "aeiou":
#         vowel_count += 1
# print( vowel_count)

# #5. Write a Python `for` loop to find and print all even numbers between 1 and 20.
# for num in range(1,21):
#    if num%2==0:
#       print(num)

# #7. Create a Python `for` loop that prints the squares of numbers from 1 to 5.
# for num in range(1,6):
#    square= num**2
#    print(f"the square number of {num} is {square}")

# #8. Write a Python `for` loop to find and print the factorial of a given number `n`.
# num=int(input("enter any number:"))
# factorial = 1
# if num < 0:
#     print("Factorial is undefined for negative numbers.")
# else:
#     for i in range(1, num + 1):
#      factorial *= i
# print(f"The factorial of {num} is: {factorial}")

# #9. Create a Python `for` loop to iterate over a list of names and print a greeting for each name.
# names = ["Avrila", "Bitisha", "Dilasha", "Priti","Prajina"]
# for name in names:
#      print(f"Hello, {name}!")



#10. Write a Python `for` loop to calculate and print the Fibonacci series up to a given number of
#terms.
# num=int(input("enter any term"))
# a, b = 0, 1
# if num <= 0:
#     print("Please enter a positive integer for the number of terms.")
# elif num == 1:
#         print("Fibonacci series up to 1 term:", a)
# else:
#      print("Fibonacci series up to", num, "terms:")
#      print(a, b, end=" ")

# for _ in range(2, num):
#     c = a + b
#     print(c, end=" ")
#     a, b = b, c

#11. Create a Python `for` loop to find and print the largest number in a list of integers.
numbers = [10, 5, 8, 20, 15]
if not numbers:
        print("The list is empty.")
else:
    largest_number = numbers[0]
for num in numbers:
     if num > largest_number:
      largest_number = num
      print("The largest number in the list is:", largest_number)
