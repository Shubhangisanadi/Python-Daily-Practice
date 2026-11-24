'''
class student():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name 

s1 = student("Shubhangi")
print("old name:", s1.get_name())
s1.set_name("Shreya")
print("new name:", s1.get_name())



# 2. getter and setter with validation
class BankAccount():
    def __init__(self):
        self.__balance = 5000

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")

account = BankAccount()
print(account.get_balance())
account.set_balance(8000)
print(account.get_balance())
account.set_balance(-500)      '''

# 1. Single Inheritance
class Database:
    def connect(self):
        print("Database connected")

class mySql(Database):
    def execute_query(self):
        print("Executing SQL query")

obj = mySql()
obj.connect()
obj.execute_query()

# 2. Authentication
class Authentication:
    def login(self):
        print("User login successful")

class admin(Authentication):
    def dashboard(self):
        print("admin dashboard opened")

a = admin()
a.login()
a.dashboard()

# 3. File handling
class File:
    def open_file(self):
        print("File opened")

class TextFile(File):
    def read_file(self):
        print("Reading text file")
f = TextFile()
f.open_file()
f.read_file

# 4. API Development
class API:
    def request(self):
        print("API request sent")

class UserAPI(API):
    def get_users(self):
        print("Fetching users")

u = UserAPI()
u.request()
u.get_users()

# 5. Data Processing
class Data:
    def load_data(self):
        print("Data loaded")

class DataAnalysis(Data):
    def analyze(self):
        print("Data analysis completed")

d = DataAnalysis()
d.load_data()
d.analyze()

# Multiple Inheritance
# 1. web application
class Frontend:
    def html(self):
        print("HTML page created")

class Backend:
    def python(self):
        print("Python backend running")

class WebApp(Frontend, Backend):
    def run(self):
        print("Web application running")

w = WebApp()
w.html()
w.python()
w.run

# 2. Database & Authentication
class Database:
    def connect(self):
        print("Database connected")

class Security:
    def encrypt(self):
        print("Data encrypt")

class Application(Database, Security):
    def start(self):
        print("Application started")

a = Application()
a.connect()
a.encrypt()
a.start()

# 3. E - commerce 
class Payment:
    def pay(self):
        print("Payment successful")

class Delivery:
    def ship(self):
        print("Product shipped")

class Order(Payment, Delivery):
    def confirm(self):
        print("Oredr confirmed")

o = Order()
o.pay()
o.ship()
o.confirm()

# 4. Data Analysis
class Excel:
    def read_excel(self):
        print("Excel data loaded")

class SQL:
    def fecth_data(self):
        print("SQL data fecthed")

class Report(Excel, SQL):
        def generate(self):
            print("Report generated")

r = Report()
r.read_excel()
r.fecth_data()
r.generate()

# 5. Cloud Application
class Storage:
    def upload(self):
        print("File uploaded")

class Logging:
    def log_data(self):
        print("Log recorded")

class CloudApp(Storage, Logging):
    def deploy(self):
        print("Application deployed")

c = CloudApp()
c.upload()
c.log_data()
c.deploy()

# Multilevel Inheritance
# 1. Software Development
class Programming:
    def language(self):
        print("Python programming")

class Backend(Programming):
    def framework(self):
        print("Django framework")

class FullStack(Backend):
    def frontend(self):
        print("HTML and CSS")

f = FullStack()
f.language()
f.framework()
f.frontend()

# 2. Database System
class Database:
    def create_database(self):
        print("Database created")

class MySQL(Database):
    def create_table(self):
        print("Table created")

class DatabaseAdmin(MySQL):
    def manage_users(self):
        print("Users managed")

d = DatabaseAdmin()
d.create_database()
d.create_table()
d.manage_users()

# 3. Employee Management
class Employee:
    def employee_id(self):
        print("Employee ID: 101")

class Developer(Employee):
    def skill(self):
        print("Python Developer")

class SeniorDeveloper(Developer):
    def project(self):
        print("Project completed")

s = SeniorDeveloper()
s.employee_id()
s.skill()
s.project()

# 4. Machine Learning
class Dataset:
    def load(self):
        print("Dataset loaded")

class Training(Dataset):
    def train(self):
        print("Model training started")

class Prediction(Training):
    def predict(self):
        print("Prediction generated")

p = Prediction()
p.load()
p.train()
p.predict()

# 5. API Framework
class Request:
    def send(self):
        print("Request sent")

class Response(Request):
    def receive(self):
        print("Response received")

class APIClint(Response):
    def display(self):
        print("API data displayed")

a = APIClint()
a.send()
a.receive()
a.display()

# Hierarchical Inheritance
# 1. User Management
class User:
    def login(self):
        print("User logged in")

class Admin(User):
    def manage(self):
        print("Admin managing users")

class Customer(User):
    def purchase(self):
        print("Customer purchesed product")

a = Admin()
c = Customer()

a.login()
a.manage()

c.login()
c.purchase()

# 2. Database Operations
class Database:
    def connect(self):
        print("Database connected")

class MySQL(Database):
    def query(self):
        print("MySQL query executed")

class MongoDB(Database):
    def document(self):
        print("MongoDB document fetched")

m = MySQL()
n = MongoDB()

m.connect()
m.query()

n.connect()
n.document()

# 3. Payment System
class Payment:
    def validate(self):
        print("Payment validated")

class UPI(Payment):
    def upi_pay(self):
        print("UPI Payment")

class Card(Payment):
    def card_pay(self):
        print("Card payment")

u = UPI()
c = Card()

u.validate()
u.upi_pay()

c.validate()
c.card_pay()

# 4. File Processing
class FileProcessor:
    def open_file(self):
        print("File opened")

class CSVProcessor(FileProcessor):
    def read_csv(self):
        print("CSV data read")

class JSONProcessor(FileProcessor):
    def read_json(self):
        print("JSON data read")

c = CSVProcessor()
j = JSONProcessor()

c.open_file()
c.read_csv()

j.open_file()
j.read_json()

# 5. Notification System
class Notification:
    def send(self):
        print("Notification sent")

class Email(Notification):
    def send_email(self):
        print("Email notification")

class SMS(Notification):
    def send_sms(self):
        print("SMS notification")

e = Email()
s = SMS()

e.send()
e.send_email()

s.send()
s.send_sms()

# Hybrid Inheritance
# 1. Web Application
class Database:
    def connect(self):
        print("Database connected")

class Authentication(Database):
    def login(self):
        print("User authenticated")

class Logging:
    def record(self):
        print("Activity recorded")

class Application(Authentication, Logging):
    def run(self):
        print("Application running")

a = Application()
a.connect()
a.login()
a.record()
a.run()

# 2. E-Commerce system
class Product:
    def details(self):
        print("Product details")

class Inventory(Product):
    def stock(self):
        print("Stock available")

class Payment:
    def pay(self):
        print("Payment completed")

class Order(Inventory, Payment):
    def confirm(self):
        print("Oredr confirmed")

o = Order()
o.details()
o.stock()
o.pay()
o.confirm()

# 3. Employee system
class Employee:
    def details(self):
        print("Employee details")

class Developer(Employee):
    def coding(self):
        print("Coding in python")

class Tester(Employee):
    def testing(self):
        print("Software testing")

class TeamLead(Developer, Tester):
    def manage(self):
        print("Team managed")

t = TeamLead()
t.details()
t.coding()
t.testing()
t.manage()

# 4. Data Analutics
class DataSource:
    def load(self):
        print("Data loaded")

class ExcelData(DataSource):
    def excel(self):
        print("Excel processed")

class Analytics(ExcelData, DataSource):
    def report(self):
        print("Report generated")

a = Analytics()
a.load()
a.excel()
a.sql()
a.report()

# 5. Software Deployment
class Software:
    def develop(self):
        print("Software Developed")

class Backend(Software):
    def server(self):
        print("Backend server ready")

class Frontend:
    def interface(self):
        print("Frontend interface ready")

class Deployment(Backend, Frontend):
    def deploy(self):
        print("Software deployed")

d = Deployment()
d.develop()
d.server()
d.interface()
d.deploy()        


        
        