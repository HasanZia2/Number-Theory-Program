# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:16:23 2025

@author: hzia2
"""

def NormMapConsequences():
    # This function finds an integral solution to a diophantine equation of
    # the form x^2 - dy^2 = mn, given integral solutions to the equations
    # x^2 - dy^2 = m and x^2 - dy^2 = n.
    
    print("This program finds an integral solution (x, y) to the diophantine equation x^2 - dy^2 = mn, given integral solutions to the equations x^2 - dy^2 = m and x^2 - dy^2 = n, where d is a positive integer and m, n are non-zero integers. ")
    print(" ")
    d = int(input("Enter the value of d. "))
    while d <= 0:
        d = int(input("Your input for d was not a positive integer. Please try again. "))
    m = int(input("Enter the value of m. "))
    while m == 0:
        m = int(input("Your input for m was not non-zero. Please try again. "))
    n = int(input("Enter the value of m. "))
    while n == 0:
        n = int(input("Your input for n was not non-zero. Please try again. "))
    x_1 = int(input("Enter the value of x in the solution (x, y) to the equation x^2 - " + str(d) + "y^2 = " + str(m) + ". "))
    y_1 = int(input("Enter the value of y in the solution (x, y) to the equation x^2 - " + str(d) + "y^2 = " + str(m) + ". "))
    while x_1**2 - d*(y_1**2) != m:
        print(" ")
        print("Your inputs (x, y) do not satisfy the first equation. ")
        print(" ")
        x_1 = int(input("Please enter a new value for x. "))
        y_1 = int(input("Please enter a new value for y. "))
    x_2 = int(input("Enter the value of x in the solution (x, y) to the equation x^2 - " + str(d) + "y^2 = " + str(n) + ". "))
    y_2 = int(input("Enter the value of y in the solution (x, y) to the equation x^2 - " + str(d) + "y^2 = " + str(n) + ". "))
    while x_2**2 - d*(y_2**2) != n:
        print(" ")
        print("Your inputs (x, y) do not satisfy the second equation. ")
        print(" ")
        x_2 = int(input("Please enter a new value for x. "))
        y_2 = int(input("Please enter a new value for y. "))
        
    x_3 = x_1*x_2 + d*y_1*y_2
    y_3 = x_1*y_2 + x_2*y_1
    
    print(" ")
    print("The integral solution (x, y) to the equation x^2 - " + str(d) + "y^2 = " + str(m*n) + " is (x, y) = (" + str(x_3) + ", " + str(y_3) + "). ")
    
def main():
    NormMapConsequences()

if __name__ == '__main__':
    main()