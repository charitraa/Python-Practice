# The literal meaning of abstraction is to remove some characteristics from something to reduce it to a smaller set. Similarly, Object Oriented Programming abstraction exposes only the essential information of an object to the user and hides the other details.

# In real life, like when you toggle a switch, it simply turns on or off the lights. Here, we only know the functionality of the switch, but we don’t know its internal implementation, like how it works.

# How to implement abstraction?

# You can implement abstraction using classes that group the data members and function together. Inside classes, you can choose the access specifiers for its members to control how they are visible to the outside world. We can also create header files containing the implementations of all the necessary functions. So, you can include the header file and call these functions without getting into their implementation.

# Advantages of Abstraction

# The advantages of abstraction are as follows:

# It enables code reuse by avoiding code duplication.

# It enhances software security by making only necessary information available to the users and hiding the complex ones.
# Inheritance
# Inheritance is one of the most important features of object oriented programming. It allows a class to inherit the properties and methods of another class called the parent class, the base class, or the super-class.

# The class that inherits is called the child class or sub-class.

# It helps to avoid duplication of codes by allowing code reuse as you need not define the same methods and properties present in a super-class in the sub-classes again. The sub-class can simply inherit them.

# Example:

# You can have a parent class called “Shape” and other classes like Square, Circle, Rectangle, etc. Since all these are also shapes, they will have all the properties of a shape so that they can inherit the class Shape.

# Polymorphism
# The word polymorphism means to have many forms. So, by using polymorphism, you can add different meanings to a single component.


# There are two types of polymorphism:

# Run-time polymorphism

# Compile-time polymorphism

# Let's see each type in the next section.

# Method Overloading
# Methods overloading is a type of compile-time polymorphism using which you can define various functions with the same name but different numbers of arguments. The function call is resolved at compile time, so it's a type of compile-time polymorphism.  Here resolution of the function call implies binding to the correct function definition depending on the arguments passed in the function call.

# Example:

# You can create a function “add”. Now, when you pass two integers to this function, it will return their sum, while on passing two strings, it will return their concatenation.

# So, the same function acts differently depending on the input data type.

# Method Overriding
# Method Overriding is a type of run-time polymorphism. It allows overriding a parent class’s method by a child class. Overriding means that a child class provides a new implementation of the same method it inherits from the parent class.

# These function calls are resolved at run-time, so it's a type of runtime polymorphism.

# Example:

# You can have a parent class called “Shape” with a method named “findArea” that calculates and returns the area of the shape. Several sub-classes inherit from the “Shape,” like Square, Circle, Rectangle, etc. Each of them will define the function “findArea” in its way, thus overriding the function.

# Encapsulation
# Encapsulation means enclosing the data/variables and the methods for manipulating the data into a single entity called a class. It helps to hide the internal implementation of the functions and state of the variables, promoting abstraction.

# Example:

# You can have some private variables in a class that you can't access outside the class for security reasons. Now, to read or change the value of this variable, you can define public functions in the class which will perform the read or writes operations.
