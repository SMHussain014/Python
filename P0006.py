print("Welcome to Nested if Condition")
x = int(input("Please enter any Number and press ENTER: "))
y = int(input("Please enter any Number and press ENTER: "))
if x != y:
    print(f"{x} is not equal to {y}.")
    if x <= y:
        print(f"{x} is less than or equal to {y}.")
        if x < y:
            print(f"{x} is less than {y}.")
    if x >= y:
        print(f"{x} is greater than or equal to {y}.")
        if x > y:
            print(f"{x} is greater than {y}.")
else:
    print(f"{x} is equal to {y}")
print("Program successfully ended.")
print("*" *7)
print("Welcome to if elif else Conditional Statement")
z = int(input("Please enter Marks Obtained: "))
if z>90:
    print("Congratulation! Your Grade is \"A+\".")
elif z>80:
    print("Congratulation! Your Grade is \"A\".")
elif z>70:
    print("Excellent! Your Grade is \"B+\".")
elif z>60:
    print("Very Good! Your Grade is \"B\".")
elif z>50:
    print("Good! Your Grade is \"C\".")
elif z>40:
    print("Oh! Your Grade is \"D\".")
else:
    print("Sorry! You are \"Fail\", Good luck for next time.")
print("Program successfully ended.")
print("Design a program that tell whether a number is prime or not.")
number = int(input("Please enter any number and press ENTER: "))
if number == 0 or number < 2:
    print(f"The entered number, i.e. {number}, is either not defined or a universal divisor.")
elif number % 2 != 0 or number == 2:
    if number % 3 != 0 or number == 3:
        if number % 5 != 0 or number == 5:
            if number % 7 != 0 or number == 7:
                if number % 11 != 0 or number == 11:
                    if number % 13 != 0 or number == 13:
                        if number % 17 != 0 or number == 17:
                            if number % 19 != 0 or number == 19:
                                if number % 23 != 0 or number == 23:
                                    if number % 29 != 0 or number == 29:
                                        if number % 31 != 0 or number == 31:
                                            if number % 37 != 0 or number == 37:
                                                if number % 41 != 0 or number == 41:
                                                    if number % 43 != 0 or number == 43:
                                                        if number % 47 != 0 or number == 47:
                                                            if number % 53 != 0 or number == 53:
                                                                if number % 229 != 0 or number == 229:
                                                                    print(f"The entered number, i.e. {number} is a prime number.")
                                                                else:
                                                                    print(f"The entered number, i.e. {number} is a not prime number.")
                                                            else:
                                                                print(f"The entered number, i.e. {number} is a not prime number.")
                                                        else:
                                                            print(f"The entered number, i.e. {number} is a not prime number.")
                                                    else:
                                                        print(f"The entered number, i.e. {number} is a not prime number.")
                                                else:
                                                    print(f"The entered number, i.e. {number} is a not prime number.")
                                            else:
                                                print(f"The entered number, i.e. {number} is a not prime number.")
                                        else:
                                            print(f"The entered number, i.e. {number} is a not prime number.")
                                    else:
                                        print(f"The entered number, i.e. {number} is a not prime number.")
                                else:
                                    print(f"The entered number, i.e. {number} is a not prime number.")
                            else:
                                print(f"The entered number, i.e. {number} is a not prime number.")  
                        else:
                            print(f"The entered number, i.e. {number} is a not prime number.")  
                    else:
                        print(f"The entered number, i.e. {number} is a not prime number.")  
                else:
                    print(f"The entered number, i.e. {number} is a not prime number.")  
            else:
                print(f"The entered number, i.e. {number} is a not prime number.")
        else:
            print(f"The entered number, i.e. {number} is a not prime number.")
    else:
        print(f"The entered number, i.e. {number} is a not prime number.")
else:
    print(f"The entered number, i.e. {number} is a not prime number.")
print("Program successfully ended.")