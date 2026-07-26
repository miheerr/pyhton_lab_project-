#write a python code to create a dictionary

from unittest import result


emp = {
    "emp_name": "John",
    "salary": 50000,
    "age": 30,
    "city": "New York"
}

print(emp["age"])  # Output: 30
print(emp["city"])  # Output: New York
print(emp["emp_name"])  # Output: John
print(emp["salary"])  # Output: 50000


## SETS

#Remove the items that are duplicated in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print((set(list1) - set(list2)))  # Output: {1, 2, 3}
print((set(list1) ^ set(list2)))  # Output: {1, 2, 3, 6, 7, 8}

#UNION

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
print("Union:", union)

# Convert lists to sets and find the intersection
duplicates = set(list1) & set(list2)

print("Duplicates:", duplicates)

#Write a program using a for loop to print the factorial of a number
'''def factorial(n):
   result = 1
   for i in range(1, n + 1):
        result *= i
        return result

print(factorial(5))  # Output: 120'''

'''num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)'''

#using if and else 
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)
