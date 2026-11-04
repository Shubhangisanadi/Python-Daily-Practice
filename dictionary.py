
students = {
    "name": "Shubhangi",
    "age":  "22",
    "city": "pune",
    "marks": "85"
}
'''
keys = list(students.keys())
i = 0

# for loop in dictionary

for key in students:
    print(key)

for value in students.values():
    print(value)

for key, value in students.items():
    print(key, value)

# while loop in dictionary
while i < len(keys):
    print(keys[i])
    i += 1


Values = list(students.values())

i = 0
while i < len(Values):
    print(Values[i])
    i += 1'''

#print(students["name"])
#print(students["age"])
#students["course"] = "python"
#print(students)
#students["age"] = 23
#print(students)
#del students["city"]
#print(students)
'''
for key, value in students.():
    print(key, value)'''

'''
# methods
# 1. key method
stud = {
    "name" : "Shubhangi",
    "age"  : 22,
    "city" : "pune"
}
print(stud.keys())

# 2. value method
print(students.values())

# 3. items method
print(students.items())

# 4. get method
print(students.get("name"))

# agar key value nhi hai to default value bhi de skte hai.
#print(students.get("marks", 0))

# 5. update method
students.update({"age": 21})
print(students)

# 6. pop method
students.pop("city")
print(students)

# 7. clear method
students.clear()
print(students)

# 8. copy method
students = {"name": "Shubhangi", "age": "22"}
new_students = students.copy()
print(new_students)'''






'''
customer_info = {"cust_id": 111, "name": "Shubhangi", "city": "pune", "salary": 45000 }
print(customer_info)
print(customer_info.values())
print(customer_info.keys())
print(customer_info.clear())
print(customer_info.copy())
print(customer_info.items())
#customer_info.pop("city")
'''

# empty set
numbers = set()
print(numbers)
print(type(numbers))

# set in default value add 
numbers = set()

numbers.add(10)
numbers.add(20)
numbers.add(30)

print(numbers)

# direct set create
numbers = {10, 20, 30}
print(numbers)

# important difference
a = {}
b = set()
print(type(a))
print(type(b))