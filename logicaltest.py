# List 

# 1.
a = [1, 2, 3, 2, 4, 1, 5]
b = []

for i in a:
    if i not in b:
        b.append(i)
        print(b)

# 2.
a = [10, 20, 40, 30, 50]
largest = a[0]
second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
        print("Second Largest:", second)

# 3.
a = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        print("Even:", even)
        print("Odd:", odd)

# 4.
a = [1, 2, 3, 1, 2, 4]
for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
            print(i, "=", count)

# 5.
a = [0, 1, 0, 3, 12, 0, 5]
b = []

for i in a:
    if i != 0:
        b.append(i)

        for i in a:
            if i == 0:
                b.append(i)
                print(b)

# Tuple
# 6.
a = (10, 20, 30, 40, 50)
b = ()
for i in a:
    b = (i,) + b
    print(b)

# 7.
a = (10, 50, 20, 5, 40)
maximum = a[0]
minimum = a[0]

for i in a:
    if i > maximum:
        maximum = i

        if i < minimum:
            minimum = i

            if i < minimum:
                minimum = i
                print("Maximum:", maximum)
                print("Minimum:", minimum)

# 8.
a = (10, 20, 30, 20, 40, 20, 50)
num = 20
count = 0

for i in a:
    if i == num:
        count += 1
        print("Frequency:", count)

# 9.
a = (1, 2, 3, 2, 4, 1, 5)
b = list(a)
c = []
for i in b:
    if i not in c:
        c.append(i)
d = tuple(c)
print(d)

# 10.
students = (
    ("Rahul", 85),
    ("Amit", 95),
    ("Sneha", 90),
    ("Priya", 80)
)

highest = students[0]

for i in students:
    if i[1] > highest[1]:
        highest = i
        print("Topper:", highest[0])
        print("Marks:", highest[1])

# 11.
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
x = set(a)
y = set(b)

common = x.intersection(y)
print(common)

# 12.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

x = set(a)
y = set(b)

unique = x.union(y)
print(unique)

# 13.
a = {1, 2}
b = {1, 2, 3, 4, 5}

flag = True

for i in a:
    if i not in b:
        flag = False
        break

    if flag:
        print("A is subset of B")
    else:
        print("A is not subset of B")

# 14.
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

common = a.intersection(b)
a = a - common
b = b - common

print("A:", a)
print("B:", b)

# 15.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

x = a - b
y = b - a
result = x.union(y)
print(result)

# DICTIONARY

# 16.
a = "programming"
b = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        print(d)

# 17.
a = "python is easy and python is powerful"
words = a.split()
d = {}

for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        print(d)

# 18.
students = {
    "Rahul": 85,
    "Amit" : 95,
    "Sneha" : 90,
    "Priya" : 80
}

highest = 0
name = ""

for i in students:
    if students[i] > highest:
        highest = students[i]
        name = i

        print("Student:", name)
        print("Highest Marks:", highest)

# 19.
d1 = {"a": 10, "b": 20}
b2 = {"b": 30, "c": 40}
b3 = {}

for i in d1:
    d3[i] = d1[i]

    for i in d2:
        if i in d3:
            d3[i] = d3[i] + d2[i]
else:
            d3[i] = d2[i]
            print(d3)

# 20.
d = {"Shubhangi": 85, "Rahul": 92, "Shradha": 78, "Omkar": 95}
items = list(d.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

            result = {}
            for i in items:
                result[i[0]] = i[1]
                print(result)
                



