# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:32:24 2025

@author: hzia2
"""

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

    pass

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
        factorial = int(input("Enter the number (a natural number) whose factorial is being taken. "))
        while factorial <= 0:
            factorial = int(input("The number you entered is either negative or zero. Please try again. "))
        WilsonsTheorem(prime, factorial)

def main():
    RemainderCalculator()
    
if __name__ == '__main__':
    main()