# V3------------------------
print("Hello, world!")

# V4-------------------------
name = "fares"  # string datatype
age = 20      # number datatype
is_male = True  # boolean datatype

print(name + " is " + str(age) + " years old")  # + sign here is called concatenation

# use comma sign instead of + if you want to print integer and string using print() function
print(age, "is your age")

# V5------------------------------
text = "Fares_hamdy"

print(text)
print(text + " \" " + text)
print(text + "\t"   + text)
print(text + " \\ " + text)

print(text.upper())
print(text.lower())
print(text.isupper())
print(text.islower())
print(text.lower().islower())

print(len(text))
print(len("codezilla"))

# print the characters of string by the index
print(text[0], text[5])

# index() used to get the index number of a character from the string
print(text.index("h"))

# replace() used string characters with another string
print(text.replace("Fares", "amir"))

# V6-----------------------------------------
# we can print any number or any operation result using the print function directly
num = -55

print(3)
print(-3)
print(3.44)
print(3 * 4)
print(3 + 4)
print(3 / 4)
print(3 - 4)

print(num)

# str() is a function used to convert numbers to strings
print(str(num))

# we can't print numbers with another string, so we should convert the number into a string firstly
print(str(num) + " is my favorite number")

# abs() is a function used to get the absolute (positive form) of any number
print(abs(num))

# pow() is a function used to get the result of a power operation
print(pow(2, 3))  # 2^3

# max() is a function used to get the biggest number of its two parameters
print(max(2, 4))

# min() is a function used to get the smallest number of its two parameters
print(min(2, 4))

# max() is a function used to get the round number of its float (fractional number) parameter
print(round(2.4))

# from math library import all functions
from math import *

# floor() is a function in the math library used to round its parameter number to the smaller value
print(floor(2.9))

# ceil() is a function in the math library used to round its parameter number to the bigger value
print(ceil(2.9))

# sqrt() is a function in the math library used to get the square root of its parameter number
print(sqrt(9))

# V7------------------------------------------------------
# input() is a function used to get data from the user and return it in string form
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name + ", your age is " + age)

# V8------------------------------------------------------
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# int() used to convert the parameter string into an integer
result1 = int(num1) + int(num2)

# float() used to convert the parameter string into an integer
result2 = float(num1) + float(num2)

print(num1 + " + " + num2 + " = " + str(result1))
print(num1 + " + " + num2 + " = " + str(result2))

# V9------------------------------------------------------
# Mad Libs game using variables

# V10------------------------------------------------------
# Lists
friends = ["fares", "amir", "ibrahim", 55, ["list2", 33]]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])

# print list from index(1) to index(3) where index(3) value will be excluded
print(friends[1:3])

# print list from index(1) to the end of the list
print(friends[1:])

# replace index(2) value with another value
friends[2] = "zeen"
print(friends[2])

# print element from a nested list
print(friends[4][1])

# V11------------------------------------------------------
codezilla = ["codezilla1", "codezilla2", "codezilla3", "codezilla4"]
friends2 = ["fares", "amir", "ibrahim"]

# extend() used to extend the list with another list
codezilla.extend(friends2)
# OR
codezilla += friends2

# append() used to add elements to the end of the list
codezilla.append("the added one")

# insert(index, object) used to add an element to the list at a particular index
codezilla.insert(2, "the added one")

# remove() is used to remove an element from the list
codezilla.remove("codezilla1")

# clear() is used to clear the list (remove all elements)
codezilla.clear()

# pop() is used to remove the last element of the list and return this element
what_was_popped = codezilla.pop()
print(what_was_popped)

# index() is used to validate if the input string exists in the list and return the index of this element
print(codezilla.index("codezilla1"))

# count() is used to count the duplicates of its parameter string and return the number of them
print(codezilla.count("fares"))

# sort() is used to sort the elements of the list in alphabetical order
print(codezilla.sort())

# copy() is used to make a shallow copy of the list (any changes on the original list will not happen on the new one)
list_new = codezilla.copy()

# not a shallow copy (any changes on the original list will happen on the new one)
list_new1 = codezilla

# V12------------------------------------------------------
# Tuples

# We can't change the tuple's values after initializing it,
# so it is used with constant values
coordinates = (25, 33, 43)

print(coordinates)
print(coordinates[0])
print(coordinates[1])
print(coordinates[2])

list_of_tuples = [(2, 3), (4, 5), (6, 7)]

print(list_of_tuples[0])
print(list_of_tuples[0][0])
print(list_of_tuples[0][1])

# V13------------------------------------------------------
# Functions

# def is the keyword for defining functions in Python
def fun1():
    # You should indent each line of the function body
    # with a tab space to define the function's scope.
    print("Hello sir\n")
    print("Hello world")

# Call the function
fun1()

# ******************
def fun2(name0):
    # "name0" here is a parameter variable for the function
    print("hello " + name0)

# "faris" is the parameter value of the "name" variable
fun2("faris")  # Call the function

# ******************
# Function with more than one parameter
def fun3(name, age, color):
    # "name", "age", and "color" here are parameter variables for the function
    print("hello " + name + ", your age is " + str(age) + " and your favorite color is " + color)

# "amir", "25", and "black" are the parameter values for "name", "age", and "color" variables
fun3("amir", 25, "black")

# V14--------------------------------------------------------------
# Function to calculate the cube of a number
def fun4(num0):
    cube = num0 * num0 * num0
    return cube  # "return" is the last line of the function, and any code after it will not execute

fun4(3)

# OR
def fun5(num0):
    return num0 * num0 * num0

fun5(4)

# V15--------------------------------------------------------------
# Conditional statements (if, elif, else)
is_hungry = False
wants_to_eat = True

if is_hungry and wants_to_eat:  # If the first condition is true and the second one is true
    print("Go eat, you are hungry")
if is_hungry and not wants_to_eat:  # If the first condition is true and the second one is not true
    print("Eat so you can survive")
elif not is_hungry and wants_to_eat:  # If the first condition is not true and the second one is true
    print("Don't eat, you are not hungry")
else:  # If all conditions above are not true
    print("Don't eat")

# V16--------------------------------------------------------------
# Comparisons and logical operators
# Comparisons:
# str1 == str2 (Equal)
# str1 != str2 (Not Equal)
# str1 >= str2 (Greater than or Equal)
# str1 <= str2 (Less than or Equal)
# str1 > str2 (Greater than)
# str1 < str2 (Less than)

# Function to match two strings
def match_strings(str1, str2):
    if str1 == str2:
        print("The strings match")
    else:
        print("The strings do not match")

match_strings("faris", "fares")

# V17--------------------------------------------------------------
# Calculator
def calculator():
    num1 = float(input("Enter the first number: "))
    operation = input("1 - (+)\n2 - (-)\n3 - (*)\n4 - (/)\nEnter the operation number: ")
    num2 = float(input("Enter the second number: "))

    if operation == '1':
        print(num1 + num2)
    elif operation == '2':
        print(num1 - num2)
    elif operation == '3':
        print(num1 * num2)
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(num1 / num2)
    else:
        print("Invalid operation")

# Call the calculator function
calculator()

# V18--------------------------------------------------------------
# Dictionaries
# All keys in the dictionary should be different, and if there are duplicate keys, the last one will be used.

convert_month = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    4: "April",
    5: True,
    "list": [1, 2, "Hello"]
}

# Getting values from the dictionary
# First way
print(convert_month["jan"])
print(convert_month[4])

# Second way is recommended because it can provide a default value if the key is not found
print(convert_month.get("list", "The value doesn't exist")[0])

# V19--------------------------------------------------------------
# While loop
i = 1
while i <= 10:
    print(i)
    if i == 6:
        continue  # Skip the iteration if the condition is true
    i += 1
    if i == 9:
        break  # Exit the loop if the condition is true
else:  # Will execute once when the while condition becomes false
    print("The condition is false")

# V20--------------------------------------------------------------
# For loop
buddies = ["faris", "amir", "ibrahim", "winner"]

# Will print the list
for x in buddies:
    print(x)

# Will print the characters of the string
for letter in "faris_hamdi":
    print(letter)

# Will print numbers from 0 to 9
for number in range(10):
    print(number)

# Will print numbers from 5 to 19
for y in range(5, 20):
    print(y)

# Will print numbers from 0 to 3 (length of the list)
for x in range(len(buddies)):
    print(x)

# Will print the elements of the list using their index
for index in range(len(buddies)):
    print(buddies[index])

# To get a string's index in a list
for buddy in range(len(buddies)):
    if buddies[buddy] == "winner":
        print(buddy, "is the winner")
    else:
        print(buddy, "is not the winner")

for buddy in buddies:
    if buddy == "amir":
        print(buddy, "is your brother")
        break  # Break the loop when buddy becomes "amir"
else:  # Execute when the for loop condition becomes false
    print("Not found")

for x in range(3, 10):
    if x == 5:
        continue  # Skip the iteration when x becomes 5
    print(x, "is the chosen number")

# V21--------------------------------------------------------------
# Exponentiation
# 2^3
print(2**3)

# Function to calculate the power of a number
def power0(base_num, pow_num):
    result = 1
    for n in range(pow_num):
        result *= base_num
    return result

print(power0(2, 3))  # 2^3

# V22--------------------------------------------------------------
# 2D Lists
no_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Will print the whole list
print(no_list)

# Will print [4, 5, 6]
print(no_list[1])

# Will print 4
print(no_list[1][0])

# Nested loops
for row in no_list:
    for column in row:
        # Will print the 2D list elements
        print(column)

# V23--------------------------------------------------------------
# Comments
'''
Multi-line comment
'''

# V24--------------------------------------------------------------
# Errors
try:
    result = 10 / 0
    value = int(input("Enter a number: "))
    print(value)
except ZeroDivisionError as err:
    print(err)
except ValueError as err1:
    print(err1)
except:
    print("Default error")

print("Success, errors haven't terminated the program")

# V25--------------------------------------------------------------
# Reading files
'''
"r"  > Read
"r+" > Read and write, cursor is at the beginning of the file
"w"  > Overwrite (delete the previous text and write new one)
"w+" > Overwrite and read (delete the previous text and write/read new one)
"a"  > Append (write and the cursor is at the end of the file)
"a+" > Read and write, cursor is at the beginning of the file
'''

# Read mode
# "workers.txt" is a text file that should be in the same folder as the project
workers_file = open("workers.txt", "r")

# readable() is a function that returns True or False and is used to check if the file is readable or not
print(workers_file.readable())

# read() is a function used to read the file in read mode
print(workers_file.read())

# readline() is used to read the file line by line, and after reading a line, it moves the cursor to the next line
print(workers_file.readline())

# readlines() is used to read all the lines from a file and return them as a list of strings.
# Each element of the list corresponds to a line from the file.
print(workers_file.readlines())

# Fetching the elements of the list
for worker in workers_file.readlines():
    print(worker)

# Close() is a function used to close the file
workers_file.close()

# V26--------------------------------------------------------------
# Writing files
# The function will create the file if it doesn't exist.
# "a", "a+", "w", and "w+" modes work the same way.
workers_file = open("workers.txt", "w")

# write() is a function used to write to the file in write mode
workers_file.write("\nhunter x hunter")

list_of_phrases = ["\nthis is a first line", "\nthis is a second line", "\nthis is a third line"]
# writelines() is a function used to write a bunch of lines like the ones in the list to the file
workers_file.writelines(list_of_phrases)

workers_file.close()

# V27--------------------------------------------------------------
# Modules: Using Python files in another project

# Import the "test0" module
from venv import test0

# roll_dice() is a function in the "test0" module
print(test0.roll_dice(9))

# You can search for more Python 3 modules

# Python 3 has built-in modules like base64 and docx
# The docx module is used to write/read Microsoft Word files but needs to be installed first
''' import docx '''

 # print(docx.fun1)

# V28--------------------------------------------------------------
# Classes: Creating new data types
# The first letter of the class name should be capitalized
class Employee:
    # The __init__ function initializes the class variables (specifications)
    def __init__(self, name0, age0, department0, is_manager0, rating0):
        self.name0 = name0
        self.age0 = age0
        self.department0 = department0
        self.is_manager0 = is_manager0
        self.rating0 = rating0

# You should import the file that contains the class if they are not in the same file
# The class file and the class name
''' from Employee_file import Employee '''

# Creating objects (should be outside the scope of the class and the function)
employee1 = Employee("faris", 20, "Google", True, 5)
employee2 = Employee("amir", 16, "Open AI", False, 3)

# Accessing the attributes of objects (should be outside the scope of the class and the function)
print(employee1.age0, employee2.name0, employee1.department0)

# V29--------------------------------------------------------------
# Classes: Methods and functions in classes
class Student:
    def __init__(self, name0, age0, department0, rating0):
        self.name0 = name0
        self.age0 = age0
        self.department0 = department0
        self.rating0 = rating0

    # Class function (should be in the class's scope)
    def is_excellent(self):
        if self.rating0 >= 15:
            return True
        else:
            return False

student1 = Student("faris", 20, "Computer Science", 19)
student2 = Student("amir", 16, "Biology", 5)

# Using the class function
print(student1.is_excellent())
print(student2.is_excellent())

# V30--------------------------------------------------------------
# Class inheritance
class Doctor:
    def studied_years(self):
        print("I studied for 7 years")

    def work_where(self):
        print("I work in a hospital")

    def paid_by_who(self):
        print("I get paid by the government")

# Creating an object
doctor1 = Doctor()

doctor1.studied_years()
doctor1.work_where()
doctor1.paid_by_who()

# Class inheritance
class FamilyDoctor(Doctor):
    def what_specialization(self):
        print("I work with families")

    # Overriding the method from the parent class
    def paid_by_who(self):
        print("I get paid by the people")

# Creating an object of the subclass
doctor2 = FamilyDoctor()

doctor2.work_where()  # Inherited method from the parent class
doctor2.paid_by_who()  # Overridden method in the subclass
