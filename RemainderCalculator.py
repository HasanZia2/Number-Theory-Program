# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:32:24 2025

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

def Inversion(integer, modulo):
    # This function finds an inverse to an integer mod another integer.
    
    equation_list = EuclideanAlgorithm(modulo, integer)
    if integer == equation_list[2]:
        equation_inverse = equation_list[1]
    else:
        equation_inverse = equation_list[3]
    return equation_inverse

def OddPrime(prime):
    # This function determines if an integer is an odd prime.
    
    odd_prime = True
    if prime != int(prime) or prime <= 2:
        odd_prime = False
    else:
        for integer in range(2, prime):
            if prime/integer == int(prime/integer):
                odd_prime = False
                break
    return odd_prime

def FermatsLittleTheorem(prime, base, exponent):
    # This function applies Fermat's Little Theorem to solve
    # remainder problems involving exponentiation.

    reducedExponent = exponent%(prime - 1)
    return base**reducedExponent%prime

def WilsonsTheorem(prime, factorial):
    # This function applies Wilson's Theorem to solve
    # remainder problems involving factorials.

    remainder_inverse = 1
    for i in range(factorial - prime + 1, 0):
        remainder_inverse = remainder_inverse*i
    if remainder_inverse < 0:
        remainder_inverse = remainder_inverse%prime
    remainder = -1*Inversion(remainder_inverse, prime)%prime
    return remainder

def RemainderCalculator():
    # This function finds the remainder when dividing large natural 
    # numbers (involving exponentiation or factorials) by prime
    # numbers.

    print("This program finds the remainder when dividing large natural numbers (involving exponentiation or factorials) by prime numbers. ")
    print(" ")
    prime = int(input("Enter the prime you would like to divide by. "))
    print(" ")
    while not OddPrime(prime) and prime != 2:
        prime = int(input("The number you entered is not prime. Please try again. "))
    type = input("Does the large number you want to divide involve exponentiation or factorials? (Enter \"E\" for the former or \"F\" for the latter.) ").upper()
    while type != "E" and type != "F":
        type = input("You did not correctly select exponentiation or factorials. Please try again. (Enter \"E\" for the former or \"F\" for the latter.) ").upper()
    print(" ")
    if type == "E":
        base = int(input("Enter the base (a natural number) of the exponential expression. "))
        while base <= 0:
            base = int(input("The number you entered is either negative or zero. Please try again. "))
        exponent = int(input("Enter the exponent (a natural number) of the exponential expression. "))
        while exponent <= 0:
            exponent = int(input("The number you entered is either negative or zero. Please try again. "))
        remainder = FermatsLittleTheorem(prime, base, exponent)
        print("The remainder on dividing " + str(base) + "^" + str(exponent) + " by " + str(prime) + " is " + str(remainder) + ". ")
    else:
        factorial = int(input("Enter the number (a natural number less than the prime chosen) whose factorial is being taken. "))
        while factorial <= 0 or factorial > prime:
            factorial = int(input("The number you entered is either negative or zero, or is greater than the prime you chose, " + str(prime) + ". Please try again. "))
        print(" ")
        if factorial == prime:
            print("Your chosen number whose factorial is being taken is equal to your chosen prime, so we have that " + str(factorial) + "! ≡ 0 (mod " + str(prime) + "); the remainder is 0. ")
        else:
            remainder = WilsonsTheorem(prime, factorial)
            print("The remainder on dividing " + str(factorial) + "! by " + str(prime) + " is " + str(remainder) + ". ")

def main():
    RemainderCalculator()
    
if __name__ == '__main__':
    main()