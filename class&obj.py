# class
# 1.
'''
class Student:
    name = "Shubhangi"
    age = 21
print(Student.name)
print(Student.age)

# 2.
class Employee:
    salary = 25000
print(Employee.salary)

# 3.
class Car:
    color = "Red"
print(Car.color)

# 4.
class Bike:
    brand = "Honda"
print(Bike.brand)

# 5.
class Laptop:
    price = 50000
print(Laptop.price)

# 6.
class Mobile:
    model = "Samsung"
print(Mobile.model)

# 7.
class College:
    name = "GFGC"
print(College.name)

# 8.
class Teacher:
    subject = "Python"
print(Teacher.subject)

# 9.
class Book:
    title = "Python Basics"
print(Book.title)

# 10.
class Animal:
    sound = "Bark"
print(Animal.sound)

# 11.
class Fruit:
    name = "Apple"
print(Fruit.name)

# 12.
class Bank:
    branch = "Belagavi"
print(Bank.branch)

# 13.
class Hospital:
    Name = "City Hospital"
print(Hospital.Name)

# 14.
class Product:
    price = 1000
print(Product.price)

# 15.
class Course:
    duration = "6 Months"
print(Course.duration)

# 16.
class Hotel:
    rooms = 20
print(Hotel.rooms)

# 17.
class Movie:
    city = "3 Idiots"
print(Movie.city)

# 18.
class Person:
    city = "Pune"
print(Person.city)

# 19.
class Developer:
    skill = "Python"
print(Developer.skill)

# 20.
class Food:
    name = "Dosa"
print(Food.name)


# 21.
class Student:
    name = "Rahul"
s1 = Student()
print(s1.name)

# 22.
class Student:
    Name = "Omkar"
    age = 20
s1 = Student()
print(s1.Name)
print(s1.age)

# 23.
class Employee:
    name = "Rahul"
    salary = 25000
e1 = Employee()
print(e1.name)
print(e1.salary)

# 24.
class Car:
    brand = "Toyota"
    color = "Black"
c1 = Car()
print(c1.brand)
print(c1.color)

# 25.
class Bike:
    name = "Honda"
    price = 80000
b1 = Bike()
print(b1.name)
print(b1.price)

# 26.
class Laptop:
    brand = "Dell"
    price = 50000
l1 = Laptop()
print(l1.brand)
print(l1.price)

# Practise Questions :
# 1 Student Management System
class Student:
    def __init__(self, name, Rollnumber, course,):
        self.name = name
        self.Rollnumber = Rollnumber
        self.Course = course
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.Rollnumber)
        print("Course:", self.Course)
s1 = Student("Shubhangi", 101, "Python Full Stack")
s1.display_details()

# 2. Employee salary details
class Employee:
    def __init__(self, emp_name, emp_ID, salary):
        self.emp_name = emp_name
        self.emp_ID = emp_ID
        self.salary = salary
    def calculate_salary(self):
        salary = self.salary * 12
        print("Employee Name:", self.emp_name)
        print("Employee ID:", self.emp_ID)
        print("salary:", self.salary)
e1 = Employee("Rahul", 101, 25000)
e1.calculate_salary()'''

# 3. Mobile class with brand, model and price.
class Mobile:
    def __init__(self, brand, mode, price):
        self.brand = brand
        self.mode = mode
        self.price = price
    def display_details(self):
        print("brand:", self.brand)
        print("mode:", self.mode)
        print("price:", self.price)
m1 = Mobile("vivo", "ss", 50000)
m1.desplay_details()

        

    

        


        
      
  

