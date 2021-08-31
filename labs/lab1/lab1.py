"""
Name: <Caroline Greer>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area=", area)


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width:"))
    area = length * width
    print("Area=", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("Volume=", volume)


def shooting_percentage():
    total_shots = eval(input("Enter Total Shots:"))
    shots_made = eval(input("Enter Shots Made:"))
    shooting_percentage = shots_made / total_shots * 100
    print("Shooting_Percentge=", shooting_percentage)


def coffee():
    pounds = eval(input("Pounds of Coffee:"))
    coffee_cost = 10.50 * pounds
    shipping_cost = 0.86 * pounds
    fixed_cost = 1.50
    total_cost = coffee_cost + shipping_cost + fixed_cost
    print("Total_Cost=",total_cost)


def kilometers_to_miles():
    kilometers = eval(input("Total Kilometers Driven:"))
    miles = kilometers / 1.61
    print("Number_of_Miles=", miles)
