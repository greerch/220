import math

"""
Name: Caroline Greer
lab3.py

Discription: Solve the problems for lab 3

Certification of authenticity:
I worked on sequence and pi with Jessica and Leslie, the rest are entirely my own work
"""

def average():
    number_hw = eval(input("Enter number of homeworks"))
    sum = 0
    for i in range(number_hw):
        hw_input = eval(input("Enter your grade on HW" + str(i + 1)))
        sum = sum + hw_input
    average = sum / number_hw
    print("The average of your homeworks is: ", average)

average()


def tip_jar():
   tip = 0
   for i in range(1, 6):
      tip_amount = int(input("Enter tip amount: "))
      # tip = tip + tip_amount
      tip += tip_amount
   print("The total tips are: ", tip)

tip_jar()


def newton():
    numberx = eval(input("Input number x: "))
    num_approx = eval(input("Input number of desired approximations: "))
    for i in range(num_approx):
        num_approx = (num_approx + (numberx / num_approx)) / 2
    print ("Your number was:", numberx, "and here is the value of the approximation:", num_approx)

newton()


def sequence():
    num = eval(input("Input number of terms in series: "))
    total = 1
    for i in range(0, num):
        remainder = i % 2
        total = (total + 2*remainder)
        print(total, end="")

sequence()


def pi():
    n = eval(input("Input number of terms in series (n): "))
    top = 2
    num = 0
    bottom = 1
    den = 0
    for i in range(2, n):
        remainder_top = i % 2
        top = (top + 2*remainder_top)
        num = top + num
        remainder_bottom = i % 2
        bottom = (bottom + 2*remainder_bottom)
        den = bottom + den
    output = num/den
    pi_answer = output * 2
    print(pi_answer)
 # I know this is wrong, but I do not know what to do!
pi()

