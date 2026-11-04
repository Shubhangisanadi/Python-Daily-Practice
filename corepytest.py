# 3.
a = 10
print(id(a))

# 4.
name = input("Enter your name:")

print(name)
print(type(name))

# 5.
my_var = 10     
print(my_var)

# 6.
a = 10
b = "python"
c = 10.5

print(type(a))
print(type(b))
print(type(c))

# 7.
a = 1 / 2

print(a)
print(type(a))

# 8.
name = "Shubhangi"
age = 21

print(name)
print(age)

# 9.
print(17 // 4)

# 10.
print(bool("False"))

# 11.
a = 10
b = a
print(a)
print(b)

# 12.
student_name = "Shubhangi"
print(student_name)

# 13.
name = "Python"
print(name)

# 14.
a = 256
b = 256
print(id(a) == id(b))

# 15.
print(type([]))

# 16.
data = (10, 20, 30)
print(type(data))

# 17.
a, b, c = map(int, input("Enter 3 numbers: ").split())
print(a, b, c)

# 18.
print(0.1 + 0.2 == 0.3)

# 19.
name = "Python"
print(repr(name))

# IF - ELSE MATCH CASE

# 21
marks = 75
if marks >= 90:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("C Grade")

# 22.
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")

# 23.
number = 5
match number:
    case 1:
        print("One")
    case _:
        print("Other number")

# 24.
x = 10
if x > 15:
    print("A")
else:
    print("B")

# 26.
a = 10
b = 20

if a > 5 and b > 10:
    print("True")
else:
    print("False")

# 27.
res = "Even" if 4 % 2 == 0 else "Odd"
print(res)

# 28.
number = 2
match number:
    case 1 | 2:
        print("One or Two")
    case _:
        print("Other")

# 29.
x = 10

match x:
    case n if n > 0:
        print("Positive")
    case _:
        print("Negative or zero")

# 30.
print(bool([]))
print(bool(0))
print(bool("0"))
print(bool(None))

# 31.
a = False

print(a and 10)
print(True or 20)

# 32.
print(5 and 10)

# 33.
print(0 or "Python")

# 34.
if 10 > 5:
    print("Hello")
    print("Python")

# 35.
if 10 > 5:
    pass

print("Program completed")

# LOOPS & ITERATION

# 36.
for i in range(2, 8, 2):
    print(i)

# 40.
items = ["Apple", "Mango", "Banana"]

for i, v in enumerate(items):
    print(i, v)

# 41.
i = 1
while i < 4:
    print(i, end="")
    print(i, end="")
    i += 1

# 42.
a = [1, 2, 3]
b = ["A", "B", "C"]

print(list(zip(a, b)))

# 45.
print(sum(range(1, 5)))

# 47.
result = [x * 2 for x in range(3)]
print(result)

# 50.
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Completed")

# 51.
t = (1,)
print(t)
print(type(t))

# 53.
lst = [1, 2, 3]
lst.append([4, 5])
print(lst)

# 54.
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)     

# 55.
lst = [10, 20, 30]
x = lst.pop()

print(x)
print(lst)

# 56.
a = [1, 2]
b = [3, 4]

print(a + b)

# 57.
a = (1, 2, 3)
a[0] = 99

print(a)

# 59.
lst = [10, 20, 30]
print(lst.index(20))

# 61.
lst = [10, 20, 30]
lst.remove(40)

# 62.
lst = [5, 2, 8, 1]

lst.sort()
print(lst)

# 65.
lst = [1, 2, 2, 3, 2]
print(lst.count(2))

# 66.
a = (1, 2)
print(a * 2)

# 68.
lst = [10, 20, 40]

lst.insert(2, 30)
print(lst)

# 69.
a = list("cat")
print(a)

# DICTIONARY & SET

# 71.
d = {}
print(d)

d = dict()
print(d)

# 72.
s = set()
print(s)

# 74.
d = {"name:" "Shubhangi"}

print(d["age"])
print(d.get("age"))

# 77.
s = {1, 2, 2, 3}
print(s)

# 78.
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

# 79.
A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)

# 80.
s = {1, 2}

s.add(3)
print(s)

# 81.
s = {1, 2, 3}

s.discard(5)
print(s)

s.remove(5)
print(s)

# 83.
d = {"name": "Shubhangi", "age": 21}

print(d.items())
print(list(d.items()))

# 84.
d = {"a": 1}
d.update({"b": 2})

print(d)

# 85.
d = {"a": 1, "b": 2, "c": 3}

print(d.popitem())
print(d)

# 86.
s = frozenset([1, 2])
s.add(3)
print(s)

# 87 - 88.
A = {1, 2, 3}
B = {3, 4, 5}
print(A ^ B)
print(A.symmetric_difference(B))

# 89.
d = {"a": 1, "b": 2, "a": 3}
print(d)
print(len(d))

# SET AND DICTIONARY PROGRAMS
# 90.
s = {1, 2, 3}
a.add([4, 5])
print(s)

# 91.
d = {"name": "Shubhangi", "age": 21}
d.clear()
print(d)

# 92.
d = {"a": 1, "b": 2}
print("a" in d)
print(1 in d)

# 93.
numbers = [1, 2, 3, 4, 5]
d = {x: x*x for x in numbers}
print(d)



        
        

