a = "1"
b = "2"
print(int(a)+int(b))


a = 1
b = 2
print(str(a)+str(b))

# example of explicit typecasting

string = "15"
number = 7
# throw an error if the string is not a valid integer
string_number = int(string)
sum = number + string_number
print("Sum: ", sum, "\n")


# Implicit Typecasting
# implicitly converted to float because it contains decimal point.
string = '3'
