from lab13.algorithms import *
from random import randint

"""
Name: Caroline Greer
lab12.py

Discription: Complete Lab 12

Certification of authenticity:
I certify that this assignment is entirely my own work
"""


def find_and_remove_first(list, value):
    ind = list.index(value)
    list.pop(ind)
    list.insert(ind, "Caty")
    print(list)


def good_input():
    num = eval(input("what is your value? "))
    while 1 > num or num > 10:
        if 1 > num:
            print("your value is too low")
        elif num > 10:
            print("your value is too high")
        num = eval(input("what is your value? "))
    else:
        return num


def num_digits():
    num = eval(input("what is your value? "))
    var = num
    while num > 0:
        val = 0
        var = num
        while num != 0:
            num = num // 10
            val += 1
        print(var, "has", val, "digits")
        num = eval(input("what is your value? "))
    print("your value is out of range")


def hi_lo_game():
    value = randint(0, 100)
    guesses = 1
    while guesses < 8:
        num = eval(input("what is your guess? "))
        if num > value:
            print("you are too high")
            guesses += 1
        elif num < value:
            print("you are too low")
            guesses += 1
        else:
            print("You win in", guesses, "guesses")
            return
    print("Sorry, you lose. The number was", value)



def main():
    find_and_remove_first([15, 20, 30, 40, 50], 30)
    read_data("read_data_test_data.txt")
    is_in_linear(12, [15, 20, 30, 40, 50])
    good_input()
    num_digits()
    hi_lo_game()


main()


"""
Code from algorithms.py: 

def read_data(filename):
    file = open(filename, "r")
    file = file.read()
    lines = file.split()
    num = 0
    while num < len(lines):
        lines[num] = eval(lines[num])
        num += 1
    return lines


def is_in_linear(search_val, values):
    num = 0
    while num < len(values):
        if search_val in values:
            return True
        else:
            return False
"""
