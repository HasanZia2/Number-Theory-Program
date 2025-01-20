# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:16:10 2025

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
            if prime%integer == 0:
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

def QuadraticCongruence():
    # This function solves a provided quadratic congruence of the form 
    # ax^2 + bx + c ≡ 0 (mod p), where a, b, and c are positive integers,
    # and p is a positive odd prime such that p does not divide a.
    
    print("This program finds solutions to quadratic congruences of the form ax^2 + bx + c ≡ 0 (mod p) for positive integers a, b, c, and positive odd prime p such that p∤a. ")
    print(" ")
    a = int(input("Enter the value of a. "))
    while a <= 0:
        a = int(input("Your input for a was not a positive integer. Please try again. "))
    b = int(input("Enter the value of b. "))
    while b <= 0:
        b = int(input("Your input for b was not a positive integer. Please try again. "))
    c = int(input("Enter the value of c. "))
    while c <= 0:
        c = int(input("Your input for c was not a positive integer. Please try again. "))
    p = int(input("Enter the value of p. "))
    while not OddPrime(p) or a%p == 0:
        p = int(input("Your input for p was not a positive odd prime that does not divide a. Please try again. "))
        
    α = a%p
    β = b%p
    γ = c%p
    
    inverse = Inversion((2*α), p)%p
    discriminant = (β**2 - 4*α*γ)%p
    
    if a == 1 or a == -1:
        a = str(a).replace(str(1), "")
    a = str(a)
    if b == 1 or b == -1:
        b = str(b).replace(str(1), "")
    b = str(b)
    c = str(c)
    
    print(" ")
    if discriminant not in QuadraticResidue(p):
        print("The discriminant, " + str(discriminant) +", is not square mod " + str(p) + ". Hence, there exist no solutions. ")
    elif discriminant == 0:
        solution = (inverse*-β)%p
        print("The solutions of the quadratic congruence " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " ≡ 0 (mod " + str(p) + ") are of the form x ≡ " + str(solution) + " (mod " + str(p) + ").")
    else:
        discriminant_sqrt = QuadraticResidue(p).index(discriminant)
        solution_plus = (inverse*(-β + discriminant_sqrt))%p
        solution_minus = (inverse*(-β - discriminant_sqrt))%p
        if solution_plus > solution_minus:
            print("The solutions of the quadratic congruence " + a + "x^2 + " + b + "x + " + c + " ≡ 0 (mod " + str(p) + ") satisfy x ≡ " + str(solution_minus) + " (mod " + str(p) + ") or x ≡ " + str(solution_plus) + " (mod " + str(p) + ").")
        else:
            print("The solutions of the quadratic congruence " + a + "x^2 + " + b + "x + " + c + " ≡ 0 (mod " + str(p) + ") satisfy x ≡ " + str(solution_plus) + " (mod " + str(p) + ") or x ≡ " + str(solution_minus) + " (mod " + str(p) + ").")

def main():
    QuadraticCongruence()
    
if __name__ == '__main__':
    main()