# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:17:50 2024

@author: hzia2
"""

# This section records the numbers inputted by the user and initialises
# different objects.

print("This program performs the Euclidean algorithm on two positive integers. ")
print(" ")
initial_number1 = int(input("Enter the first positive integer you wish to apply the Euclidean algorithm on. "))
while initial_number1 <= 0:
    initial_number1 = int(input("Your first input was not a positive integer. Please try again. "))
initial_number2 = int(input("Enter the second positive integer. "))
while initial_number2 <= 0:
    initial_number2 = int(input("Your second input was not a positive integer. Please try again. "))
number1 = initial_number1
number2 = initial_number2
remainder = number1%number2
step = -1
quotients = []
number1s = []

print(" ")

# This section finds the greatest common factor of the two numbers
# entered. It also records the different quotient and number1 values
# per loop into lists for future use.
while remainder >= 0:
    quotient = number1//number2
    if number1 >= number2:
        number1s.append(number1)
        quotients.append(quotient)
        step += 1
    remainder = number1%number2
    print("  " + str(number1) + " = (" + str(quotient) + ")(" + str(number2) + ") + " + str(remainder))
    try:
        number2%remainder
        if number2%remainder == 0 and step != -1:
            print(" ")
            print("∴gcd(" + str(initial_number1) + ", " + str(initial_number2) + ") = " + str(remainder) + ". Moreover,")
            print(" ")
            break
        else:
            number1 = number2
            number2 = remainder
    except ZeroDivisionError:
        print(" ")
        if initial_number1 <= initial_number2:
            print("∴gcd(" + str(initial_number1) + ", " + str(initial_number2) + ") = " + str(initial_number1) + ". Moreover,")
        else:
            print("∴gcd(" + str(initial_number1) + ", " + str(initial_number2) + ") = " + str(initial_number2) + ". Moreover,")
        if not initial_number1%initial_number2 == 0 or not initial_number2%initial_number1 == 0 or initial_number1 == initial_number2:
            if initial_number1 > initial_number2:
                remainder = initial_number2
            else:
                remainder = initial_number1    
        print(" ")
        break    

# This section takes the recorded quotients and number1s and uses them
# to express the greatest common factor of the two integers entered as
# a linear combination of the two integers.
step_after_gcd = step
steps = range(step, -1, -1)
coefficient1 = 1
if step == 0 and initial_number1%initial_number2 == 0 or initial_number2%initial_number1 == 0:
    coefficient2 = 1
else:
    coefficient2 = 0
for step in steps:
    if (step_after_gcd - step)%2 != 0:
        coefficient1 += abs(coefficient2)*quotients[step]
        number2 = number1s[step]
        print("  " + str(remainder) + " = (" + str(coefficient1) + ")(" + str(number1) + ") + (" + str(coefficient2) + ")(" + str(number2) + ")")
    elif (step_after_gcd - step)%2 == 0: 
        if step_after_gcd - step != 0:
            number1 = number1s[step]
        coefficient2 -= abs(coefficient1)*quotients[step]
        print("  " + str(remainder) + " = (" + str(coefficient1) + ")(" + str(number1) + ") + (" + str(coefficient2) + ")(" + str(number2) + ")")