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

def FermatsLittleTheorem():
    # This function applies Fermat's Little Theorem to solve
    # remainder problems involving exponentiation.

    pass

def WilsonsTheorem():
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
    while not OddPrime(prime) and prime != 2:
        prime = int(input("The number you entered is not prime. Please try again. "))
    type = input("Does the large number you want to divide involve exponentiation or factorials? (Enter \"exponentiation\" or \"factorial\".) ").lower
    while type != "exponentiation" and type != "factorial":
        type = input("You did not correctly select exponentiation or factorials. Please try again. (Enter \"exponentiation\" or \"factorial\".) ").lower

def main():
    RemainderCalculator()
    
if __name__ == '__main__':
    main()