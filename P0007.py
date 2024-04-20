"""
There are two types of loops in Python (i) while loop; and (ii) for loop
Loop (while) is used to repeat a task as desired.
Syntax of while loop
while expression:
    statement 1
    statement 2
Within a while loop, if or else condition may also be used.
We may use "pass", in case, for the time being, we have no body of a block.
Assignment Operators
These are used to assign values to the desired variable, like
Value Assignment (x = 10), x += y (x = x + y), x -= y (x = x - y), x *= y (x = x * y),
x /= y (x = x / y), x //= y (x = x // y), x %= y (x = x % y), x **= y (x = x ** y), 
x &= y (x = x & y), x |= y (x = x | y), x ^= y (x = x ^ y)
"""
i = 1
print("Before while loop")
while i <= 5:
    print(i)
    i = i + 1
print("After while loop")
print(i)
print("*" * 7)
i = 1
print("The while loop with if condition")
while i <= 10:
    if i % 2 == 0:
        print(i)
    i = i + 1
print("End of while loop")
print("*" * 7)
i = 1
print("The while loop with else condition")
while i <= 5:
    print(i)
    i = i + 1
else:
    print("End of while loop")
print("*" * 7)
print("Design a program reading data from str.")
sample = "Python Program"
length = len(sample)
print(length)
i = 0
while i <= 5:
    print(sample[i])
    i = i + 1
print("Start of second while loop")
j = 0
while j <= 13:
    if sample[j] != "a" and sample[j] != "e" and sample[j] != "i" and sample[j] != "o" and sample[j] != "u":
# if sample[k] not in "aeiou": can also be used
        print (sample[j])
    j = j + 1
print("*" * 7)
print("Design a program to perform addition from 1 to 10")
n = 1
sum = 0
while n <= 10:
    sum = sum + n
    n = n + 1
    print("Sum of 1 to 10 is:", sum)
print("Design a program to perform addition by a user")
number = " "
sum = 0
while True:
    number = input("Please enter the number designated to be added: ")
    print('Type "exit" and press ENTER to exit.')
    if number != "exit":
        sum = sum + int(number)
    print("Your answer is:", sum)
# Nested while loop
print("A program to show a Sequence")
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(j, end = " ")
        j = j + 1
    print(i)
    i = i + 1
print("End of Program, Come again.")
print("The while loop with continue option")
k = 1
while k <= 5:
    if k == 3:
        k = k + 1
        continue
    print(k)
    k = k + 1
print("End of while loop with continue option")
print("The while loop with break option")
k = 1
while k <= 5:
    if k == 3:
        k = k + 1
        break
    print(k)
    k = k + 1
print("End of while loop with break option")