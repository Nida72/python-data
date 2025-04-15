#class and object

class Name:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print("Hello! my name is", self.name)

# Creating an object
n = Name("Nida")
n.say_hello()


#eg2
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start(self):
        print(f"{self.color} {self.brand} is starting...")
car = Car("HondA", "white")
car.start()

#Encapsulation:
"""def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  

        def deposit(self, amount):
         if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
         else:
            print("Invalid deposit amount!")

        def withdraw(self, amount):
         if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
         else:
            print("Insufficient balanc!")

        def get_balance(self):  
          return self.__balance
"""

# Create object
B_acc = ("Nida", 1000)
B_acc.deposit(2000)
print("Balance:", B_acc.get_balance())  
B_acc.withdraw(300)
print("Balance:", B_acc.get_balance())  


#Inheritance
class Animal:
    def eat(self):
        print("Animal eat food.")

class Dog(Animal):
    def eat(self):
        print("Dog eat meat.")

a = Animal()
d = Dog()

a.eat()  
d.eat()  

#polymorphism
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        print("area = π × r²")

class Square(Shape):
    def area(self):
        print("area = side × side")

shapes = [Circle(), Square()]
for s in shapes:
    s.area()

#Abstraction
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):    
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
def area(self):
        return self.length * self.width

# Create objects
c = Circle(7)
r = Rectangle(3,5)

print("Circle Area:", c.area())     
print("Rectangle Area:", r.area()) 


