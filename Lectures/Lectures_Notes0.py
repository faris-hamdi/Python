# ENG.FARIS HAMDI RIZK

# V3------------------------

print("Hello, world!")

# V4-------------------------

name = "fares"  # string datatype
age = 20      # number datatype
is_male = True  # boolean datatype

print(name + "is " + str(age) + " years old") # + sign here is called concatenation

# use comma sign instead of + # if you want to print integer and string using print() function
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
print(text[0],text[5])

# index() used to get the index number of a character from string
print(text.index("h"))

# replace() used string characters with another string
print(text.replace("Fares","amir"))



# V6-----------------------------------------

# we can print any number or any operation result using print function directly
num = -55

print(3)
print(-3)
print(3.44)
print(3*4)
print(3+4)
print(3/4)
print(3-4)

print(num)

# str() is a function used to convert numbers to strings
print(str(num))

# we can't print numbers with another string ,so we should convert the number into string firstly
print(str(num) + " is my favourite number")

# abs() is a function used to get the absolute (positive form) of any number
print(abs(num))

# pow() is a function used to get the result of power operation
print(pow(2,3))  # 2^3

# max() is a function used to get the biggest number of its two parameters numbers
print(max(2,4))

# min() is a function used to get the smallest number of its two parameters numbers
print(min(2,4))

# max() is a function used to get the round number of its float(fractional number) parameter
print(round(2.4))

# from math library import all functions
from math import *

# floor() is a function in math library used to round its parameter number to the smaller value
print(floor(2.9))

# ceil() is a function in math library used to round its parameter number to the bigger value
print(ceil(2.9))

# sqrt() is a function in math library used to get the square root of its parameter number
print(sqrt(9))


# V7------------------------------------------------------

# input() is a function used to get data from user and return it in string form
name = input("Enter your name: ")
age = input("Enter your age: ")

print("hello "+name+" your age is "+age)


# V8------------------------------------------------------


num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# int() used to convert the parameter string into integer
result1 = int(num1) + int(num2)

# float() used to convert the parameter string into integer
result2 = float(num1) + float(num2)

print(num1 + " + " + num2 + "=" + str(result1))
print(num1 + " + " + num2 + "=" + str(result2))


# V9------------------------------------------------------

# madlibs game using variables

# V10------------------------------------------------------

# lists

friends = ["fares", "amir", "ibrahim", 55, ["list2", 33]]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])

# print list from index(1) to index(3) which index(3) value will be excluded
print(friends[1:3])

# print list from index(1) to the end of the list
print(friends[1:])

# replace index(2) value by another value
friends[2] = "zeen"
print(friends[2])

# print element from nested list
print(friends[4][1])

# V11------------------------------------------------------

codezilla = ["codezilla1","codezilla2","codezilla3","codezilla4"]

friends2 = ["fares", "amir", "ibrahim"]

# extend() used to extend list with another list
codezilla.extend(friends2)
# OR
codezilla += friends2

# append() used to add elements on the end of list
codezilla.append("the added one")

# insert(index, object) used to add element to list in particular index
codezilla.insert(2,"the added one")

# remove() is used to remove element from list
codezilla.remove("codezilla1")

# clear() is used to clear the list (remove all elemenmts)
codezilla.clear()

# pop() is used to remove the last element of th list and return this element
what_was_popped = codezilla.pop()
print(what_was_popped)

# index() is used to validate if the input string is exist in the list and return the index of this element
print(codezilla.index("codezilla1"))

# count() is used to count the duplicates of its parameter string and return the number of them
print(codezilla.count("fares"))

# sort() is used to sort the elements of the list by the alphabetic order
print(codezilla.sort())

# copy() is used to make a shallow copy of list (any changes on the original list will not happen on the new one)
list_new = codezilla.copy()

# not shallow copy (any changes on the original list will happen on the new one)
list_new1 = codezilla


# V12------------------------------------------------------

# tuples

# we can't change the tuple's values after initialized it
# so it used with constant values
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

# def is the key word of the functions in python
def fun1():  # you should let two blank lines before the function definition
    # you should let tab space before every code line of the function body code to be at the function scope
    print("Hello sir\n")
    print("Hello world")


# you should let two blank lines after the last line code of the function body code
fun1()  # function call


# ******************

def fun2(name0):  # name here is a parameter variable for the function
    print("hello " + name0)


# "faris" is the parameter value of name variable
fun2("faris")  # the function call


# ******************

# function with more than one parameter


def fun3(name, age, color):  # name , age and color here are parameters variables for the function
    print("hello " + name + "your age is " + str(age) + "and yor favorite color is" + color)


# "amir" , "25" and black are the parameters values of name and age variables
fun3("amir", 25, "black")


# V14---------------------------------------------------------------


def fun4(num0):
    cube = num0 * num0 * num0
    return cube  # return is the last line of the function and any line in the function after return will not execute


fun4(3)


# OR >>>
def fun5(num0):
    return num0 * num0 * num0


fun5(4)

# V15---------------------------------------------------------------

is_hungry = False
wants_to_eat = True

if is_hungry and wants_to_eat:  # if the first condition is true and the second one is true
    print("go eat you are hungry")
if is_hungry and not wants_to_eat:  # if the first condition is true and the second one is not true
    print("eat so you can survive")
elif not is_hungry and wants_to_eat:  # if the first condition is not true and the second one is true
    print("don't eat you are not hungry")
else:  # if all conditions above is not true
    print("don't eat")


# V16---------------------------------------------------------------


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(1, 2, 3))

# max() is pre-made function used to get the biggest number of the parameter's number
print(max(1, 2, 3, 4))

# logical operators
# str1 == str2
# str1 != str2
# str1 >= str2
# str1 <= str2
# str1 > str2
# str1 < str2


def match_strings(str1, str2):
    if str1 == str2:
        print("the strings is matched")
    else:
        print("the strings is nt matched")


match_strings("faris", "fares")


# V17---------------------------------------------------------------

# calculator__________THIS IS MY WAY______________________

num1 = input("Enter the first number: ")

operation = int(input("1 - (+)\n2 - (-)\n3 - (*)\n4 - (\\)\nEnter the operation number: "))

num2 = input("Enter the second number: ")


def sum0(num1, num2):
    return int(num1) + int(num2)


def sub0(num1, num2):
    return int(num1) - int(num2)


def mul0(num1, num2):
    return int(num1) * int(num2)


def div0(num1, num2):
    return int(num1) / int(num2)


if 1 == operation:
    print(sum0(num1, num2))

elif 2 == operation:
   print(sub0(num1, num2))

elif 3 == operation:
    print(mul0(num1, num2))

elif 4 == operation:
    print(div0(num1, num2))


# V18-----------------------------------------------------------

# dictionaries
# all keys in the dictionary should be different and if there are duplicates keys the last one will be printed
convert_month = {
    # key     value
    "jan": "january",
    "feb": "febraury",
    "mar": "march",
    4: "april",
    5: True,
    "list": [1, 2, "hello"]

}

# getting values from the dictionary

# first way
print(convert_month["jan"])
print(convert_month[4])

# second way is recommended because we can creat a message if the given key is not exist in the dictionary
print(convert_month.get("list", "the value doesn't exist")[0])


# V19-----------------------------------------------------------
# while loop

i = 1
while i <= 10:
    print(i)
    if i == 6:
        continue  # used to skip the iteration if the condition is true

    i +=1
    if i == 9:
        break     # used to get out the loop if the if condition is true

else:   # will execute once when the while condition becomes false
    print("the condition is false")

# V20-----------------------------------------------------------
# for loop

buddies = ["faris", "amir", "ibrahim","winner"]

# will print list
for x in buddies:
    print(x)

# will print the characters of the string
for letter in "faris_hamdi":
    print(letter)

# will print numbers from 0 to 9
for number in range(10):
    print(number)

# will print numbers from 5 to 19
for y in range(5, 20):
    print(y)

# will print numbers from 0 to 3(length of the list)
for x in range(len(buddies)):
    print(x)

# will print the elements of the list using its index
for index in range(len(buddies)):
    print(buddies[index])

# to get string's index in a list
for buddy in range(len(buddies)):
    if buddies[buddy] == "winner":
        print(buddy, "is the winner")
    else:
        print(buddy, "is not the winner")


for buddy in buddies:
    if buddy == "amir":
        print(buddy, "is your brother")
        # break will break the loop when buddy becomes "amir"
        break
# else statement will execute when the for loop condition becomes false
else:
    print("not found")


for x in range(3, 10):
    if x == 5:
        # continue will skip the iteration when x becomes 5
        continue
    print(x, "is the chosen number")


# V21-----------------------------------------------------------

# 2^3
print(2**3)

# the power function


def power0(base_num, pow_num):
    result = 1
    for n in range(pow_num):
        result *= base_num

    return result


print(power0(2,3))


# V22-----------------------------------------------------------
# 2D lists

no_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# will print the whole list
print(no_list)

# will print [4, 5, 6]
print(no_list[1])

# will print 4
print(no_list[1][0])


# nested loops

for row in no_list:
    for column in row:
        # will print the 2d list elements
        print(column)

# V23-----------------------------------------------------------

# comments

'''

multi line comment

'''

# V24-----------------------------------------------------------
# Errors

try:
    result = 10 / 0
    value = int(input("Enter a number: "))
    print(value)
# if there is a division by zero, an error will appear but the program will not terminate
except ZeroDivisionError as err:
    print(err)
# if there is an invalid input, an error will appear but the program will not terminate
except ValueError as err1:
    print(err1)
# default error
except:
    print("default error")

print("Success, errors hasn't terminated the program")


# V25-----------------------------------------------------------
# Reading files
'''
"r"  > read
"r+" > read and write and cursor is in the beginning of the file

# the coming modes have the ability to creat the file if the file isn't exist 

"w"  > overwrite (delete the previous text and write new one)
"w+  > overwrite/read (delete the previous text and write/read new one)
"a"  > append (writing and the cursor is in the end of the file)
"a+" > read and write and cursor is in the beginning of the file



'''
# read mode

# workers.txt is a text file should be in the same folder as the project
workers_file = open("workers.txt", "r")

# readable() is a function returns True or False and  used to validate if the file is readable or not
print(workers_file.readable())

# read() is a function used to read the file in the read mode
print(workers_file.read())

# readline() used to read the file line by line and after reading the line it makes the cursor move to the next line
print(workers_file.readline())

# readlines() is used to read all the lines from a file and returns them as a list of strings.
# Each element of the list corresponds to a line from the file.
print(workers_file.readlines())

# fetching the elements of the list
for worker in workers_file.readlines():
    print(worker)

# close() is a function used to close the file
workers_file.close()

# V26-----------------------------------------------------------
# writing files
# the function will creat the file if the file isn't exist
# a, a+, w and w+ modes work with the same way

workers_file = open("workers", "w")

# write() is a function used to write the file in the write mode
workers_file.write("\nhunter x hunter")

list_of_phrases = ["\nthis is a first line","\nthis is a second line","\nthis is a third line"]
# writelines() is a function used to write bunch of lines like the lists in the file
workers_file.writelines(list_of_phrases)

workers_file.close()


# V27-----------------------------------------------------------
# modules : using python files in another project

from venv import test0

# roll_dice() is a function in the test0 module
print(test0.roll_dice(9))

# search for more python 3 modules

# python 3 has built-in modules like base64 and docx
# docx module used to write/read M.S word file but it needs to install first
import docx

print(docx.fun1)

# V28-----------------------------------------------------------
# class : creating new data types
#  first letter of the class name should be capital
class Employee:
    # initialize function : the class variables(specifications)
    #                 the parameters of the function
    def __init__(self, name0, age0, department0, is_manager0,rating0):
        self.name0 = name0
        self.age0 = age0
        self.department0 = department0
        self.is_manager0 = is_manager0
        self.rating0 = rating0

# should import the file which the class is exist(if there are not in the same file)
# the class's file   the class name
from Employee_file import Employee

# creating objects ( should be outside the scope of the class and the function)
employee1 = Employee("faris", 20,"Google", True)
employee2 = Employee("amir", 16,"Open AI", False)

# calling the objects ( should be outside the scope of the class and the function)
print(employee1.age0, employee2.name0, employee1.department0)


# V29-----------------------------------------------------------

class Student:
    def __init__(self, name0, age0, department0, rating0):
        self.name0 = name0
        self.age0 = age0
        self.department0 = department0
        self.rating0 = rating0

    # class function ( should be in the class's scope)
    def is_excellent(self):
        if self.rating0 >=15:
            return True
        else:
            return False

student1 = Student("faris", 20, True, 19)
student2 = Student("amir", 16, False, 5)

# using class function
print(student1.is_excellent())
print(student2.is_excellent())


# V30-----------------------------------------------------------
# class inheritance
class Doctor:
    def studied_years(self):
        print("i studied 7 years")

    def work_where(self):
        print("i work in a hospital")

    def paid_by_who(self):
        print("i get paid by the goverment")


# making object
doctor1 = Doctor()

doctor1.studied_years()
doctor1.work_where()
doctor1.paid_by_who()

# class inheritance
class FamilyDoctor(Doctor)
    def what_specialization(self):
        print("i work with families")
    def paid_by_who(self):
        print("i get paid by the people ")

#calling the class
doctor2 = FamilyDoctor()
doctor2.work_where()
doctor2.paid_by_who()
# _______________________________THE END__________________________________________
