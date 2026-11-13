# 1. Variables
'''
a = 10
b = 20.5
c = "Shubhangi"
d = True
e = [1, 2, 3]
f = (10, 20)
g = {1, 2, 3}
h = {"name": "Shubhangi"}
i = None
j = 5 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))'''

# 2. Check data type before and after reassignment.
a = 10
print(type(a))

a = "Python"
print(type(a))

# 3. Store employee details.
emp_id = 101
name = "Rahul"
salary = 25000.50
department = "IT"
status = True

print(emp_id)
print(name)
print(salary)
print(department)
print(status)

# 4. Calculate rectangle area.
len = float(input("Enter leg: "))
width = float(input("Enter width: "))

area = leg * width

print("Area:", area)

# 5. Swap two variables without using a third variable.
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# Type Conversion
# 7.Convert "250" into integer and calculate square.

a = "250"
b = int(a)

print(b * b)

# 8.Convert 45 into float, string and boolean.
a = 45

print(float(a))
print(str(a))
print(bool(a))

# 9. Convert 99.99 into integer.
a = 99.99
b = int(a)

print(b)

# 10. Accept number as string and convert into integer.
a = input("Enter number: ")
b = int(a)
print(b)
print(type(b))

# 11. Calculate percentage after converting marks into numbers.
marks = input("Enter marks: ")
marks = float(marks)
percentage = (marks / 100) * 100
print("Percentage:", percentage)

# 12. Predict the output.
a = 100
b = 20.5

print(str(a) + str(b))
print(int(b))
print(float(a))
print(bool(0))
print(bool(""))

# String Data Type
# 13. Display full name in uppercase and lowercase.

name = input("Enter your name: ")

print(name.upper())
print(name.lower())

# 14. Count characters in a string.
name = "Shubhangi"
print(len(name))

# 15. Reverse a string without using reverse methods.
name  = "Python"
reverse = name[::-1]
print(reverse)

# 16. Count how many times 'a' appears.
name = "banana"
print(name.count("a"))

# 17.Replace spaces with hyphens.
text = "Python Full Stack"
print(text.replace(" ", "-"))

# 18. Check whether a word exists in a sentence.
sentence = "I like Python programming"
print("Python in sentence")

# 19. Extract username and domain from email.
email = "abc@gmail.com"
parts = email.split("@")

print("Username:", parts[0])
print("Domain:", parts[1])

# 20. Create a sentence using three variables.
name = "Shubhangi"
city = "Belagavi"
course = "Python"

print(f"My name is {name}. I live in {city}. I am learning {course}. ")

# List Data Type
# 21. Create a list of 15 numbers and find all numbers greater than 50.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 15, 25, 55, 65, 75]

for num in numbers:
    if num > 50:
        print(num)

# 22. Find the second-largest number in a list.
numbers = [10, 20, 50, 40, 30]
numbers.sort()

print("Second largest:", numbers[-2])

# 23. Remove duplicate elements from a list.
numbers = [10, 20, 10, 30, 20, 40]
new_list = list(set(numbers))
print(new_list)

# 24.Combine two lists into one list.
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b 
print(c)

# 25. find common elements between two lists.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = []

for num in a:
    if num in b:
        common.append(num)

print(common)

# 26. Count how many students passed(marks greater than equal to 40).
marks = [35, 45, 60, 25, 80, 30, 50]
count = 0
for mark in marks:
    if mark >= 40:
        count += 1
        print("Passed students:", count)

# 27. Separate positive, negative and zero values.
numbers = [10, -5, 0, 20, -10, 0, 5]
positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

# 28. find the sum of all even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for num in numbers:
    if num % 2 == 0:
        total += num
        print("Sum:", total)

# 29.Create a nested list and access individual elements.
students = [
    ["Rahul", 80],
    ["Priya", 90],
    ["Shubhangi", 85]
]
print(students[0][0])
print(students[1][1])
print(students[2][0])

# 30. Reverse a list  without reverse() or slicing.
numbers = [1, 2, 3, 4, 5]
reverse = []
for num in numbers:
    reverse.insert(0, num)
    print(reverse)

# Tuple Data Type 
# 31. Create a tuple of 15 numbers and find numbers greater than 50.

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 15, 25, 55, 65, 75)
for num in numbers:
    if num > 50:
        print(num)

# 32. find the second-largest number in a tuple.
numbers = (10, 20, 50, 40, 30)
new_list = sorted(numbers)
print(new_list[-2])

# 33. 
numbers = (10, 20, 10, 30, 20, 40)
new_list = tuple(set(numbers))
print(new_list)

# 34.
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b 
print(c)

#35. 
a = (1, 2, 3, 4,)
b = (3, 4, 5, 6)
common = []

for num in a:
    if num in b:
        common.append(num)
        print(tuple(common))

# 36.
marks = (35, 45, 60, 25, 80, 30, 50)
count = 0
for mark in marks:
    if mark >= 40:
        count += 1
        print("Passed:", count)

#37.
numbers = (10, -5, 0, 20, -10, 0, 5)
positive = []
negative = []
zero = []
for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero.append(num)
        print(tuple(positive))
        print(tuple(negative))
        print(tuple(zero))

# 38.
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
total = 0
for num in numbers:
    if num % 2 == 0:
        total += num
        print(total)

# 39.
students = (
    ("Rahul", 80),
    ("Priya", 90),
    ("Shubhangi", 85)
)
print(students[0][0])
print(students[1][1])
print(students[2][0])

#40.
numbers = (1, 2, 3, 4, 5)
reverse = ()
for num in numbers:
    reverse = (num,) + reverse
    print(reverse)

# Set Data Type 
# 41.
set1 = {101, 102, 103, 104}
set2 = {103, 104, 105, 106}

print(set1.intersection(set2))

# 42.
a = {1, 2, 3, 4, 5,}
b = {3, 4, 5, 6}
print(a.difference(b))

# 43.
a = {1, 2}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))

# 44.
name = "programming"
unique = set(name)
print(unique)

# 45.
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
common = a.intersection(b, c)
print(common)

# Dictionary Data Type
# 46.

employees = {
    "Rahul": 25000,
    "Priya": 30000,
    "Amit": 20000,
    "Sneha": 35000,
    "Raj": 28000
}
print(employees)

# 47.
employees = {
    "Rahul": 25000,
    "Priya": 30000,
    "Amit": 20000,
    "Sneha": 35000
}
highest = max(employees,
              key=employees.get)
print(highest)
print(employees[highest])

# 48.
employees = {
    "Rahul": 25000,
    "Priya": 30000,
    "Amit": 20000
}
total = sum(employees.values())
print("Total salary:", total)

# 49.
text = "banana"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
    print(frequency)

# 50.
keys = ["name", "age", "city"]
values = ["Rahul", 22, "Pune"]
data = dict(zip(keys, values))
print(data)

# 51.
a = {"name": "Rahul", "age": 22}
b = {"city": "pune", "course": "Pyhton"}
a.update(b)
print(a)

# 52.
products = {
    "Mobile": 12000,
    "Mouse": 500,
    "Keyboard": 2000,
    "Laptop": 45000
}
for name, price in products.items():
    if price > 1500:
        print(name, price)

# 53.
students = {
    "student1": {
        "name": "Rahul",
        "marks": 80
    },
    "student2": {
        "name": "Priya",
        "marks": 90
    },
    "student3": {
        "name": "Amit",
        "marks": 75
    }
}
print(students["student1"]["name"])
print(students["student2"]["marks"])
print(students["student3"]["name"])

# 54.
student = {
    "name": "Rahul",
    "age": 22,
    "city": "Pune"
}
if "name" in student:
    print("key exists")
else:
    print("key does not exist")

# 55.
marks = {
    "Python": 85,
    "SQL": 90,
    "HTML": 80,
    "CSS": 75
}
highest = max(marks, key=marks.get)
print("Highest subject:", highest)
print("Marks:", marks[highest])
