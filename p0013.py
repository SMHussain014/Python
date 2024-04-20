"""
In python, a function is a block of statements which we have to define. 
Only defining a function will do nothing but we have to call it to perform designated tasks.
We may pass the same arguments, while we call a function, which we defined at the time of creation of a function.
A function may or may not have return value.
"""
# How to define a function; def function_name()
def display():
    print("Hello World!")
# How to call a function; function_name()
display()
# a function may be defined with a single or multiple arguments without specifying any data type 
def show(name):
    print("Hello!", name)
show("Hussain")
show(10)
def num(a, b):
    print("a=", a)
    print("b=", b)
num(10, 20)
num("Ali", "Fatima")
# function without return value
def sum(a, b, c):
    s = a + b + c
    print("Sum is equal to", s)
x, y, z = 10, 20, 30
sum(x, y, z)
# function with return value
def sum(a, b, c):
    s = a + b + c
    return s
x, y, z = 5, 10, 15
s = sum(x, y, z)
print("The sum is", s)
# a program for even number determination
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
x = int(input("Please enter any integer:" ))
flag = is_even(x)
if (flag):
    print("This is an even number.")
else:
    print("This is an odd number.")