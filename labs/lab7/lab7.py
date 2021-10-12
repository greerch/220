"""
Name: Caroline Greer
lab7.py

Discription: Solve the problems for lab 7

Certification of authenticity:
I certify that this assignment is entirely my own work
"""
from math import pi

def cash_conversion():
    value = eval(input("Enter integer: "))
    cents = 00
    print("{0:.2f}".format(value))

def encode():
    message = input("Enter message: ")
    key = eval(input("Enter an integer value key: "))
    new = ""
    for i in range(len(message)):
        num = ord(message[i])
        shift = num + key
        new = new + chr(shift)
    print(new, end=" ")

def sphere_area(radius):
    surface_area = 4 * pi * radius**2
    return round(surface_area

def sphere_volume(radius):
    volume = (4 / 3) * pi * radius**3
    return round(volume, 3)

def sum_n(n):
    total = n * (n + 1) / 2
    return round(total, 3)

def sum_n_cubes(n):
    total = (n ** 2 * (n + 1) ** 2) / 4
    return round(total, 3)

def encode_better():
    message = input("Enter message: ")
    key = input("Enter key: ")
    new = ""
    for i in range(len(message)):
        num = ord(message[i])
        module = i % len(key)
        shift = num + (ord(key[module]) - 97)
        new = new + chr(shift)
    print(new, end=" ")


 def main():
     cash_conversion()
     encode()
     sphere_area()
     sphere_volume()
     sum_n()
     sum_n_cubes()
     encode_better()
     pass

if __name__ == '__main__':
    main()
