from algorithms import *
from graphics import Point, Rectangle

"""
Name: Caroline Greer
lab13.py

Discription: Complete Lab 13

Certification of authenticity:
I certify that this assignment is entirely my own work
"""


def trade_alert(filename):
    file = open(filename, "r")
    file_nums = file.readline()
    file_value = file_nums.split(" ")
    for index in range(0, len(file_value)):
        if 830 < int(file_value[index]):
            print("this is a warning, the trade volume is above 830. At", index + 1, "seconds the trade value is",
                  file_value[index])
        if 500 == int(file_value[index]):
            print("pay attention, the trade volume is at 500. This is happening at", index + 1, "seconds")
    file.close()



def main():
    trade_alert("trades.txt")
    is_in_binary(20, [15, 20, 30, 40, 50])
    selection_sort([20, 40, 4, 28, 19, 3, 22, 43, 0, 18, -4])
    rect_sort([Rectangle(Point(1, 2), Point(3, 4)), Rectangle(Point(1, 8), (Point(10, 1)))])

main()


"""
from algorithms.py

def is_in_binary(search_val, values):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (right + left) // 2
        middle_value = values[middle]
        if search_val == middle_value:
            return True
        elif search_val < middle_value:
            right = middle - 1
        elif search_val > middle_value:
            left = middle + 1
    return False


def selection_sort(values):
    n = len(values)
    for bottom in range(n-1):
        lowest = bottom
        for i in range(bottom + 1, n):
            if values[i] < values[lowest]:
                lowest = i
        values[bottom], values[lowest] = values[lowest], values[bottom]
        
        
def rect_sort(rectangles):
    area_list = []
    for i in range(len(rectangles)):
        area_list.append(calc_area(rectangles[i]))
    selection_sort(area_list)
    return area_list


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    p1x, p1y = p1.getX(), p1.getY()
    p2x, p2y = p2.getX(), p2.getY()
    base = abs(p1x - p2x)
    height = abs(p1y - p2y)
    area = base * height
    return area
"""
