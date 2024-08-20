# Concept:
# Today, we’ll dive deeper into Object-Oriented Programming(OOP) concepts, focusing on inheritance, polymorphism, and abstraction. These concepts help in creating more sophisticated and flexible code structures.

# 1. Inheritance:

# Inheritance allows one class (the child class) to inherit attributes and methods from another class (the parent class). This promotes code reuse and establishes a relationship between the classes.


from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        return f"{self.make} {self.model} is starting."


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def lock_doors(self):
        return f"All {self.doors} doors are locked."


my_car = Car("Toyota", "Camry", 4)
print(my_car.start())  # Output: Toyota Camry is starting.
print(my_car.lock_doors())  # Output: All 4 doors are locked.


# 2. Polymorphism:

# Polymorphism allows different classes to be treated as instances of the same class through inheritance. It also enables methods to be overridden, meaning a method in a child class can have the same name as a method in the parent class but behave differently.


class Animal:
    def make_sound(self):
        return "Some generic sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())  # Output: Woof, Meow


# 3. Abstraction:

# Abstraction hides the complex implementation details and shows only the necessary features of an object. In Python, abstraction is achieved using abstract classes and methods, which are defined using the abc module.
# Example:


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius


my_circle = Circle(5)
print(my_circle.area())  # Output: 78.53975
print(my_circle.perimeter())  # Output: 31.4159
