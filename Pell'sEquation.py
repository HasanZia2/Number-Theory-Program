# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:29:54 2025

@author: hzia2
"""

#Pell's Equation

import math
import copy

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

def InfiniteContinuedFraction(irrational, max_count, square_root):
    # This function finds the infinite canonical continued-fraction representation
    # of an irrational number. The amount of integers displayed in the
    # representation is decided by the user. This function also finds the period
    # of the continued-fraction representation of the irrational number.
    
    continued_fraction = []
    current_count = 0
    period_found = False

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
        current_integer = ICFAlgorithm(irrational, current_count)[1]
        continued_fraction.append(current_integer)
        current_count += 1
        if current_integer == 2*continued_fraction[0] and square_root and not period_found:
            period = len(continued_fraction) - 1
            period_found = True
    
    if square_root and not period_found:
        continued_fraction_period = copy.deepcopy(continued_fraction)
        while not period_found:
            current_integer = ICFAlgorithm(irrational, current_count)[1]
            continued_fraction_period.append(ICFAlgorithm(irrational, current_count)[1])
            current_count += 1
            if current_integer == 2*continued_fraction_period[0]:
                period = len(continued_fraction_period) - 1
                period_found = True
    
    continued_fraction_list = copy.deepcopy(continued_fraction)
    continued_fraction = str(continued_fraction).replace(",", ";", 1)
    continued_fraction = continued_fraction.replace("]", ", ...]")
    
    if square_root:
        return [continued_fraction, str(period), continued_fraction_list]
    else:
        return continued_fraction

def PellsEquation():
    # This function solves Pell's Equation, a diophantine equation
    # of the form x^2 - dy^2 = ±1, where d is a non-square integer.
    
    print("This program solves Pell's Equation, a diophantine equation of the form x^2 - dy^2 = ±1, where d is a non-square integer greater than or equal to 2. ")
    print(" ")
    d = int(input("Enter the value of d. "))
    while d < 2 or math.sqrt(d) == int(math.sqrt(d)):
        print(" ")
        if d < 2:
            print("Your value of d is less than 2. ")
        else:
            print("Your value of d is a square integer. ")
        print(" ")
        d = int(input("Please enter a new value for d. "))
    print(" ")
    sign = input("Do you want to solve x^2 - " + str(d) + "y^2 = 1 or x^2 - " + str(d) + "y^2 = -1? Enter \"p\" for the former, or \"n\" for the latter. ").lower()
    while sign != "p" and sign != "n":
        print(" ")
        sign = input("Your input was not valid. Enter either \"p\" or \"n\". ")
    print(" ")
    period = int(InfiniteContinuedFraction(math.sqrt(d), 1, True)[1])
    solutions = []
    if sign == "p":
        number_of_solutions = int(input("Enter the number of (x, y)-pair solutions desired. "))
        while number_of_solutions <= 0:
            print(" ")
            number_of_solutions = int(input("Your number of solutions is invalid (less than or equal to 0). Please try again. "))
        if d%2 == 0:
            for r in range(1, number_of_solutions + 1):
                final_index = period*number_of_solutions - 1
                continued_fraction = InfiniteContinuedFraction(math.sqrt(d), final_index, True)[2]
                solutions.append((pAlgorithm(continued_fraction, period*r - 1), qAlgorithm(continued_fraction, period*r - 1)))
        else:
            for r in range(2, 2*number_of_solutions + 2, 2):
                final_index = period*number_of_solutions - 1
                continued_fraction = InfiniteContinuedFraction(math.sqrt(d), final_index, True)[2]
                solutions.append((pAlgorithm(continued_fraction, period*r - 1), qAlgorithm(continued_fraction, period*r - 1)))
        print(solutions)
    else:
        if d%2 == 0:
            print("The diophantine equation x^2 - " + str(d) + "y^2 = -1 has no solutions. ")
        else:
            number_of_solutions = int(input("Enter the number of (x, y)-pair solutions desired. "))
            while number_of_solutions <= 0:
                print(" ")
                number_of_solutions = int(input("Your number of solutions is invalid (less than or equal to 0). Please try again. "))
            for r in range(1, 2*number_of_solutions + 1, 2):
                final_index = period*number_of_solutions - 1
                continued_fraction = InfiniteContinuedFraction(math.sqrt(d), final_index, True)[2]
                solutions.append((pAlgorithm(continued_fraction, period*r - 1), qAlgorithm(continued_fraction, period*r - 1)))
            print(solutions)

        
def main():
    PellsEquation()

if __name__ == '__main__':
    main()