# Concept:
# Object-Oriented Programming(OOP) is a programming paradigm that uses objects and classes to structure code in a more modular and reusable way. OOP allows you to model real-world entities as objects, each with its own properties(attributes) and behaviors(methods).

# Key Concepts:

# Class:

# A class is a blueprint for creating objects. It defines the properties(attributes) and behaviors(methods) that the objects created from the class will have.
# Example:


class Dog:  # type: ignore
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"


# Object:

# An object is an instance of a class . It is created from a class and can use the attributes and methods defined in the class .
# Example:


my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
print(my_dog.bark())  # Output: Buddy says Woof!
# Attributes:

# Attributes are the properties of an object. They are variables that belong to an object.
# Example:


class Car:  # type: ignore
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# Methods:

# Methods are functions that belong to an object. They define the behaviors of the object.
# Example:


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.make} {self.model} is starting."


# __init__ Method:

# The __init__ method is a special method in Python classes. It is called automatically when a new object is created and is used to initialize the object's attributes.
# Example:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Inheritance:

# Inheritance allows one class to inherit attributes and methods from another class, promoting code reuse.
# Example:


class Animal:  # type: ignore
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound."


class Dog(Animal):  # type: ignore
    def bark(self):
        return f"{self.name} says Woof!"


# Encapsulation:

# Encapsulation is the practice of keeping data(attributes) private and only exposing methods to interact with the data.
# Example:


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# Polymorphism:

# Polymorphism allows different classes to be treated as instances of the same class through inheritance. It also allows methods to have the same name but behave differently based on the object.
# Example:


class Animal:
    def make_sound(self):
        return "Some sound"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


animals = [Cat(), Dog()]
for animal in animals:
    print(animal.make_sound())  # Output: Meow, Woof
