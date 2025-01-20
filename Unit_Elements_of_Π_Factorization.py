# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 02:01:50 2025

@author: hzia2
"""

import math

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

def PrimeFactorization(integer, prime_factors, power_of_factor):
    # This function gives a list of the prime factors of a positive integer
    # greater than 1, as well as a list of the respective powers of the prime
    # factors in the factorization of the integer.
    
    integer = int(integer)
    if integer <= 1:
        return [prime_factors, power_of_factor]
    else:
        prime_factor_found = False
        for number in range(2, integer):
            if number == 2 or OddPrime(number) == True:
                if integer%number == 0:
                    if number not in prime_factors:
                        integer_copy = integer
                        prime_factors.append(number)
                        power = 0
                        while integer_copy%number == 0:
                            integer_copy = integer_copy/number
                            power += 1
                        power_of_factor.append(power)
                    prime_factor_found = True
                    return PrimeFactorization(integer/(number**power), prime_factors, power_of_factor)
        if not prime_factor_found:
            if integer not in prime_factors:
                integer_copy = integer
                prime_factors.append(integer)
            if integer != 1:
                power_of_factor.append(1)
            return [prime_factors, power_of_factor]

def Pi_Of_Prime_Factors(prime_factors):
    # This function finds the elements of Π associated with the prime
    # factors of an integer.
    
    pi_list = []
    number_of_pi_terms = 0
    for prime in prime_factors:
        if prime == 2:
            pi_list.append(1 + 1j)
            number_of_pi_terms += 1
        if prime%4 == 1:
            for number1 in range(1, prime):
                number2 = math.sqrt(prime - number1**2)
                if number2 == int(number2):
                    if number1 < number2:
                        pi_list.append(number1 + number2*(1j))
                        pi_list.append(number1 - number2*(1j))
                    else:
                        pi_list.append(number2 + number1*(1j))
                        pi_list.append(number2 - number1*(1j))
                    break
        if prime%4 == 3:
            pi_list.append(prime)
            number_of_pi_terms += 1
    return pi_list

def Unit_Elements_of_Π_Factorization():
    # This function finds the factorization of a Gaussian integer in terms of
    # a Gaussian unit and elements of the set Π.
    
    print("This program expresses a Gaussian integer α in the form α = a + bi for integers a, b as the product of a Gaussian unit and the elements of Π. ")
    print(" ")
    a = int(input("Enter the value of the integer a. "))
    b = int(input("Enter the value of the integer b. "))
    α = a + b*(1j)
    prime_factors = PrimeFactorization(int(abs(a**2) + abs(b**2)), [], [])[0]
    pi_list = Pi_Of_Prime_Factors(prime_factors)
    pi_factors = []
    power_of_factor = []
    factorization = ""
    for pi in pi_list:
        quotient = α/pi
        if ((round(quotient.real) - 0.001 <= quotient.real <= round(quotient.real)) or (round(quotient.real) <= quotient.real <= round(quotient.real) + 0.001)) and ((round(quotient.imag) - 0.001 <= quotient.imag <= round(quotient.imag)) or (round(quotient.imag) <= quotient.imag <= round(quotient.imag) + 0.001)):
            quotient = round(quotient.real) + round(quotient.imag)*(1j)
        if quotient.real == int(quotient.real) and quotient.imag == int(quotient.imag):
            pi_factors.append(pi)
            power_of_pi = 0
            while (quotient.real == int(quotient.real) and quotient.imag == int(quotient.imag)):
                power_of_pi += 1
                quotient = quotient/pi
                if ((round(quotient.real) - 0.001 <= quotient.real <= round(quotient.real)) or (round(quotient.real) <= quotient.real <= round(quotient.real) + 0.001)) and ((round(quotient.imag) - 0.001 <= quotient.imag <= round(quotient.imag)) or (round(quotient.imag) <= quotient.imag <= round(quotient.imag) + 0.001)):
                    quotient = round(quotient.real) + round(quotient.imag)*(1j)
            power_of_factor.append(power_of_pi)
    unit_quotient = 1
    for pi in pi_factors:
        unit_quotient *= pi**power_of_factor[pi_factors.index(pi)]
    unit = α/unit_quotient
    if ((round(unit.real) - 0.001 <= unit.real <= round(unit.real)) or (round(unit.real) <= unit.real <= round(unit.real) + 0.001)) and ((round(unit.imag) - 0.001 <= unit.imag <= round(unit.imag)) or (round(unit.imag) <= unit.imag <= round(unit.imag) + 0.001)):
        unit = round(unit.real) + round(unit.imag)*(1j)
    if unit == 1j:
        factorization = factorization + "(i)"
    elif unit == -1:
        factorization = factorization + "(-1)"
    elif unit == -1j:
        factorization = factorization + "(-i)"
    for pi in pi_factors:
        if pi.imag != 0:
            prime_factor = pi.real**2 + pi.imag**2
        else:
            prime_factor = pi
        if pi.imag > 0:
            if power_of_factor[pi_factors.index(pi)] != 1:
                factorization = factorization + "(π_" + str(int(prime_factor)) + ")^" + str(int(power_of_factor[pi_factors.index(pi)]))
            else:
                factorization = factorization + "(π_" + str(int(prime_factor)) + ")"
        else:
            if power_of_factor[pi_factors.index(pi)] != 1:
                factorization = factorization + "(π" + '\u0305' + "  _" + str(int(prime_factor)) + ")^" + str(int(power_of_factor[pi_factors.index(pi)]))
            else:
                factorization = factorization + "(π" + '\u0305' + "  _" + str(int(prime_factor)) + ")"
            
    print(" ")
    if b > 0:
        print("The factorization of " + str(a) + " + " + str(b) + "i is " + factorization + ". ")
    else:
        print("The factorization of " + str(a) + " - " + str(abs(b)) + "i is " + factorization + ". ")

def main():
    Unit_Elements_of_Π_Factorization()

if __name__ == '__main__':
    main()