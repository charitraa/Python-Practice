a = "charitra1111 111111111111111 charitra"
print(len(a))

print(a.upper())
print(a.lower())
print(a.rstrip("1"))
print(a.replace("charitra", "Ravi"))
print(a.split(" "))

b = "introduction"
print(b.capitalize())

str1 = " welcome to the Console"
print(len(str1))
print(str1.center(50))
print(a.count("charitra"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))


print(str1.endswith("to", 4, 10))
str1 = "he is a good boy"
print(str1.find("is"))
str1 = "Hello"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str2 = "welcome"
print(str2.islower())

str3 = "WELCOME TO THE CONSOLE"
print(str3.isprintable())

str3 = "                        "
print(str3.isspace())

str1 = "Hello World"
print(str1.istitle())

str1 = "his name is Dan"
print(str1.title())
