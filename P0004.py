print("Let us see, how int or float work in Python.")
print("There are three cases:")
print("(i) when the values are same and fixed, e.g. when x and y are 10, and use of Identity Operator;")
x1 = y1 = 10
z1 = x1 + y1
print(f"Sum of {x1} and {y1} is {z1}.")
print(x1 is y1)
""" 
"is" and "is not" operators also called Identity Operator
They are used to check whether both values are located in the same part of memory or not
They return True, if the values of two variables occupy the same memory location
""" 
print("(ii) When the values are different but fixed, e.g. when x and y are 10 & 20, and use of Identity Operator; and")
x2, y2 = 10, 20
z2 = x2 + y2
print(f"Sum of {x2} and {y2} is {z2}.")
print(x2 is not y2)
# use of Identity Operator
print("(iii) when the values are given by the User and use of Identity Operator.")
x3 = int(input("Please enter the value of x: "))
y3 = int(input("Please enter the value of y: "))
z3 = x3 + y3
print (f"Sum of {x3} and {y3} is {z3}.")
print(x3 is y3)
# use of Identity Operator
print("End of First Program.")
print("Welcome to the World of Mathematics!")
x = int(input("Please enter any Number: "))
y = int(input("Please enter any Number: "))
"""
To deal with Mathematics, we have following Arithmetic Operators
Addition (+), Subtraction (-), Multiplication (*), Division (/), 
Floor Division  (//). It gives answers in integers,
Modulus (%). It gives remainder of division, and
Exponential (**). It gives square/cube roots etc.
The operators are always performed on 'operand' of Number type.
"""
z1 = x + y
# Additive Operator
z2 = x - y
# Subtractive Operator
z3 = x * y
# Multiplicative Operator
z4 = round(x / y, 2)
# Division Operator
# round() round off the decimal upto specified limit
# In print(), round command can be used as print(number:.2f)
z5 = x // y
# Floor Division Operator
z6 = x % y
# Modulus Operator
z7 = x ** y
# Exponential Operator
# pow = (x, y)
print(f"Sum of {x} and {y} is {z1:,}.")
# :, will divide figure into triplets
print(f"Subtraction of {x} and {y} is {z2:,}.")
print(f"Multiplication of {x} and {y} is {z3:,}.")
print(f"Division of {x} and {y} is {z4:,}.")
print(f"Floor Division of {x} and {y} is {z5:,}.")
print(f"Remainder of {x} and {y} is {z6:,}.")
print(f"Power of {x} to {y} is {z7:,}.")
print("End of Second Program")