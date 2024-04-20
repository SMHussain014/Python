"""
Syntax of if-else Condition
if condition:
    if condition is true, command will be executed
else:
    if condition is false, command will not be executed
Comparison Operators
These are widely used in Mathematics, like
Equal to (==), Not Equal to (!=), Less than (<), Greater than (>),
Less than or Equal to (<=) and Greater than or Equal to (>=)
"""
x = int(input("Please enter first number: "))
y = int(input("Please enter second number: "))
if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")
    if x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{x} is greater than {y}")
    if x <= y:
        print(f"{x} is less than or equal to {y}")
    else:
        print(f"{x} is greater than or equal to {y}")
print("End of the first Program")
print("Design a Program to tell given number is even or odd.")
number = int(input("Please enter any integral number and press ENTER: "))
if number % 2 == 0: 
    print(f"{number} is an Even Number.")
else:
    print(f"{number} is an Odd Number.")
print("End of the second Program")
"""
Short Hand if statement
if x < 10: print("x is less than 10")
Short Hand if-else statement
print("x is less than 10") if x < 10 else print("x is not less than 10")
Note: -
In case, we don't want to use if condition's body, simply write "pass"
so that else conditions's body may execute.
Logical Operators
AND (and), OR (or), NOT(not) operators are used to combine two conditional statements
AND operator turns True, if both the conditions are true
OR operator turns True, if any one of the condition true
NOT operator reverse the result, i.e returns False, if the result is true
"""
print("This Program show the use of Short-hand Command and Logical Operators.")
z = int(input("Please enter any number and press ENTER: "))
if z < 10: print(f"The desired number, i.e. {z}, is less than 10.")
print(f"Number {z} is less than 10.") if z < 10 else print(f"Number {z} is greater than 10.")
print("End of the third Program")
a = int(input("Please enter first number and press ENTER: "))
b = int(input("Please enter second number and Press ENTER: "))
if a != b and a < b:
    print(f"Number {a} is less than Number {b}.")
    print("The program is in the body of if condition.")
else:
    print(f"Number {a} is greater than Number {b}.")
    print("The program is in the body of else condition.")
    print("End of the fourth Program")