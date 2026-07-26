'''print("what is your name?")
name = input()
print("hello " + name)

print("how old are you?")
age = input("Enter your age: ")
print("you are " + age + " years old"+ ".")

learning = input("What are you learning?, ")
print("you are learning " + learning + ".")'''

# variables
apple_type = "Granny Smith"
apple_color = "green"
apple_count = 5
print("I have " + str(apple_count) + " " + apple_type + " apples. They are " + apple_color + " in color.")

# data types
integer = 10
floating_point = 10.5
string = "Hello, World!"
boolean = True
print(type(integer))
print(type(floating_point))
print(type(string))
print(type(boolean))

# type conversion
num_str = "100"
num_int = int(num_str)
print(type(num_int))
num_float = float(num_str)
print(type(num_float))
num_str2 = str(num_int)
print(type(num_str2))

# basic operations
a = 10
b = 3
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a // b) # floor division
print(a % b)  # modulus
print(a ** b) # exponentiation

# string operations
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # concatenation
print(str1 * 3)            # repetition
print(len(str1))           # length
print(str1[0])             # indexing
print(str1[1:4])           # slicing
print(str1.lower())        # lowercase
print(str1.upper())        # uppercase
print(str1.replace("H", "J")) # replace
print(str1.split("e"))     # split
print("e" in str1)         # membership
print("z" not in str1)     # non-membership

# formatted strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))

# multiline strings
multiline_str = """This is a
multiline string."""
print(multiline_str)

# raw strings
raw_str = r"C:\new_folder\file.txt"
print(raw_str)

# escape characters
print("He said, \"Hello!\"")
print('It\'s a beautiful day!')
print("Line1\nLine2")
print("Column1\tColumn2")
print("This is a backslash: \\")
print("This is a bell sound: \a")
print("This is a carriage return: Hello\rWorld")
print("This is a form feed: Hello\fWorld")
print("This is a vertical tab: Hello\vWorld")
print("This is a unicode character: \u03A9")  # Omega symbol
print("This is a raw string: C:\\new_folder\\file.txt")

# comments
# This is a single-line comment
'''
This is a
multi-line comment
'''
"""
This is a docstring comment
"""
def example_function():
    """This is a docstring for the example_function."""
    pass
print(example_function.__doc__)

# input and output
user_input = input("Enter something: ")
print("You entered: " + user_input)
print("You entered: {}".format(user_input))
print(f"You entered: {user_input}")
print("You entered: %s" % user_input)

# conditional statements
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# loops
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    for i in range(5):
        print("i is:", i)
# break and continue
for i in range(10):
    if i == 5:
        break
    print("i is:", i)
    for i in range(10):
        if i % 2 == 0:
        continue
        print("i is:", i)

# functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Bob"))

# lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("date")
print(fruits)
print(fruits[1])
fruits.remove("banana")
print(fruits)
print(len(fruits))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

# dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)
print(person["name"])
person["age"] = 31
print(person)
person["job"] = "Engineer"
print(person)
del person["city"]
print(person)
print(person.keys())
print(person.values())
print(person.items())

# tuples
coordinates = (10, 20)
print(coordinates)
print(coordinates[0])
print(len(coordinates))

# sets
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
unique_numbers.add(6)
print(unique_numbers)
unique_numbers.remove(3)
print(unique_numbers)
print(4 in unique_numbers)
print(10 not in unique_numbers)

# file handling
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# error handling
'''try:
    result = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        try:
            num = int(input("Enter a number: "))
            print(f"You entered: {num}")
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")'''

# classes and objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return "Woof!"  
    my_dog = Dog("Buddy", 3)
    print(my_dog.name)
    print(my_dog.age)
    print(my_dog.bark())

# modules and packages
import math
print(math.sqrt(16))
from math import pi, factorial
print(pi)
print(factorial(5))
import random
print(random.randint(1, 10))
from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# list comprehensions
squares = [x**2 for x in range(10)]
print(squares)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# lambda functions
add = lambda x, y: x + y
print(add(5, 3))
multiply = lambda x, y: x * y
print(multiply(5, 3))

# map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

# generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(5):
    print(number)

# decorators
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print("Display function executed")
    display()

# iterators
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# comprehensions
my_dict = {x: x**2 for x in range(5)}
print(my_dict)
my_set = {x for x in range(5) if x % 2 == 0}
print(my_set)

# f-strings
name = "Charlie"
age = 25
print(f"My name is {name} and I am {age} years old.")

# type hints
def add_numbers(a: int, b: int) -> int:
    return a + b
print(add_numbers(5, 10))

# context managers
with open("example2.txt", "w") as file:
    file.write("This is another test file.\n")
with open("example2.txt", "r") as file:
    content = file.read()
    print(content)

# async and await
import asyncio
async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
    asyncio.run(main())

# f-strings with expressions
value = 10
print(f"The value is {value} and its square is {value**2}.")

# walrus operator
if (n := 10) > 5:
    print(f"{n} is greater than 5.")

# pattern matching (Python 3.10+)
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
print(http_status(200))
print(http_status(404))
print(http_status(123))

# structural pattern matching
def point_location(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"X-axis at {x}"
        case (0, y):
            return f"Y-axis at {y}"
        case (x, y) if x > 0 and y > 0:
            return "First quadrant"
        case (x, y) if x < 0 and y > 0:
            return "Second quadrant"
        case (x, y) if x < 0 and y < 0:
            return "Third quadrant"
        case (x, y) if x > 0 and y < 0:
            return "Fourth quadrant"
        case _:
            return "Unknown location"
print(point_location((0, 0)))
print(point_location((5, 0)))
print(point_location((0, -3)))
print(point_location((2, 3)))
print(point_location((-2, 3)))
print(point_location((-2, -3)))
print(point_location((2, -3)))
print(point_location((1, 1, 1)))

# end of the code