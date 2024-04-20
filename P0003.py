print("This program will show multi-lines str.")
multi_lines_str: str = """ Hi!, I am Python.
I am here to help you
in multiple ways.
Thank you for your trust in me.
Good Luck!"""
print(multi_lines_str)
# str can be written in multiple lines by using single or double quotations
print("A str can act as an Array, see how?")
text: str = "Python Program"
print(len(text))
print(text[0])
print(text[5])
print(text[13])
print(text[-4])
""" str can work as an Array, starting from zero.
It can provide indexing to us.
len() tells about total numbers of characters in a str
"""
print('This program show the working of "Membership Operators".')
print("gra" in text)
print("n P" not in text)
""" "in" and "not in" called Membership Operators 
they tell whether something is found or not found in a desired expression
they return True, if a sequence with specified value is present in a desired expression or object
"""
print("This program will perform slicing of a str.")
print(text[8:])
print(text[:8])
print(text[5:11])
"""
Slicing, i.e. taking a part of whole str, or making sub-str
But last character is not included in slicing
print(str_name[n:]) prints till end
print(str_name[:n] prints from beginning
print(str_name[n0:nn] prints range but end not included
"""
print("Use of different types of data without casting.")
statement: str = "I want {} kg {} for {} dollars."
items: str = "apples"; quantity: int = 5; price: float = 30.50
print(statement.format(quantity, items, price))
# This command is called str format
print("The aim of this program is to divide full name into parts.")
full_name = input("Please enter your full name: ").strip().title()
first, middle, last = full_name.split(" ")
print(f"Hello!, {last}")
print(f"Hello!, {middle} {last}")
print("A Simple Sequence")
print("*")
print("**")
print("***")
print("**")
print("*")
x = "Its me"
print(x)
del x
# print(x) will show error as variable x no longer exists.
# del will permanently delete a variable and will not be used in future.