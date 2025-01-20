# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 00:01:32 2024

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

def ChineseRemainderTheorem():
    # This function finds the solution to the problem directly using the
    # foumulas for x_0 and the new modulo integer.
    
    print(" ")
    print("This program solves Chinese Remainder Theorem problems of the form ax ≡ b (mod m) ∧ cx ≡ d (mod n) ∀a, m, c, n ∈ Z+ and ∀b, d ∈ Z≥0. ")
    print(" ")
    a = int(input("Enter the value of a. "))
    while a <= 0:
        a = int(input("Your input for a was not a positive integer. Please try again. "))
    b = int(input("Enter the value of b. "))
    while b < 0:
        b = int(input("Your input for b was not a non-negative integer. Please try again. "))
    m = int(input("Enter the value of m. "))
    while m <= 0:
        m = int(input("Your input for m was not a positive integer. Please try again. "))
    c = int(input("Enter the value of c. "))
    while c <= 0:
        c = int(input("Your input for c was not a positive integer. Please try again. "))
    d = int(input("Enter the value of d. "))
    while d < 0:
        d = int(input("Your input for d was not a non-negative integer. Please try again. "))
    n = int(input("Enter the value of n. "))
    while n <= 0:
        n = int(input("Your input for n was not a positive integer. Please try again. "))
    print(" ")
    first_equation_gcd = EuclideanAlgorithm(a, m)[0]
    second_equation_gcd = EuclideanAlgorithm(c, n)[0]
    solution_list = EuclideanAlgorithm(m, n)
    if solution_list[0] != 1:
        print("Problem is invalid; m and n are not coprime, or at least one of m, n is negative. ")
    elif b%first_equation_gcd != 0 and d%second_equation_gcd == 0:
        if a != 1:
            print("No solutions exist; " + str(a) + "x ≡ " + str(b) + " (mod " + str(m) + ") has no solutions." )
        else:
            print("No solutions exist; x ≡ " + str(b) + " (mod " + str(m) + ") has no solutions." )
    elif b%first_equation_gcd == 0 and d%second_equation_gcd != 0:
        if a != 1:
            print("No solutions exist; " + str(c) + "x ≡ " + str(d) + " (mod " + str(n) + ") has no solutions." )
        else:
            print("No solutions exist; x ≡ " + str(d) + " (mod " + str(n) + ") has no solutions." )
    elif b%first_equation_gcd != 0 and d%second_equation_gcd != 0:
        print("No solutions exist; neither of the congruences have individual solutions. ")
    else:
        if a == 1:
            b_solution = b
        else:
            b_solution = b*Inversion(a, m)
        if c == 1:
            d_solution = d
        else:
            d_solution = d*Inversion(c, n)
        if m == solution_list[2]:
            s = solution_list[1]
            t = solution_list[3]
        else:
            s = solution_list[3]
            t = solution_list[1]
        x_0 = b_solution*t*n + d_solution*s*m
        modulo_solution = m*n
        x_0 = x_0%modulo_solution
        
        if a == 1 or a == -1:
            a = str(a).replace(str(1), "")
        a = str(a)
        if c == 1 or a == -1:
            c = str(c).replace(str(1), "")
        c = str(c)
        b = str(b)
        m = str(m)
        d = str(d)
        n = str(n)
        x_0 = str(x_0)
        modulo_solution = str(modulo_solution)
        print("The solution to " + a + "x ≡ " + b + " (mod " + m + ") ∧ " + c + "x ≡ " + d + " (mod " + n + ") is x ≡ " + x_0 + " (mod " + modulo_solution + "). ")

def main():
    ChineseRemainderTheorem()
    
if __name__ == '__main__':
    main()