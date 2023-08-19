letter = " Hey my name is {} and i am from {}"
country = "nepal"
name = "ravi"
print(letter.format(name, country))


print(f" Hey my name is {name} and i am from {country}")

txt = "For only {price:.2f}"
print(txt.format(price=49.00999999))

price = 49.0999999
print(f"for only {price:.2f}")
