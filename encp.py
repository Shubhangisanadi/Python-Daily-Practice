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
account.set_balance(-500)


        
        