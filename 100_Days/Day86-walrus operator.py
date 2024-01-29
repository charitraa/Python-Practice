a = True
print(a := False)

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())


# happy = False
# print(happy)

# print(happy := True)

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":  # using walrus
    foods.append(food)
