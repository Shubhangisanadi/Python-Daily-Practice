'''
def function_name():
    # code
    statement

    function_name    # syntax

# 2.
def greet():
    print("hello Shubhangi")
greet()                           # simple fun

#3.
def greet(name):
    print("hello", name)
greet("Shubhangi")               # fun with parameters

# 4.
def add(a, b):
    print(a + b)
add(10, 20)

# 5.
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# 6.
def stud(name, age):
    print(name, age)
stud("Shubhangi", 21)

# 7.
def stud(name, age):
    #print(name, age)
    stud(age=22, name="Shubhangi")

# 8.
def add(*numbers):
    print(sum(numbers))
add(10, 20, 30, 40)

# 9.
def stud(**details):
    print(details)
stud(name="Shubhangi", age=22, city="pune")

# 1.
def find_length(name):
    print(len(name))
find_length("python")

# 2.
def find_max(numbers):
    print(max(numbers))
find_max([10, 20, 50, 30])

# 3.
def finf_min(numbers):
    print(min(numbers))
finf_min([10, 20, 5, 30])

# 4.
def find_sum(numbers):
    print(sum(numbers))
find_sum([10, 20, 30])

# 5.
def add(a, b):
    print(a+b)
add(10, 20)

# 6.
def sub(a, b):
    print(a-b)
sub(5, 2)

# 7. 
def mul(a, b):
    print(a * b)
mul(7, 2)

# 8.
def div(a, b):
    print(a / b)
div(20, 5)

# 9.
def check_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even(10)

# 10.
def calculate(numbers):
    print("Length:", len(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))
calculate([10, 20, 30, 40, 50])'''




# Without Argument-Without Return

# 1.
def greet():
    print("Hello Python")
greet()    

# 2. Addition
def add():
    print(10 + 20)
add()

# 3. Even Odd
def even_odd():
    num = 10
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
print_odd()

# 4. Square 
def square():
    print(5 * 5)
square()

# 5. multiplication
def multiply():
    print(5 * 4)
multiply()

# 6. Welcome
def welcome():
    print("welcome to python")
welcome()

# 7. Table
def table():
    for i in range(1, 6):
        print(2 * i)
table()

# 8.Reverse string
def reverse():
    print("Python"[::-1])
reverse()

# 9. Maximum
def maximum():
    print(max(10, 20, 30))
maximum()

# 10. List
def show_list():
    print([10, 20, 30])
show_list()

# Without Argument-with Return

# 1. 
def add():
    return 10 + 20
result = add()
print(result)

# 2. square
def square():
    return 5 * 5
print(square())

# 3. Subtraction
def subtract():
    return 50 - 20
print(subtract())

# 4. multiplication
def multiply():
    return 5 * 4
print(multiply())

# 5. division
def division():
    return 20 / 5
print(divide())

# 6. even odd
def even_odd():
    num = 8
    return num % 2 == 0
print(even_odd())

# 7. string
def name():
    return "Shubhangi"
print(name())

# 8. list
def numbers():
    return [10, 20, 30]
print(numbers())

# 9. maximum
def maximum():
    return max(10, 20, 30)
print(maximum())

# 10. reverse
def reverse():
    return "python"[::-1]
print(reverse())

# with argument-without return
# 1.
def greet(name):
    print("Hello", name)
greet("Amit")

# 2. addition
def add(a, b):
    print(a + b)
add(10, 20)

# 3. even odd
def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
even_odd(8)

# 4. square
def square(num):
    print(num * num)
square(5)

# 5. multiplication
def multiply(a, b):
    print(a * b)
multiply(4, 5)

# 6. subtraction
def subtract(a, b):
    print(a - b)
subtract(50, 20)

# 7. reverse string
def reverse(name):
    print(name[::-1])
reverse("python")

# 8. table
def table(num):
    for i in range(1, 11):
        print(num * i)
table(2)

# 9. maximum
def maximum(a, b):
    print(max(a, b))
maximum(10, 20)

# 10. palindrome string
def palindrome(word):
    if word == word[::-1]:
        print("palindrome")
    else:
        print("Not palindrome")
palindrome("madam")

# with argument-with return

# 1.
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# 2. even odd
def even_odd(num):
    if num % 2 == 0:
        return "even"
    return "odd"
print(even_odd(8))

# 3. square
def square(num):
    return num * num
print(square(5))

# 4. subtraction
def subtract(a, b):
    return a - b
print(subtract(50, 20))

# 5. multiplication
def multiply(a, b):
    return a * b
print(multiply(4, 5))

# 6. division
def divide(a, b):
    return a / b
print(divide(20, 5))

# 7. reverse string
def reverse(word):
    return word[::-1]
print(reverse("python"))

# 8.palindrome
def palindrome(word):
    return word == word[::-1]
print(maximum(10, 20, 30))

# 10. factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        return fact
print(factorial(5))




