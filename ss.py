numbers = [10, 20, 30, 20 ]
unique = list(set(numbers))
print(unique)

# palindrome
num = 121
if str(num) == str(num)[::-1]:
    print("Palindrome number")
else:
    print("not palindrome")