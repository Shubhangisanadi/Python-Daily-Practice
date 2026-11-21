'''
class student:
    def __init__(self):
        print("student informention")
s1 = student()

# 2. product
class Product:
    def __init__(self):
        self.name = "Laptop"
        self.price = 50000
    def desplay(self):
        print(self.name)
        print(self.price)
p1 = Product()
p1.desplay()

# 3. Non - parameterized constructor 
class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.color = "Black"

# 4.
class Company:
    def __init__(self):
        self.name = "Infosys"
        self.location = "Bangalore"

# Parameterized constructor 
class employee:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
#c1 = Car("BMW", 5000000)

# 2.
class ss:
    def __init__(self, id, "name"):
        self.id = 22
        self.name = "rahul"
    def display():
        print(self.id)
        print(self.name)
m1 = ss()'''

# oop
# 10.
class Student:
    def __init__(self, name="Alex"):
        self.name = name
s = Student()
print(s.name)   # ANS B)


'''       
# 13
class Book:
    def __init__(self, title):
        self.title = title
        return title
b = Book("Python 101")   # ANS B)


#  16.
class Dog:
    species = "Canis Familiaris"
    def __init__(self, name):
        self.name = name
d1 = Dog("Buddy")
d2 = Dog("Max")
Dog.species = "Wolf"
print(d1.species, d2.species)  # ANS B)

# 17.
class Counter:
    count = 0
c1 = Counter()
c2 = Counter()
c1.count = 10
print(Counter.count, c1.count, c2.count)   # ANS B)

# 20
class Team:
    members = []
t1 = Team()
t2 = Team()
t1.members.append("Sara")
print(t2.members)          # ANS B)

# 23.
class Greeter:
    def say_hi():
        print("Hi!")
g = Greeter()
g.say_hi()      # ANS B)

# 26.
class mathOps:
    @staticmethod
    def add(x, y):
        return x + y
print(mathOps.add(4, 5))   # ANS A)

# 28.
class Circle:
    pi = 3.14
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.pi * self.r * self.r
c = Circle(2)
print(c.area()) '''  # ANS B) 12.56 



        
        