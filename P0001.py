# This is the first program, say hello!
name: str = "Hello World"
print(name)
print(type(name))
print(id(name))
print(dir(name))
# Explanation 1:
""" 
In every programming language, "Comments" are made to remember the purpose of coding.
They enhance the readability of a program. The compilers don't print them at all.
In fact, they are note(s) for other programmers to understand a program properly.
sometimes, also called pseudo-code and are of two types;
(i) single line comment, starts with # sign.
(ii) Multiple lines comments, are written between thrice double quotes.
"""
# Explanation 2:
""" 
print() is a command and displays output on screen, wherein;
() represents function, like verbs, designated to perform a task
"Hello World" is merely text to be displayed on screen
"""
# Explanation 3:
"""
Concept of Indentation
Code(s) should be written without providing any space before a command,
In case of indent, the program will not run at executing time.
However, in block structure like if, while, for blocks, some indent is provided.
In block structure, end of indent means end of that block.
"""
x: int = 10
y: int = 20
z: int = x + y
print(x)
print(y)
print("Sum of x and y is", z)
"""
# Explanation 4:
x, y, and z are variables, i.e. memory spaces, in which data is stored
In python, there are seven (07) types of data, i.e. number (int, float, complex), str, bool, 
list, tuple, set & dict;
str; string that is the text written between single/double quotes
int; integers that represent numbers
float; float that are decimal numbers
complex; complex that is combination of real and imaginary numbers, e,g, 5 + 6j
bool; boolean that is condition, e.g. True or False, it's always True 
'Zero', 'None' & 'Empty Space'
"""
# Explanation 5:
"""
Rules for Writing/Declaring Variable's Name/Title
Python is a case sensitive language. 
Use of "Special Characters" and "Spaces" are not allowed.
Variable can only be written in (a-z), (A-Z), (0-9), and (_). 
However, no variable can have a number (0-9) in the start of its name. 
There are 3 techniques to declare a variable in Python;
(i) Camel Case, i.e. myVariableName
(ii) Pascal Case, i.e. MyVariableName; and
(iii) Snake Case, i.e. my_variable_name
"""
# Explanation 6:
"""
'=' is Assignment Operator that associates a variable to its value 
'+' is Arithmetic Operator to perform addition 
print() is capable to display str and variable at the same time, separated by coma (see line 35)
Syntax is print(str, variable)
No space is required as coma creates a single space between str and variable itself
"""