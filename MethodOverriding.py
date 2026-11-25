# Method Overriding
# 1. Employee
class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

obj = Developer()
obj.work()

# Notification
class Notification:
    def send(self):
        print("sending notification")

class Email(Notification):
    def send(self):
        print("sending email")

obj = Email()
obj.send()

# 3. Calculator
class Calculator:
    def calculate(self):
        print("Basic calculation")

class AdvancedCalculator(Calculator):
    def calculate(self):
        print("advanced calculation")

obj = AdvancedCalculator()
obj.calculate()

# 4. API 
class API:
    def request(self):
        print("sending request")

class UserAPI(API):
    def request(self):
        print("sending user request")

obj = UserAPI()
obj.request()

# 5. Security
class Security:
    def check(self):
        print("Security checking")

class Firewall(Security):
    def check(self):
        print("Firewall checking")

obj = Firewall()
obj.check()

# 6. Loggin
class Logger:
    def log(self):
        print("normal logging")

class ErrorLogger(Logger):
    def log(self):
        print("Error logging")

obj = ErrorLogger()
obj.log()

# 7. Search
class Search:
    def find(self):
        print("searching data")

class DatabaseSearch(Search):
    def find(self):
        print("searching database")

obj = DatabaseSearch()
obj.find()

# 8. Backup
class Backup:
    def save(self):
        print("saving backup")

class AutoBackup(Backup):
    def save(self):
        print("saving automatic backup")

obj = AutoBackup()
obj.save()

# 9. Cloud Storage
class Storage:
    def upload(self):
        print("uploading file")

class CloudStorage(Storage):
    def upload(self):
        print("uploading file to cloud")

obj = CloudStorage()
obj.upload()

# 10. Student
class Student:
    def study(self):
        print("student is studying")

class CollegeStudent(Student):
    def study(self):
        print("college student is studying python")

obj = CollegeStudent()
obj.study()

# Method Overloading
# 1. Addition
class Calculator:
    def add(self, a, b=0):
        print(a + b)

obj = Calculator()
obj.add(10)
obj.add(10, 20)

# Multiplication
class Calculator:
    def multiply(self, a, b=1):
        print(a * b)

obj = Calculator()
obj.multiply(5)
obj.multiply(5, 4)

# 3. Greeting
class Message:
    def greet(self, name="user"):
        print("Hello", name)

obj = Message()
obj.greet()
obj.greet("Rahul")

# 4. Area
class Shape:
    def area(self, length, width=0):
        if width == 0:
            print(length * length)
        else:
            print(length * width)

obj = Shape()
obj.area(5)
obj.area(5, 4)

# 5. student details
class Student:
    def details(self, name, age=None):
        print(name, age)

obj = Student()
obj.details("Rahul")
obj.details("Rahul", 22)

# Subtraction
class Calculator:
    def subtract(self, a, b=0):
        print(a - b)

obj = Calculator()
obj.subtract(20)
obj.subtract(20, 5)

# 7. display
class Display:
    def show(self, *values):
        for value in values:
            print(value)

obj = Display()
obj.show(10)
obj.show(10,20)
obj.show(10, 20, 30)

# 8. employee information
class Employee:
    def info(self, name, salary=None):
        print(name, salary)

obj = Employee()
obj.info("Amit")
obj.info("Amit", 25000)

# 9. Division
class Calculator:
    def divide(self, a, b=1):
        print(a / b)

obj = Calculator()
obj.divide(10)
obj.divide(10, 2)

# 10. power
class Calculator:
    def power(self, a, b=2):
        print(a ** b)

obj = Calculator()
obj.power(5)
obj.power(5, 3)



