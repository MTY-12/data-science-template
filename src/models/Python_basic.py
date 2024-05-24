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

# 9. String Concatenation:











