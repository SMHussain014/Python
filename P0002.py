print("Hello,\nWorld!")
# \n is Escape Sequence and create new line
# print() create a new line automatically after the end of command
print("\tHello, World!")
# \t is Escape Sequence and provide tab length before or after the text
print("Hello to the \"World of Python\"!")
# \ is Escape Sequence and it converts any Special Character into a simple string/character
# Here Special Character, i.e. double quote("), has been converted to simple string
print("Python", end = "-")
print("Course")
# end is a positional parameter to eliminate new line
print("Hi", "Hussain", sep = "! ")
# sep is a positional parameter to separate two or more text pieces
x: str = "Teacher said, "
y: str = "Welcome! "
z: str = 'to "Python" class.'
""" another way to create double quotes around the desired text is to use single quote to 
declare a str """
print(x + y + z)
"""
Variables, in general, are of two types w.r.t their values, i.e. Permanent and Temporary
When a programmer assign a value to a variable, it is permanent in its nature
when a user input a value to a variable, it is temporary in its nature
a str or its variable can only be added to another str or its variable
"""
first_name: str = input("Please enter your first name and press ENTER: ").title().strip()
middle_name: str = input("Please enter your middle name and press ENTER: ").title().strip()
last_name: str = input("Please enter your last name and press ENTER: ").title().strip()
name: str = first_name + " " + middle_name + " " + last_name
"""
There is no need to mention data type here as default data type is str,
input() takes input from the user, 
title() capitalize the title, and 
strip() waives off extra spaces, if any
All three variables are added in a single variable with space, present between double quotes
Unlike coma, Additive operator does not create space automatically
"""
age: int = int(input("Please enter your age and press ENTER: "))
# Before input(), we have to introduce int() so to get correct integral entry
country_name: str = input("Please enter the name of your country and press ENTER: ").title().strip()
comments: str = input("Please enter your comments and Press Enter: ").capitalize().strip()
# capitalize() capitalize the first letter of a phrase
print(f"Hello, {name},")
# Use of format command, in case, variable is used within a str
print("Your age is " + str(age) + " years.", end = " ")
# We have to change data type "int" into data type str 
# (the process of changing data type is called casting)
print("You live in", country_name + ".")
# using comma, extra space is not required. Coma and Additive Operator can be used at the same time
print(comments)
print("Thanks for your feedback.")
print(type(name))
print(type(age))
print(type(str(age)))
# type() tells the type of data used
general: str = "End of Program"
print(general.lower())
# lower() convert the text to lower case
print(general.upper())
# upper() converts the text to upper case
print("End of Program")
print("*" * 7)
# str can be multiplied to create sequences