# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:00:06 2025

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

def QuadraticResidue(prime):
    # This function finds the list of quadratic residues mod n for some positive
    # integer n. (In the context of this program, it is used specifically mod
    # p, where p is some odd prime.)

    quadratic_residue_list = []
    for integer in range(0, int((prime + 1)/2)):
        quadratic_residue = (integer**2)%prime
        if quadratic_residue not in quadratic_residue_list:
            quadratic_residue_list.append(quadratic_residue)
    return quadratic_residue_list

def LegendreSymbol():
    # This function solves the Legendre symbol (a/p), where a is some positive
    # integer, and p is some positive odd prime.
    
    print("This program solves the value of the Legendre symbol (a/p), where a is some positive integer, and p is some positive odd prime.")
    print(" ")
    a = int(input("Enter the value of a. "))
    while a <= 0:
        a = int(input("Your input for a was not a positive integer. Please try again. "))
    p = int(input("Enter the value of p. "))
    while not OddPrime(p):
        p = int(input("Your input for p was not a positive odd prime. Please try again. "))
    print(" ")
    
    if a%p == 0:
        print("(" + str(a) + "/" + str(p) + ") = 0. ")
    elif a%p in QuadraticResidue(p):
        print("(" + str(a) + "/" + str(p) + ") = 1. ")
    else:
        print("(" + str(a) + "/" + str(p) + ") = -1. ")

def main():
    LegendreSymbol()
    
if __name__ == '__main__':
    main()