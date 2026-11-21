# local variable
def student():
    name = "Shubhangi"
    print(name)
student()

# 2.
def age():
    a = 22
    print(a)
age()

# 3.
def add():
    a = 10
    b = 20
    print(a + b)
add()

# 4.
def sub():
    a = 50
    b = 20
    print(a - b)
sub()

# 5.
def mul():
    a = 5
    b = 4
    print(a * b)
mul()

# 6.
def div():
    a = 20
    b = 5
    print(a / b)
div()

# 7.
def check():
    num = 10
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
check()

# 8.
def square():
    num = 5
    print(num ** 2)
square() 

# 9.
def length():
    name = "Python"
    print(len(name))
length()

# 10.
def fruits():
    mylist = ["apple", "banana", "kivi"]
    print(mylist)
fruits()

# Global varibale
# 1.
name = "Shubhangi"
def student():
    print(name)
student()

# 2.
age = 22
def show():
    print(age)
show()

# 3.
a = 10
b = 20
def add():
    print(a + b)
add()

# 4.
a = 50
b = 20
def sub():
    print(a - b)
sub()

# 5.
a = 5
b = 4
def multiply():
    print(a * b)
multiply()

# 6.
num = 8
def check():
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check()

# 7.
num = 6
def square():
    print(num ** 2)
square()

# 8.
name = "Python"
def length():
    print(len(name))
length()

# 9.
x = 10
def change():
    global x
    x = 50
change()
print(x)

# 10.
fruits = ["Apple", "Mango",]
def show():
    fruits.append("kivi")
    print(fruits)
show()

# Nested Functions
# 1.
def outer():
    print("Outer Function")

    def inner():
        print("Inner function")
    inner()
outer()

# 2.
def outer():
    a = 10
    b = 20
    def inner():
        print(a + b)
    inner()
outer()

# 3.
def outer():
    a = 50
    b = 20
    def inner():
        print(a - b)
    inner()
outer()

# 4.
def outer():
    a = 5
    b = 4
    def inner():
        print(a * b)
    inner()
outer()

# 5.
def outer():
    a = 20
    b = 5
    def inner():
        print(a / b)
    inner() 
outer()

# 6.
def outer():
    num = 10
    def inner():
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    inner()
outer()

# 7.
def outer():
    num = 5
    def inner():
        print(num ** 2)
    inner()
outer()

# 8.
def outer():
    name = "Python"
    def inner():
        print(len(name))
    inner()
outer()

# 9.
def outer():
    name = "Python"
    def inner():
        print(name[::-1])
    inner()
outer()

# 10.
def outer():
    num = 5
    def inner():
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
            print(fact)
    inner()
outer()
