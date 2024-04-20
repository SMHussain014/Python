"""
Loop (for) is used to iterate over a sequence.
Syntax of for loop
for variable in iterable:
    statements
Within a for loop, if or else condition may also be used.
We may use "pass", in case, for the time being, we have no body of a block.
"""
"""
Bitwise Operators
These are used to deal with binary numbers, i.e. ones (1) and zeros (0)
'bit' is the smallest unit of memory storage and 8 bits equal 1 bye and so on ...
consider two variables x and y having value 53 and 23 respectively
Allocation (Representation) in binary system of variable 'x' is as under
-128   64  32  16  8   4   2   1
   0    0   1   1  0   1   0   1
Allocation (Representation) in binary system of variable 'y' is as under
-128   64  32  16  8   4   2   1
   0    0   0   1  0   1   1   1
The following are Bitwise operators, like
Bitwise AND (&); set each bit to 1 if both bits are 1; syntax (x & y)
Bitwise OR (|); set each bit to 1 if one of two bits is 1; syntax (x | y)
Bitwise NOT (~); reverse all the bits (0 to 1 and 1 to 0); syntax (x ~ y)
Bitwise XOR (^); set each bit to 1 if only one of two bits is 1; syntax (x ^ y)
Bitwise left shift (<<); shift left by pushing zeros in from the right 
and let the leftmost bit fall off; syntax (x << y)
Bitwise right shift (>>); shift right by pushing copies of the leftmost bit in from the left 
and let the rightmost bit fall off; syntax (x >> y)
Allocation (Representation) in binary system of x & y (i.e. 21) is as under
-128   64  32  16  8   4   2   1
   0    0   0   1  0   1   0   1
print("Write a program for Bitwise AND Operator")
"""
x = 53
y = 23
print(x & y)
print("ENd of Bitwise Operators")
print("Write a program looping through a String")
sample = "Python"
for x in sample:
    print(x)
print("Second Loop")
for x in sample:
    if x not in "aeiou":
        print(x)
print("End of String")
"""
'range()' is a built in function that is used when a user needs to perform an action onto specific times.
Syntax of range() is; 
range(start, end, steps)
It always start from zero unless specified otherwise. 
if range is specified, last number in range() will not be printed
if steps are specified in range(), only that stages will be printed
"""
print("Write a program looping through range()")
for x in range(5):
    print(x)
print("Range-1 ends here")
for y in range(1, 6):
    print(y)
print("Range-2 ends here")
for z in range(1, 11, 3):
    print(z)
print("Range-3 ends here")
print("Write a program to develop a sequence")
for i in range(1, 6):
    for j in range(1, i):
        print(j, end = " ")
    print(i)
print("Write a program of for loop using continue and break statements")
display = "Hello World"
for letter in display:
    if letter in 'aeiou':
        continue
    print(display)
print("Continue statement ends here")
for letter in display:
    if letter in " ":
        break
    print(display)
print("Break statement ends here")
"""
Continue statement when reaches to the specified condition, the loop will start again
Break statement when reaches to the specified condition, the loop will be terminated
"""
print("Write a program of for loop using continue and break statements")
display = "Hello World"
for letter in display:
    if letter == 'aeiou':
        continue
    print(display)
print("Continue statement ends here")
for letter in display:
    if letter == " ":
        break
    print(display)
print("Break statement ends here")