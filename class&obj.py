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
        print("Mode:", self.mode)
        print("Price:", self.price)
    def apply_discount(self, discount):
        final_price = self.price - discount
        print("Final Price:", final_price)
m1 = Mobile("vivo", "M14", 15000)

m1.desplay_details()
m1.apply_discount(2000)

# Bank Account
class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposite(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdraw:", amount)
        else:
            print("Insufficient Balance")
    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
a1 = BankAccount("Amit", 10000)
a1.deposite(2000)
a1.withdraw(3000)
a1.display_balance()

# Car Rental System
class Car:
    def __init__(self, car_name, rent_per_day):
        self.car_name = car_name
        self.rent_per_day = rent_per_day
    def calculate_rent(self, days):
        total_rent = self.rent_per_day * days
        print("Car Name:", self.car_name)
        print("Rental Days:", days)
        print("Total Rent:", total_rent)
c1 = Car("Swift", 1500)
c1.calculate_rent(5)

# Laptop info no - argument constructor
class Laptop:
    def __init__(self):
        self.brand = "Dell"
        self.shubhangi = "16GB"
        self.price = 55000
    def display_details(self):
        print("Brand:", self.brand)
        print("SHUBHANGI:", self.shubhangi)
        print("price:", self.price)

l1 = Laptop()
l1.display_details()

# Book info parameterized constuctor
class Book:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price
    def display_details(self):
        print("Book:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)
b1 = Book("Python", "Jhon", 500)
b2 = Book("Java", "David", 600)

b1.display_details()
b2.display_details()

# Rectangle area
class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area:", area)


r1 = Rectangle(10, 5)
r1.calculate_area()


#Electricity bill
class ElectricityBill:
    def _init_(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5

        elif self.units <= 200:
            bill = (100 * 5) + (self.units - 100) * 7

        else:
            bill = (100 * 5) + (100 * 7) + (self.units - 200) * 10

        print("Customer:", self.name)
        print("Units:", self.units)
        print("Total Bill:", bill)


e1 = ElectricityBill("Amit", 250)
e1.calculate_bill()


# Product inventory
class Product:
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total_price(self):
        total = self.price * self.quantity
        print("Total Price:", total)

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Updated Quantity:", self.quantity)


p1 = Product("Laptop", 50000, 2)

p1.display_product()
p1.calculate_total_price()
p1.update_quantity(5)


# company employee counter
class Employee:
    company_name = "ABC Company"
    employee_count = 0

    def _init_(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

        Employee.employee_count += 1

    def display_details(self):
        print("Company:", Employee.company_name)
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Total Employees:", Employee.employee_count)


e1 = Employee("Amit", 101)
e2 = Employee("Priya", 102)
e3 = Employee("Rahul", 103)

e1.display_details()
e2.display_details()
e3.display_details()


# school student info
class Student:
    school_name = "ABC School"

    def _init_(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        percentage = 85

        print("School:", Student.school_name)
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Percentage:", percentage)


s1 = Student("Amit", 101)
s1.display_details()


#shopping cart
class ShoppingCart:
    discount_percentage = 10

    def _init_(self, customer, total_amount):
        self.customer = customer
        self.total_amount = total_amount

    def calculate_discount(self):
        discount = self.total_amount * ShoppingCart.discount_percentage / 100

        final_amount = self.total_amount - discount

        print("Customer:", self.customer)
        print("Original Amount:", self.total_amount)
        print("Discount:", discount)
        print("Final Amount:", final_amount)


c1 = ShoppingCart("Priya", 2000)
c1.calculate_discount()


# hospital patient management
class Patient:
    hospital_name = "City Hospital"

    def _init_(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def display_patient(self):
        print("Hospital:", Patient.hospital_name)
        print("Patient:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


p1 = Patient("Amit", 25, "Fever")
p2 = Patient("Priya", 30, "Cold")
p3 = Patient("Rahul", 28, "Cough")

p1.display_patient()
p2.display_patient()
p3.display_patient()


# online course management
class Course:
    institute_name = "Kiran Academy"

    def _init_(self, course_name, course_fee):
        self.course_name = course_name
        self.course_fee = course_fee

    def calculate_fee(self):
        discount = 500

        final_fee = self.course_fee - discount

        print("Institute:", Course.institute_name)
        print("Course:", self.course_name)
        print("Original Fee:", self.course_fee)
        print("Discount:", discount)
        print("Final Fee:", final_fee)


c1 = Course("Python Full Stack", 20000)
c1.calculate_fee()


# ATM withdrawal system
class ATM:
    def _init_(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient Balance")
            return self.balance


a1 = ATM("Amit", 10000)

a1.check_balance()

new_balance = a1.deposit(2000)
print("After Deposit:", new_balance)

new_balance = a1.withdraw(3000)
print("After Withdraw:", new_balance)


# temperature converter
class Temperature:
    def _init_(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius


t1 = Temperature(30)

print("Fahrenheit:", t1.celsius_to_fahrenheit())

print("Celsius:", t1.fahrenheit_to_celsius(98.6))


# student result management
class StudentResult:
    def _init_(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_total(self):
        return self.m1 + self.m2 + self.m3

    def calculate_percentage(self):
        total = self.calculate_total()
        percentage = total / 3
        return percentage

    def display_result(self):
        print("Name:", self.name)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())


s1 = StudentResult("Amit", 80, 90, 85)
s1.display_result()


# food ordering system
class FoodOrder:
    def _init_(self, customer, food, price, quantity):
        self.customer = customer
        self.food = food
        self.price = price
        self.quantity = quantity

    def calculate_bill(self):
        total = self.price * self.quantity
        return total

    def apply_coupon(self, discount):
        total = self.calculate_bill()
        final_bill = total - discount
        return final_bill

    def display_order(self):
        print("Customer:", self.customer)
        print("Food:", self.food)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.calculate_bill())
        print("Final Bill:", self.apply_coupon(50))


f1 = FoodOrder("Priya", "Pizza", 200, 2)
f1.display_order()


# vehicle management system
class Vehicle:
    vehicle_count = 0

    def _init_(self, name, vehicle_type, price):
        self.name = name
        self.vehicle_type = vehicle_type
        self.price = price

        Vehicle.vehicle_count += 1

    def display_details(self):
        print("Name:", self.name)
        print("Type:", self.vehicle_type)
        print("Price:", self.price)

    def calculate_insurance(self, rate):
        insurance = self.price * rate / 100
        return insurance

    def update_price(self, new_price):
        self.price = new_price
        print("Updated Price:", self.price)


v1 = Vehicle("Swift", "Car", 800000)
v2 = Vehicle("Honda", "Bike", 100000)

v1.display_details()

print("Insurance:", v1.calculate_insurance(5))

v1.update_price(850000)

print("Total Vehicles:", Vehicle.vehicle_count)
        

    

        


        
      
  

