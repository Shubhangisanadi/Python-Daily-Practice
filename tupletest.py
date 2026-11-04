
# 1. 
t = (5, )
print(type(t))

# 2.
t = (1, 2, 3)
# Tuple is immutable

# 3.
t = (10, 20, 30)
print(t.count(20))
print(t.index(20))

# 4.
t = (10, 20, 30, 20, 40)
print(t.count(20))

# 5.
t = (1, 2, 3)
print(t.index(5))   # valueerror

# 6.
t = (10, 20, 30, 40, 50)
print(t[1:4])

# 7.
t = (1, 2, 3)
# t[0] = 10  # typeerror

# 8.
t = (1, [2, 3], 4)
t[1][0] = 99
print(t)

# 9.
a, b, *c = (1, 2, 3, 4, 5)
print(c)

# 10.
print(tuple("python"))

# 11.
print("10:", (1, 2) < (1, 3))

# 12.


# 13.
t13 = (1, 2, 3)
print(type(t13))

# 14.


# 15.
print("15:", bool(()))

# 16.
marks = (56, [78, 90], 89)
print(len(marks))

# 17.
t17 = (10, 20, 10, 30, 10)
print( t17.index(10, 1))

# 18.
#t18 = (1, 2, 3)
#del t18[0]
#except TypeError as e:

#19.
age = (18, 21, 25, 30)
print(25 in age)

# 20 .
print((1, 2) + (3, 4))

# 22.
t = (10,)
print(type(t))

# 23.
a = (("apple", "Banana", "cherry"))
print(min("apple","banana","cherry"))

# 24.


# 25.
t1 = (1, 2, 3, 4)
print(t[-1])

# 26.
a = zip([1, 2], ('a','b'))

# 27.
print((0,)*4)

# 28.
t2 = (10, 20, 30)
print(30 in t)

# 29.

# 30.
t3 = (1, 2, 3)
print(sum(t, 10))

