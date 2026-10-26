
# 1. Print numbers from 3 to 15

n = 3
while n <= 15:
    print(n)
    n += 1

# 2. Print Multiples of 4 up to 40

i = 4
while i <= 40:
    print(i)
    i += 1

# 3. Print numbers from 50 to 60

n = 50
while n <= 60:
    print(n)
    n += 1

# 4. Print numbers from 100 to 90
n = 100
while n >= 90:
    print(n)
    n += 1

# 5. Print numbers that end in 5
n = 5
while n <= 50:
    print(n)
    n += 10

# 6. Print multiple of 6 up to 60
n = 6
while n <= 60:
    print(n)
    n += 6

# 7. Print numbers from 1 to 20, skipping 5
n = 1
while n <= 20:
    if n != 5:
        print(n)
        n += 1

# 8. Print numbers from 1 to 20, skipping multiples of 3
n = 1 
while n <= 50:
    if n % 3 != 0:
        print(n)
        n += 1

# 9. Print numbers divisible by both 2 and 5
n = 1
while n <= 50:
    if n % 2 == 0 and n % 5 == 0:
        print(n)
        n += 1

# 10. Print numbers and their cubes
n = 1
while n <= 5:
    print(n, "cube =", n ** 3)
    n += 1

# 11. Count numbers divisible by 4 between 1 and 40
n = 1
count = 0
while n <= 40:
    if n % 4 == 0:
        count += 1
        n += 1
print(count)

# 12. find the product of numbers 1 to 5
n = 1
product = 1
while n <= 5:
    product += n
    n += 1

print(product)

# 13. find the sum of multiples of 7 up to 70
n = 7
total = 0
while n <= 70:
    total += n
    n += 7

print(total)

# 14. find the smallest number from a list
nums = [17, 8, 29, 4, 13]
i = 1
smallest = nums[0]

while i < len(nums):
    if nums[i] < smallest:
        smallest = nums[i]
    i += 1

print(smallest)

# 15. find the largest number from a list
nums = [17, 8, 29, 4, 13]
i = 1
largest = nums[0]

while i < len(nums):
    if nums[i] > largest:
        largest = nums[i]
        i += 1

print(largest)

# 16. Count positive numbers in a list
nums = [5, -2, 8, -7, 3]
i = 0
count = 0

while i < len(nums):
    if nums[i] > 0:
        count += 1
        i += 1

print(count)

# 17. count negative numbers in a list
nums = [5, -2, 8, -7, 3]
i = 0
count = 0

while i < len(nums):
    if nums[i] > 0:
        count += 1
        i += 1

print(count)

# 18. count zeros in a list
nums = [0, 4, 0, 7, 2, 0]
i = 0
count = 0

while i < len(nums):
    if nums[i] == 0:
        count += 1
        i += 1

print(count)

# 19. print a string one character at a time 
word = "coding"
i = 0
while i < len(word):
    print(word[i])
    i += 1

# 20. print a string in uppercase, character by character
word = "hello"
i = 0
while i < len(word):
    print(word[i].upper())
    i += 1

# 21. count spaces in a sentence
sentence = "Python is fun to learn"
i = 0
count = 0
while i < len(sentence):
    if sentence[i] == " ":
        count += 1
        i += 1
print(count)

# 22. count consonants in a word
word = "python"
i = 0
count = 0
while i < len(word):
    ch = word[i].lower()
    if ch.isalpha() and ch not in "aeiou":
        count += 1
        i += 1
print(count)

# 23. print list items in reverse order 
items = ["red", "blue", "green"]
i = len(items) - 1
while i >= 0:
    print(items[i])
    i -= 1

# 24. factorial using while loop
num = 5 
fact = 1
i = 1
while i <= num:
    fact = fact * i 
    i += 1
print("factorial =", fact)

# 25. palindrome number using while loop
num = 121
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not palindrome")
