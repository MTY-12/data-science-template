# 1. Variables: 

students_count = 1000  # naming convention: snake_case using underscore
rating = 4.99  # float  
is_published = True  # boolean
course_name  = "Python Programming"  # string
multiple_lines= """ 


This is a multiple line string

"""

x,y = 1,2  # multiple assignment in one line
x =y = 1  # multiple assignment in one line 


# 2. Dynamic Typing: we can change the type of the variable at any time, it is not fixed or static like in other languages

students_count = "1000"  # now it is a string
print(type(students_count))  # <class 'str'>

students_count = 1000  # now it is an integer
print(type(students_count))  # <class 'int'>


type(1.1)  # <class 'float'> since python is a dynamic language, the type of variables are determined at runtime as opposed to compile time
type(True)  # <class 'bool'>
type("hello")  # <class 'str'>

# 3. Type annotations: by using type hints, ( setting mypy) we can specify the type of the variable, but it is not enforced by the interpreter
# it is just a hint for the developer or other tools like linters or IDEs
# for example, we can specify the type of the parameter and the return type of the function
def add(x: int, y: int) -> int:
    return x + y

# 4. Mutable and Immutable types: 

# Immutable types: int, float, bool, string, tuple 

x= 1
print(id(x))  # 1407266704 , the memory address of the variable x will not be affected because it is immutable
x= x+1
print(id(x))  # 1407266736, we get two different memory location because  x is immutable, so the value of x is changed and a new memory location is created for the new value of x


# Mutable types: list, set, dictionary

x = [1,2,3]
print(id(x))  # 1407266704, the memory address of the variable x will not be affected because it is mutable
x.append(4)
print(id(x))  # 1407266704, we get the same memory location because x is mutable, so the value of x is changed in the same memory location

# 5. Strings:

course = "Python Programming" # string
print(course[0])  # P, indexing starts at 0 in python
print(course[-1])  # g, negative indexing starts at -1 in python
print(course[0:3])  # Pyt, slicing, the first index is inclusive and the second index is exclusive
print(course[0:])  # Python Programming, if we omit the second index, it will go to the end of the string
print(course[:3])  # Pyt, if we omit the first index, it will start from the beginning of the string
print(course[:])  # Python Programming, if we omit both indices, it will return the whole string
another = course[:]  # we can copy the whole string using slicing
print(another)  # Python Programming
len(course)  # 18, the inbuilt function len() returns length of the string , len()  can be used to get the length of any iterable object like list, tuple, set, dictionary that contains elements

# 6. Escape Sequences:  \n, \t, \\, \', \"
course = "Python \"Programming"  # Python "Programming  , we can use backslash to escape the double quote
print(course)   # Python "Programming  
course = "Python \'Programming"  # Python 'Programming  , we can use backslash to escape the single quote
print(course)   # Python 'Programming  
course = "Python \\Programming"  # Python \Programming  , we can use backslash to escape the backslash
print(course)   # Python \Programming
course = "Python \nProgramming"  # Python  , we can use backslash n to create a new line
print(course)   # Programming   
course = "Python \tProgramming"  # Python  , we can use backslash t to create a tab
print(course)   # Programming

# 7. Formatted Strings:  f"{}" or .format() method  or % operator  or join() method or f-string with triple quotes  or f-string with expressions
first = "John"
last = "Smith"
full = first + " " + last  # John Smith, concatenation using + operator   
full = f"{first} {last}"  # John Smith, f-string   
full = " {} {} ".format(first, last)  # John Smith, .format() method
full = " %s %s " % (first, last)  # John Smith, % operator 
full = " ".join([first, last])  # John Smith, join() method
full = f"""
{first} {last}
"""  # John Smith, f-string with triple quotes  
full = f"{first} {last} is a {len(first)} letter name"  # John Smith is a 4 letter name, f-string with expressions 

# 8. String Methods:  since  everything in python is an object, we can call methods on strings means we can use the dot operator to call methods on strings
course = "Python Programming" # string  
print(course.upper())  # PYTHON PROGRAMMING, converts the string to uppercase
print(course.lower())  # python programming, converts the string to lowercase
print(course.title())  # Python Programming, converts the string to title case
print(course.strip())  # Python Programming, removes the leading and trailing whitespaces
print(course.find("Pro"))  # 7, returns the index of the first occurrence of the substring
print(course.replace("P", "-"))  # -ython -rogramming, replaces the first argument with the second argument
print("Pro" in course)  # True, checks if the substring is present in the string
print("swift" not in course)  # True, checks if the substring is not present in the string
print(course.split(" "))  # ['Python', 'Programming'], splits the string into a list of strings based on the delimiter
print(course.split("o"))  # ['Pyth', 'n Pr', 'gramming'], splits the string into a list of strings based on the delimiter

# 9. String Concatenation:  we can use the + operator to concatenate strings
first = "John"
last = "Smith"
full = first + " " + last  # John Smith, concatenation using + operator

# 10. String Interpolation:  we can use f-strings to interpolate variables in strings
first = "John"
last = "Smith"
full = f"{first} {last}"  # John Smith, f-string

# 11. NUMBERS: int, float, complex, bin , hex, oct, abs, round, pow, math module"
x = 1  # int 
y = 2.0  # float
z = 1 + 2j  # complex
bin(5)  # 0b101, binary
hex(5)  # 0x5, hexadecimal
oct(5)  # 0o5, octal
abs(-2)  # 2, absolute value
round(3.75)  # 4, round off
pow(2, 3)  # 8, power
import math  # math module
math.ceil(2.9)  # 3, ceiling
math.floor(2.9)  # 2, floor
math.sqrt(16)  # 4.0, square root
math.pi  # 3.141592653589793, pi
math.e  # 2.718281828459045, e

# 12. Arthmetic Operators: +, -, *, /, //, %, **
x = 10
y = 3
print(x + y)  # 13, addition
print(x - y)  # 7, subtraction
print(x * y)  # 30, multiplication
print(x / y)  # 3.3333333333333335, division
print(x // y)  # 3, floor division
print(x % y)  # 1, modulus
print(x ** y)  # 1000, exponentiation

# 13. Comparison Operators: >, <, >=, <=, ==, !=
x = 3
y = 2
print(x > y)  # True, greater than  
print(x < y)  # False, less than
print(x >= y)  # True, greater than or equal to
print(x <= y)  # False, less than or equal to
print(x == y)  # False, equal to
print(x != y)  # True, not equal to

# 14. Logical Operators: and, or, not
x = 3
y = 2
print(x > 2 and y > 1)  # True, and operator
print(x > 2 or y > 3)  # True, or operator
print(not x > 2)  # False, not operator

# 15. Ternary Operator:  x if condition else y
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)  # Eligible

# 16. Chaining Comparison Operators:  we can chain comparison operators
age = 22
if 18 <= age < 65:
    print("Eligible")  # Eligible

# 17. Lists:  ordered, mutable, allows duplicate elements, can contain different data types
numbers = [1, 2, 3, 4]  # list
numbers = list((1, 2, 3, 4))  # list
numbers = [1, 2, 3, 4]  # list
numbers = [1, 2.0, "three", True]  # list
numbers = [1, 2, 3, 4]  # list

# 18. List Methods:  since  everything in python is an object, we can call methods on lists means we can use the dot operator to call methods on lists
numbers = [1, 2, 3, 4]  # list
numbers.append(5)  # [1, 2, 3, 4, 5], adds an element to the end of the list
numbers.insert(0, 0)  # [0, 1, 2, 3, 4, 5], inserts an element at the specified index
numbers.remove(3)  # [0, 1, 2, 4, 5], removes the first occurrence of the element
numbers.pop()  # [0, 1, 2, 4], removes the last element
numbers.pop(0)  # [1, 2, 4], removes the element at the specified index
numbers.clear()  # [], removes all the elements
numbers = [1, 2, 3, 4]  # list
numbers.index(2)  # 1, returns the index of the first occurrence of the element
numbers.count(1)  # 1, returns the number of occurrences of the element
numbers.sort()  # [1, 2, 3, 4], sorts the elements in ascending order
numbers.reverse()  # [4, 3, 2, 1], reverses the elements

# 19. List Slicing:  we can use slicing to get a subset of the list
numbers = [1, 2, 3, 4]  # list
print(numbers[0])  # 1, indexing
print(numbers[-1])  # 4, negative indexing
print(numbers[0:3])  # [1, 2, 3], slicing
print(numbers[0:])  # [1, 2, 3, 4], slicing


# 20. List Comprehension:  we can use list comprehension to create a new list based on an existing list
numbers = [1, 2, 3, 4]  # list
doubled = [x * 2 for x in numbers]  # [2, 4, 6, 8], list comprehension
evens = [x for x in numbers if x % 2 == 0]  # [2, 4], list comprehension
odds = [x for x in numbers if x % 2 != 0]  # [1, 3], list comprehension

# 21. Tuples:  ordered, immutable, allows duplicate elements, can contain different data types
numbers = (1, 2, 3, 4)  # tuple
numbers = tuple((1, 2, 3, 4))  # tuple
numbers = (1, 2, 3, 4)  # tuple
numbers = (1, 2.0, "three", True)  # tuple
numbers = (1, 2, 3, 4)  # tuple

# 22. Sets:  unordered, mutable, no duplicate elements, can contain different data types
numbers = {1, 2, 3, 4}  # set
numbers = set((1, 2, 3, 4))  # set
numbers = {1, 2, 3, 4}  # set
numbers = {1, 2.0, "three", True}  # set
numbers = {1, 2, 3, 4}  # set

# 23. Set Methods:  since  everything in python is an object, we can call methods on sets means we can use the dot operator to call methods on sets
numbers = {1, 2, 3, 4}  # set
numbers.add(5)  # {1, 2, 3, 4, 5}, adds an element to the set
numbers.remove(3)  # {1, 2, 4, 5}, removes the element
numbers.discard(3)  # {1, 2, 4, 5}, removes the element if it is present
numbers.pop()  # {2, 4, 5}, removes a random element
numbers.clear()  # set(), removes all the elements
numbers = {1, 2, 3, 4}  # set
numbers2 = {3, 4, 5, 6}  # set
numbers.union(numbers2)  # {1, 2, 3, 4, 5, 6}, returns the union of two sets
numbers.intersection(numbers2)  # {3, 4}, returns the intersection of two sets
numbers.difference(numbers2)  # {1, 2}, returns the difference of two sets
numbers.symmetric_difference(numbers2)  # {1, 2, 5, 6}, returns the symmetric difference of two sets
numbers.issubset(numbers2)  # False, checks if the set is a subset of another set
numbers.issuperset(numbers2)  # False, checks if the set is a superset of another set
numbers.isdisjoint(numbers2)  # False, checks if the set has no intersection with another set

# 24. Dictionaries:  unordered, mutable, indexed, no duplicate keys, can contain different data types
person = {
    "first": "John",
    "last": "Smith",
    "age": 30
}  # dictionary
person = dict(first="John", last="Smith", age=30)  # dictionary
person = {
    "first": "John",
    "last": "Smith",
    "age": 30
}  # dictionary
person = {
    "first": "John",
    "last": "Smith",
    "age": 30
}  # dictionary
person = {
    "first": "John",
    "last": "Smith",
    "age": 30
}  # dictionary

# 25. Dictionary Methods:  since  everything in python is an object, we can call methods on dictionaries means we can use the dot operator to call methods on dictionaries
person = {
    "first": "John",
    "last": "Smith",
    "age": 30
}  # dictionary 
person["first"]  # John, indexing
person.get("first")  # John, indexing
person["first"] = "Jane"  # Jane, assignment
person["email"] = " [email protected]"  # [email protected], assignment
person.pop("age")  # 30, removes the element with the specified key
person.popitem()  # ('email', ' [email protected]'), removes the last element
person.clear()  # {}, removes all the elements

# 26. Dictionary Comprehension:  we can use dictionary comprehension to create a new dictionary based on an existing dictionary
person = {
    "first": "John",
    "last": "Smith",
    "age": 30
}  # dictionary
person = {k: v for k, v in person.items()}  # {'first': 'John', 'last': 'Smith', 'age': 30}, dictionary comprehension
person = {k: v for k, v in person.items() if k != "age"}  # {'first': 'John', 'last': 'Smith'}, dictionary comprehension

# 27. Functions:  block of code that only runs when it is called
def greet(): # function
    print("Hello")  # Hello, function
greet()  # Hello, function 

# 28. Function  which has self as an argument
def greet(self): # function
    print("Hello")  # Hello, function
greet("self")  # Hello, function


# 29. defining a function with a parameter self ??? 


# 28. Function Parameters:  we can pass parameters to functions
def greet(name): # function
    print(f"Hello, {name}")  # Hello, John, function
greet("John")  # Hello, John, function

# 29. Default Parameters:  we can set default values for parameters
def greet(name="John"): # function
    print(f"Hello, {name}")  # Hello, John, function
greet()  # Hello, John, function
greet("Jane")  # Hello, Jane, function

# 30. Return Statement:  we can return values from functions
def add(x, y): # function
    return x + y  # 3, function
result = add(1, 2)  # 3, function

# 31. Keyword Arguments:  we can pass arguments by specifying the parameter name
def greet(first, last): # function
    print(f"Hello, {first} {last}")  # Hello, John Smith, function
greet(first="John", last="Smith")  # Hello, John Smith, function

# 32. Arbitrary Arguments:  we can pass a variable number of arguments
def greet(*names): # function
    print(f"Hello, {names[0]}")  # Hello, John, function
greet("John", "Jane")  # Hello, John, function

# 33. Arbitrary Keyword Arguments:  we can pass a variable number of keyword arguments
def greet(**person): # function
    print(f"Hello, {person['first']}")  # Hello, John, function
greet(first="John", last="Smith")  # Hello, John, function

# 34. Scope:  the scope of a variable is the region of the code where it is defined
def greet(): # function
    message = "a"  # a, local variable
greet()  # a, local variable
print(message)  # NameError: name 'message' is not defined, global variable

# 35. Global Keyword:  we can use the global keyword to access a global variable inside a function
message = "a"  # a, global variable
def greet(): # function
    global message
    message = "b"  # b, global variable
greet()  # b, global variable
print(message)  # b, global variable

# 36. Modules:  a file containing a set of functions that can be included in other files
# Path: src/models/Python_basic.py
# Compare this snippet from src/models/test.py:
# print('hello world!')











