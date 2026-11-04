x = [10, 20, 30, 40]
print(x[2])

# 2.
x = [1, 2, 3]
x.append(4)
print(x)

# 3.
x = [10, 20, 30]
x.insert(1, 99)
print(x)

# 4.
x = [1, 2, 3, 4, 5]
print(x[1:4])

# 5.
x = [10, 20, 30, 40]
print(x[-2])

# 6.
x = [1, 2, 3]
x.extend([4, 5])
print(x)

# 7.
x = [10, 20, 30]
print(x.pop())
print(x)

# 8.
x = [10, 20, 30, 20]
x.remove(20)
print(x)

# 9.
x = [5, 2, 8, 1]
x.sort()
print(x)

# 10.
x = [1, 2, 3, 4]
x.remove()
print(x)

# 11.
x = [10, 20, 30]
y = x
y.append(40)
print(x)

# 12.
x = [10, 20, 30]
y = x.copy()
y.append(40)
print(x)
print(y)

# 13.
x = [[1, 2,], [3, 4], [5, 6]]
print(x[1][0])

# 14.
x = [1, 2, 3, 4, 5]
print(x[::-1])

#15
x = [1, 2, 3]
print(x * 2)

# S-B --Tuple
# 16.
x = (10, 20, 30)
print(x[1])

# 17.
x = (1, 2, 3, 4)
print(x[-1])

# 18.
x = (10, 20, 30, 40)
print(x[1:3])

# 19.
x = (1, 2, 3)
print(len(x))

# 20.
x = (10,)
print(type(x))

# 21.
x = (10)
print(type(x))

# 22.
x = (1, 2, 3)
y = (4, 5)
print(x + y)

# 23.
x = (1, 2)
print(x * 3)

# 24.
x = (10, 20, 30)
a, b, c = x
print(a, b, c)

# 25.
x = (10, 20, 30, 40)
a, *b = x
print(a)
print(b)

# 26.
x = (1, 2, 3, 2, 2)
print(x.count(2))

# 27.
x = (10, 20, 30)
print(x.index(20))

# 28.
x = ([])