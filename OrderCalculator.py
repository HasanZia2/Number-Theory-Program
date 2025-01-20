# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 00:01:22 2025

@author: hzia2
"""

def EuclideanAlgorithm(initial_number1, initial_number2):
    # This function reworks the Euclidean Algorithm program. It uses the same
    # code without the print statements, and returns a list of values which may
    # be used by other functions.
    
    number1 = initial_number1
    number2 = initial_number2
    remainder = number1%number2
    step = -1
    quotients = []
    number1s = []

    while remainder >= 0:
        quotient = number1//number2
        if abs(number1) >= abs(number2):
            number1s.append(number1)
            quotients.append(quotient)
            step += 1
        remainder = number1%number2
        try:
            number2%remainder
            if number2%remainder == 0 and step != -1:
                break
            else:
                number1 = number2
                number2 = remainder
        except ZeroDivisionError:
            if not initial_number1%initial_number2 == 0 or not initial_number2%initial_number1 == 0 or initial_number1 == initial_number2:
                if initial_number1 > initial_number2:
                    remainder = initial_number2
                else:
                    remainder = initial_number1    
            break
    
    final_number2 = number2
    
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
        elif (step_after_gcd - step)%2 == 0: 
            if step_after_gcd - step != 0:
                number1 = number1s[step]
            coefficient2 -= abs(coefficient1)*quotients[step]
    
    if abs(initial_number1) >= abs(initial_number2):
        continued_fraction = quotients
    else:
        continued_fraction = [0] + quotients
    if initial_number1 != initial_number2:
        continued_fraction.append(int(final_number2/remainder))
    continued_fraction = str(continued_fraction).replace(",", ";", 1)
    
    return [remainder, coefficient1, number1, coefficient2, number2, continued_fraction]

def OrderCalculator():
    # This function finds the order of an element a by repeatedly multiplying
    # said element by itself until the lowest positive value of n such that
    # a^n = [1] is found.
    
    order = 0
    print("This program finds the order of an element in the group (Z/nZ)*. ")
    print(" ")
    n = int(input("Enter the value of the positive integer n. "))
    while n <= 0:
        n = int(input("Your input for n was not a positive integer. Please try again. "))
    element = int(input("An element of (Z/" + str(n) + "Z)* is of the form [m], where m is an integer. Input the value of m. "))
    print(" ")
    element_order = element
    
    if element >= 0:
        gcd = EuclideanAlgorithm(n, element)[0]
    else:
        gcd = EuclideanAlgorithm(n, -element)[0]
    
    if gcd == 1:
        while element_order != 1:
            if order >= 1:
                element_order *= element
            element_order = element_order%n
            order += 1   
            
        print("The order of the element [" + str(element) + "] in (Z/" + str(n) + "Z)* is " + str(order) + ". ")
    
    else:
        print("Your chosen n and m are not coprime, so m has no defined order in Z/" + str(n) + "Z)*. ")

def main():
    OrderCalculator()
    
if __name__ == '__main__':
    main()