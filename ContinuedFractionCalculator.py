# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:11:53 2025

@author: hzia2
"""

import math

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

def pAlgorithm(continued_fraction, index):
    # This function performs the p calculation for the (p, q)-algorithm.
    
    if index == 0:
        p = continued_fraction[0]
    elif index == 1:
        p = continued_fraction[0]*continued_fraction[1] + 1
    else:
        return continued_fraction[index]*pAlgorithm(continued_fraction, index - 1) + pAlgorithm(continued_fraction, index - 2)
    return p

def qAlgorithm(continued_fraction, index):
    # This function performs the q calculation for the (p, q)-algorithm.
    
    if index == 0:
        q = 1
    elif index == 1:
        q = continued_fraction[1]
    else:
        return continued_fraction[index]*qAlgorithm(continued_fraction, index - 1) + qAlgorithm(continued_fraction, index - 2)
    return q

def pqAlgorithm(continued_fraction):
    # This function calls the pAlgorithm and qAlgorithm functions to perform
    # an explicit computation of a continued fraction.
    
    continued_fraction = ("".join(c for c in continued_fraction if c != "(" and c != "[" and c != ";" and c != "," and c != "]" and c != ")")).split()
    for number in continued_fraction:
        continued_fraction[continued_fraction.index(number)] = int(number)
    
    return str(pAlgorithm(continued_fraction, len(continued_fraction) - 1)) + "/" + str(qAlgorithm(continued_fraction, len(continued_fraction) - 1))

def InfiniteContinuedFraction(irrational, max_count):
    # This function finds the infinite canonical continued-fraction representation
    # of an irrational number. The amount of integers displayed in the
    # representation is decided by the user.
    
    continued_fraction = []
    current_count = 0

    def ICFAlgorithm(irrational, count):
        # This function recursively determines the value of one integer
        # in the canonical continued-fraction representation of an irrational
        # number at some specified position.
        
        if count == 0:
            integer = int(irrational)
        else:
            return [1/(ICFAlgorithm(irrational, count - 1)[0] - ICFAlgorithm(irrational, count - 1)[1]), int(1/(ICFAlgorithm(irrational, count - 1)[0] - ICFAlgorithm(irrational, count - 1)[1]))]
        return [irrational, integer]

    while current_count <= max_count:
        continued_fraction.append(ICFAlgorithm(irrational, current_count)[1])
        current_count += 1
    
    continued_fraction = str(continued_fraction).replace(",", ";", 1)
    continued_fraction = continued_fraction.replace("]", ", ...]")
    
    return continued_fraction

def RepeatedContinuedFraction(constant, repeated):
    # This function finds the exact quadratic irrational form of a 
    # periodic continued fraction.
    
    constant = ("".join(c for c in constant if c != "(" and c != "[" and c != ";" and c != "," and c != "]" and c != ")")).split()
    for number in constant:
        constant[constant.index(number)] = int(number)
    repeated = ("".join(c for c in repeated if c != "(" and c != "[" and c != ";" and c != "," and c != "]" and c != ")")).split()
    for number in repeated:
        repeated[repeated.index(number)] = int(number)
    
    
    def QuadraticCalculation(continued_fraction):
        # This function deals with the quadratic equation whose roots need to
        # be solved for corresponding to the repeated part of a periodic
        # continued fraction in the process of finding the quadratic irrational
        # form of the continued fraction.
        
        period_length = len(continued_fraction)
        p_index_minus_1 = pAlgorithm(continued_fraction, period_length - 1)
        p_index_minus_2 = pAlgorithm(continued_fraction, period_length - 2)
        q_index_minus_1 = qAlgorithm(continued_fraction, period_length - 1)
        q_index_minus_2 = qAlgorithm(continued_fraction, period_length - 2)
        
        denominator = 2*q_index_minus_1
        integer_part = p_index_minus_1 - q_index_minus_2
        discriminant = integer_part**2 + 4*p_index_minus_2*q_index_minus_1
        
        continued_fraction_value_decimal = (1/denominator)*(integer_part + math.sqrt(discriminant))
        continued_fraction_value_exact = "(1/" + str(denominator) + ")(" + str(integer_part) + " + sqrt(" + str(discriminant) + "))"
               
        return [continued_fraction_value_decimal, continued_fraction_value_exact, p_index_minus_1, p_index_minus_2, q_index_minus_1, q_index_minus_2, denominator, integer_part, discriminant]
    
    if constant == []:
        return [str(QuadraticCalculation(repeated)[0]), QuadraticCalculation(repeated)[1]]
    else:
        repeated_value = QuadraticCalculation(repeated)[0]
        full_value_decimal = (QuadraticCalculation(constant)[2]*repeated_value + QuadraticCalculation(constant)[3])/(QuadraticCalculation(constant)[4]*repeated_value + QuadraticCalculation(constant)[5])
        
        a = QuadraticCalculation(constant)[2]
        b = QuadraticCalculation(constant)[3]
        c = QuadraticCalculation(constant)[4]
        d = QuadraticCalculation(constant)[5]
        f = QuadraticCalculation(repeated)[6]
        g = QuadraticCalculation(repeated)[7]
        h = QuadraticCalculation(repeated)[8]
        
        new_denominator = (c*g + d*f)**2 - (c**2)*h
        new_integer_part = (a*g + b*f)*(c*g + d*f) - a*c*h
        discriminant_coefficient = a*(c*g + d*f) - c*(a*g + b*f)
        new_discriminant = h
        
        if new_denominator > 0:
            full_value_exact = "(1/" + str(new_denominator) + ")(" + str(new_integer_part) + " + (" + str(discriminant_coefficient) + ")sqrt(" + str(new_discriminant) + "))"
        else:
            full_value_exact = "(-1/" + str(abs(new_denominator)) + ")(" + str(new_integer_part) + " + (" + str(discriminant_coefficient) + ")sqrt(" + str(new_discriminant) + "))"
        
        return [str(full_value_decimal), full_value_exact]

def ContinuedFractionCalculator():
    # This function compiles all of the other functions in this program to
    # create a general continued fraction calculator.
    
    print("This program computes calculations involving finite and infinite continued fractions. Select from the following: ")
    print(" ")
    print("1: Canonical continued-fraction representation of fraction ")
    print("2: Explicit computation of finite continued fraction ")
    print("3: Infinite continued-fraction representation of irrational number ")
    print("4: Explicit computation of periodic continued fraction ")
    print(" ")
    selection = int(input("Enter the integer associated with the calculation you would like to perform. "))
    while selection != 1 and selection != 2 and selection != 3 and selection != 4:
        selection = int(input("You did not pick one of the four options. Please try again. "))
        
    if selection == 1:
        print(" ")
        print("You have selected the calculation of the canonical continued-fraction representation of a fraction. This will find the canonical continued-fraction representation of a fraction of the form a/b, where a is an integer and b is a positive integer. ")
        print(" ")
        a = int(input("Enter the value of the integer a. "))
        b = int(input("Enter the value of the positive integer b. "))
        while b <= 0:
            b = int(input("Your input for b was not a positive integer. Please try again. "))
        print(" ")
        print("The canonical continued-fraction representation of " + str(a) + "/" + str(b) + " is " + EuclideanAlgorithm(a, b)[5] + ". ")
    
    elif selection == 2:
        print(" ")
        print("You have selected the explicit computation of a finite continued fraction. A finite continued fraction takes the form [a_0; a_1, ..., a_n], and should be entered as such. ")
        print(" ")
        continued_fraction = input("Enter your continued fraction. ")
        print(" ")
        print("The explicit computation of the continued fraction " + continued_fraction + " is " + pqAlgorithm(continued_fraction) + ". ")
    
    elif selection == 3:
        print(" ")
        print("You have selected the calculation of the infinite continued-fraction representation of an irrational number. Note that this continued fraction will be infinite, so you must select the number of integers of the continued fraction you want displayed. ")
        print(" ")
        irrational = eval(input("Enter your irrational number. When entering this number, call it using the Python math library. "))
        max_count = int(input("Enter the desired amount of displayed integers in the infinite continued fraction. ")) - 1
        print(" ")
        print("The infinite continued-fraction representation of the irrational " + str(irrational) + " is " + InfiniteContinuedFraction(irrational, max_count) + ". ")
    
    elif selection == 4:
        print(" ")
        print("You have selected the explicit computation of a periodic continued fraction. A periodic continued fraction takes the form [a_0; a_1, ..., a_m, a_m+1, ..., a_m+n, ..., a_m+1, ..., a_m+n, ...], where a_0 is an integer, and a_i is a positive integer for all i ≥ 1. The non-repeating part should be entered as \"[a_0; a_1, ..., a_m]\", and the repeating part should be entered as \"[a_m+1; a_m+2, ..., a_m+n]\". ")
        print(" ")
        constant = input("Enter the non-repeating part of the periodic continued fraction. If there is no non-repeating part, simply press enter without typing anything. ")
        repeated = input("Enter the repeating part of the periodic continued fraction. (If only one integer a is repeated, enter \"[a; a]\".) ")
        print(" ")
        print("The quadratic irrational form of the provided periodic continued fraction is " + RepeatedContinuedFraction(constant, repeated)[1] + ", which is approximately equal to " + RepeatedContinuedFraction(constant, repeated)[0] + ". ")
        
def main():
    ContinuedFractionCalculator()

if __name__ == '__main__':
    main()
