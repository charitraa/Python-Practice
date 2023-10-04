# # def hello(a):
# #     print("hello world " + a)


# # name = "rabi"
# # hello(name)

# def hello(a, b, c):
#     an = a + b + c
#     return an % 2 == 0


# print(hello(5, 6, 7))
# print(hello(5, 4, 4))

# # ,/'.


# def multiple(x):

#     if ((x % 2) == 0):
#         print("true")
#     else:
#         print("false")


# multiple(5)

# Create a Python function called `calculate_grade` that takes a student's score as input and returns their
# grade. Use the following grading scale: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59). Use an `if-
# else` statement inside the function to determine the grade.
def grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'


# Example usage:
student_score = 85
gradee = grade(student_score)
print(f"The grade for a score of {student_score} is: {gradee}")

# Write a Python function called `is_even_or_odd` that takes an integer as input and prints whether the
# number is even or odd. Use an `if-else` statement inside the function to check and print the result.


def is_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# Example usage:
input_number = 7
is_even_or_odd(input_number)
