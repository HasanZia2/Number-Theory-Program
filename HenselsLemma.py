# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 21:23:35 2025

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

def Derivative(polynomial):
    # This function finds the derivative of a given polynomial.
    
    polynomial_list = (polynomial.replace(" ", "")).split("+")
    derivative_list = []
    for monomial in polynomial_list:
        if "^" not in list(monomial):
            if "x" in list(monomial):
                derivative_list.append(monomial.replace("x", ''))
        else:
            monomial_length = len(list(monomial))
            exponent = int(list(monomial)[monomial_length - 1])
            if monomial.split("x")[0] == '':
                if exponent == 2:
                    derivative_monomial = "2x"
                else:
                    derivative_monomial = str(exponent) + "x^" + str(exponent - 1)
                derivative_list.append(derivative_monomial)
            else:
                coefficient = int(monomial.split("x")[0])
                if exponent == 2:
                    derivative_monomial = str(2*coefficient) + "x"
                else:
                    derivative_monomial = str(coefficient*exponent) + "x^" + str(exponent - 1)
                derivative_list.append(derivative_monomial)
    
    derivative = ""
    for derivative_monomial in derivative_list:
        derivative = derivative + derivative_monomial
        if derivative_list.index(derivative_monomial) != len(derivative_list) - 1:
            derivative = derivative + " + "
            
    return derivative

def Polynomial_Evaluation(polynomial, solution):
    # This function evaluates a given polynomial at a given value of x.
    
    polynomial_list = (polynomial.replace(" ", "")).split("+")
    
    value_list = []
    for monomial in polynomial_list:
        if "^" not in list(monomial):
            if "x" not in list(monomial):
                monomial_value = int(monomial)
                value_list.append(monomial_value)
            else:
                monomial_value = int(eval(monomial.replace("x", "*(" + str(solution) + ")")))
                value_list.append(monomial_value)
        else:
            if monomial.split("x")[0] == '':
                monomial_value = monomial.replace("x", "(" + str(solution) + ")")
                monomial_value = monomial_value.replace("^", "**")
                monomial_value = int(eval(monomial_value))
                value_list.append(monomial_value)
            else:
                monomial_value = monomial.replace("x", "*(" + str(solution) + ")")
                monomial_value = monomial_value.replace("^", "**")
                monomial_value = int(eval(monomial_value))
                value_list.append(monomial_value)
    polynomial_value = 0
    
    for monomial_value in value_list:
        polynomial_value += monomial_value
    
    return polynomial_value

def HenselsLemma():
    # This function finds lifts to the congruence f(x) ≡ 0 (mod p^(k + 1))
    # given some positive prime p, non-negative integer k, and positive
    # integer solution a to the congruence f(x) ≡ 0 (mod p^k).
    
    print("This program finds lifts from congruences of the form f(x) ≡ 0 (mod p^k) (*) to congruences of the form f(x) ≡ 0 (mod p^(k + 1)), given some integer a satisfies (*). Here, x is a variable, p is a positive prime, and k is a positive integer. ")
    print(" ")
    polynomial = input("Enter a polynomial of a form (a_1)x^(n) + (a_2)x^(n - 1) + ... + (a_n)x + (a_(n + 1)). (If a term is negative, write it as adding a negative coefficient. For example, write x^2 - x as x^2 + -1x.) ")
    p = int(input("Enter the value of p. "))
    while not OddPrime(p):
        if p == 2:
            break
        else:
            p = int(input("Your input for p was not a positive prime. Please try again. "))
    k = int(input("Enter the value of k. "))
    while k < 0:
        k = int(input("Your input for k was not a positive integer. Please try again. "))
    if k != 1:
        a = int(input("Enter a solution a to the congruence " + str(polynomial) + " ≡ 0 (mod " + str(p) + "^" + str(k) + "). "))
    else:
        a = int(input("Enter a solution a to the congruence " + str(polynomial) + " ≡ 0 (mod " + str(p) + "). "))
    
    polynomial_eval = Polynomial_Evaluation(polynomial, a)
    derivative_eval = Polynomial_Evaluation(Derivative(polynomial), a)
    
    if polynomial_eval%(p**k) != 0:
        a = int(input("Your input for a is not a valid solution. Please try again. "))
    
    print(" ")
    if derivative_eval%p != 0:
        for t in range(0, p):
            if (polynomial_eval/(p**k) + derivative_eval*t)%p == 0:
                solution = a + t*(p**k)
        print("Case (i); " + str(solution) + " is a solution mod " + str(p) + "^" + str(k + 1) + ", and is the only lift mod " + str(p) + "^" + str(k + 1) + ". ")
    elif polynomial_eval%(p**(k + 1)) == 0:
        print("Case (ii); " + str(a) + " + " + str(p**k) + "t is a solution mod " + str(p) + "^" + str(k + 1) + " ∀t ∈ Z. ")
    else:
        print("Case (iii); " + str(p) + "|f'(" + str(a) + ") = " + str(derivative_eval) + ", but " + str(a) + " does not satisfy f(x) ≡ 0 (mod " + str(p) + "^" + str(k + 1) + "), so there exist no solutions. ")
        
def main():
    HenselsLemma()

if __name__ == '__main__':
    main()