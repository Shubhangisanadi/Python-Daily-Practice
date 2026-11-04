
# 1. even or odd
num = int(input("enter number :"))

if num % 2 == 0:
    print("even number")
else:
    print("odd number")

# 2. Positive negative 
num = int(input("enter number:"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("zero")

# 3. reversr 

num = 12345
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

    print(rev)

# using for loop
num = 12345
rev = 0

for i in range(5):
    digit  = num % 10
    rev = rev * 10 + digit
    num = num // 10
    print(rev)

# 4.
num = 121
temp = num 
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    print("palindrome")
else:
    print("not palindrome")

# 5.
num = 7
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
        if count == 2:
            print("prime number")
        else:
            print("not prime")

# 6.
for num in range(2, 101):
    count = 0
    for i in range(1, num + 1):
        if num % 1 == 0:
            count += 1

        if count == 2:
            print(num)

# 7.
num = 5 
fact = 1
for i in range(1, num + 1):
    fact = fact * 1
    print("factorial :",fact)

# 8.
num = 5
square = num ** 2
cube = num ** 3
print("square:", square)
print("cube:", cube)

# 9.
name = "Python"
rev = ""
for i in name:
    rev = i + rev
print(rev)


# list 
# 1.
list = [10, 15, 20, 7, 30, 11]
for i in list:
    if i % 2 == 0:
        print("even:",i)
    else:
        print("odd:", i)

# 2.
my_list = [10, 15, 20, 7, 30, 11]
even = 0
odd = 0
for i in my_list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        print("even count:", even)
        print("odd count:", odd)

# 3.
a = [10,20,30, 40, 50]
rev = []
for i in a:
    rev = [i] + rev
    print(rev)

# 4.
a = [2,4,5,7,9,11,15]
for num in a:
    count = 0
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
                if count == 2:
                    print(num)

# 5.
x = [10, "python", 20, "java", 30, "sql"]
for i in x:
    if isinstance(i, str):
        print(i)

# 6.
y = [10, "python", 20, "java", 30, 5.5]
for i in y:
    if type(i) == int:
        print(i)

# tuple
# 1.
t = (10, 20, 30, 40, 50)
print(max(t))

# 2.
t = (10, 20, 30, 40, 50)
print(min(t))

# 3. 
t = (10, 20, 30, 40, 50)
print(sum(t))

# 4.
t = (10, 20, 30, 40, 50)
count = 0
for i in t:
    count += 1
    print(count)

# 5.
t = (10, 20, 30, 40, 50)
total = 0
for i in t:
    total += i
    print(total)

# 6.
t = (10, 15, 20, 25, 30, 35)
for i in t:
    if i % 2 == 0:
        print(i)

# dict
# 1.
student = {
    "Shubhangi": 80,
    "Siya": 55,
    "Rahul": 90,
    "Priya": 65
} 
for key, value in student.items():
    print(key,value)

# 2.
student = {
    "Shubhangi": 80,
    "Siya": 55,
    "Rahul": 90,
    "Priya": 65
} 
total = 0
for marks in student.values():
    total += marks
    print("total marks:", total)

# 3.
student = {
    "Shubhangi": 80,
    "Siya": 55,
    "Rahul": 90,
    "Priya": 65
} 
for name, marks in student.items():
    if marks > 60:
        print(name, marks)

# 4.
student = {
    "Shubhangi": 80,
    "Siya": 55,
    "Rahul": 90,
    "Priya": 65
} 
count = 0
for marks in student.values():
    if marks >= 40:
        count += 1
        print("passed students:", count)

# 5.
student = {
    "Shubhangi": 80,
    "Siya": 55,
    "Rahul": 90,
    "Priya": 65
} 
highest = 0
for marks in student.values():
    if marks > highest:
        highest = marks
        print("highest marks:", highest)












            