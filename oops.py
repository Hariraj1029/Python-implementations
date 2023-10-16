# Object-Oriented Programming (OOP) Concepts

# Class Definition
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Encapsulation: Accessor Method (Getter)
    def get_name(self):
        return self.name

    # Encapsulation: Mutator Method (Setter)
    def set_name(self, new_name):
        self.name = new_name

    # Inheritance: Parent Class Method
    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.species}"

# Inheritance: Child Class (Subclass)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Inheritance: Child Class (Subclass)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Polymorphism: Function That Accepts Objects of Different Types
def animal_sound(animal):
    return animal.make_sound()

# Polymorphism: Function That Accepts Objects of Different Types
def animal_description(animal):
    return str(animal)

# Abstraction: Creating Objects (Instances of Classes)
fido = Dog("Fido", "Dog")
whiskers = Cat("Whiskers", "Cat")

# Inheritance: Calling Parent Class Method from Child Class
print(fido.make_sound())  # Output: Woof!
print(whiskers.make_sound())  # Output: Meow!

# Polymorphism: Using Functions That Accept Objects of Different Types
print(animal_sound(fido))  # Output: Woof!
print(animal_sound(whiskers))  # Output: Meow!

# Encapsulation: Using Accessor and Mutator Methods
print(fido.get_name())  # Output: Fido
fido.set_name("Rover")
print(fido.get_name())  # Output: Rover

# Abstraction: Using Objects to Access Properties
print(animal_description(fido))  # Output: Rover is a Dog.
print(animal_description(whiskers))  # Output: Whiskers is a Cat.

# Advanced OOP Concepts

# Composition: Combining Objects
class Person:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return f"{self.name} has a pet {str(self.pet)}"

# Composition: Creating Objects with Composition
alice = Person("Alice", fido)
bob = Person("Bob", whiskers)

print(alice)
print(bob)

# Abstraction: Abstract Base Class
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass

# Abstraction: Subclass Implementing Abstract Method
class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies in the sky."

# Abstraction: Subclass Implementing Abstract Method
class Penguin(Bird):
    def fly(self):
        return "Penguin swims in the water."

sparrow = Sparrow("Sparrow")
penguin = Penguin("Penguin")

print(sparrow.fly())
print(penguin.fly())
