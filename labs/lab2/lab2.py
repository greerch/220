import math

"""
Name: Caroline Greer
lab2.py
"""

def sum_of_threes():
    upper_bound = eval(input("Enter the upper bound: "))
    total = 0
    for var in range(3, upper_bound+1,3):
        total =  total + var
    print(total)


def multiplication_table():
    print(  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10)
    for row in range (1,11):
        print(row, end=" ")
        for col in range (1,11):
            print(col*row, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter length of side a"))
    b = eval(input("Enter length of side b"))
    c = eval(input("Enter length of side c"))
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)


def sumSquares():
    lower_bound = eval(input("Enter lower bound: "))
    upper_bound = eval(input("Enter upper bound: "))
    total = 0
    for var in range(lower_bound, upper_bound+1):
        total = total + var**2
    print(total)


def power():
    base = eval(input("Enter base number: "))
    exponent = eval(input("Enter exponent: "))
    total = 1
    for var in range(exponent):
        total = total * base
    print(base, "^", exponent, "=", total)


