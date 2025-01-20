# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:39:49 2025

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

def NumberOfSolutions():
    # This program finds the number of integral solutions to the diophantine
    # equation x^2 + y^2 = n.
    
    print("This program finds the number of integral solutions to the diophantine equation x^2 + y^2 = n for some positive integer n. ")
    print(" ")
    n = int(input("Enter the value of n. "))
    while n <= 0:
        n = int(input("Your input for n was not a positive integer. Please try again. "))
    
    prime_factorization = PrimeFactorization(n, [], [])
    prime_factors = prime_factorization[0]
    power_of_factor = prime_factorization[1]
    existence_of_solutions = True
    powers_of_1_mod_4 = []
    for prime in prime_factors:
        if prime%4 == 1:
            powers_of_1_mod_4.append(power_of_factor[prime_factors.index(prime)])
        elif prime%4 == 3 and power_of_factor[prime_factors.index(prime)]%2 == 1:
            prime_3_mod_4_odd_power = prime
            odd_power = power_of_factor[prime_factors.index(prime)]
            existence_of_solutions = False
            break
     
    print(" ")
    if existence_of_solutions:
        number_of_solutions = 4
        for power in powers_of_1_mod_4:
            number_of_solutions *= (power + 1)
        print("The number of integral solutions to x^2 + y^2 = " + str(n) + " is " + str(number_of_solutions) + ". ")
    else:
        print("x^2 + y^2 = " + str(n) + " has no solutions, because (among potentially others with the same properties) the prime factor " + str(prime_3_mod_4_odd_power) + " is 3 mod 4, and has odd power " + str(odd_power) + " in the prime factorization of " + str(n) + ". ")

def main():
    NumberOfSolutions()

if __name__ == '__main__':
    main()