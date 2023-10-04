# Question 1:
def calculate_grade():
    try:
        score = float(input("Enter the student's score: "))
        if 90 <= score <= 100:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        elif 60 <= score < 70:
            return "D"
        elif 0 <= score < 60:
            return "F"
        else:
            return "Invalid score"  # Handle scores outside the valid range
    except ValueError:
        return "Invalid input, please enter a numeric score."


# Example usage:
grade = calculate_grade()
print(f"Student's grade: {grade}")
# Question 2:


def is_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# Example usage:
user_input = int(input("Enter an integer: "))
is_even_or_odd(user_input)
# Question 3:


def find_maximum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
maximum = find_maximum(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is {maximum}")
# Question 4:


def is_vowel(character):
    # Convert the character to lowercase to handle both uppercase and lowercase input
    character = character.lower()
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
        return True
    else:
        return False


# Example usage:
user_input = input("Enter a character: ")
if len(user_input) == 1 and user_input.isalpha():
    result = is_vowel(user_input)
    if result:
        print(f"{user_input} is a vowel.")
    else:
        print(f"{user_input} is a consonant.")
else:
    print("Invalid input. Please enter a single character.")
# Question 5:


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Example usage:
user_input = int(input("Enter a year: "))
if is_leap_year(user_input):
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")
# Question 6:


def calculate_discount(original_price, discount_percentage):
    if discount_percentage > 50:
        discount_percentage = 50  # Apply a maximum discount of 50%

        discount_amount = (discount_percentage / 100) * original_price
        discounted_price = original_price - discount_amount
        return discounted_price


# Example usage:
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
discounted_price = calculate_discount(original_price, discount_percentage)
print(f"The discounted price is: ${discounted_price:.2f}")
# Question 7:


def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category


# Example usage:
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
bmi, category = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f}, which is categorized as {category}.")
