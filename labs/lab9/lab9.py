"""
Name: Caroline Greer
lab9.py

Discription: Solve the problems for lab 9

Certification of authenticity:
I certify that this assignment is entirely my own work
"""
from graphics import *
import math

def addTen(nums):
    for number in range(len(nums)):
        nums[number] = nums[number] + 10

def testTens():
    nums = [1, 2, 3]
    print(nums)
    addTen(nums)
    print(nums)

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc

def writeSumOfSquares():
    in_file = input("enter a file name with more than two numbers with .txt ending")
    file = open(in_file, "r")
    out_file = open("sum_out.txt", 'w')
    for line in file:
        value = line.split(" ")
        toNumbers(value)
        squareEach(value)
        tot = sumList(value)
        print("Sum of squares = " + str(tot), file=out_file, end='\n')
    file.close()
    out_file.close()

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])


def starter():
    weight = eval(input("What is the players weight"))
    numWins = int(input("How many wins has the player had?"))
    if 150 >= weight >= 160 and numWins >= 5:
        print("They should start")
    elif weight > 199 or numWins > 20:
        print("They should start")
    else:
        print("They should not start")

def leapYear(year):
    if year % 400 == 0:
        print(str(year) + " is a leap year")
    elif year % 4 == 0 and not year % 100 == 0:
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")


def circleOverlap():
    width = 400
    height = 400
    win = GraphWin("Lab 9", width, height)

    inst_pt = Point(width / 2, height - 10)
    final_pt = Point((width / 2), (height - 50))
    instructions = Text(inst_pt, "Click to add two points: the first click is center and second is for circumference")
    instructions.draw(win)

    point_center_A = win.getMouse()
    point_center_A.draw(win)
    point_circumference_A = win.getMouse()
    point_circumference_A.draw(win)

    xvalue_center_A = point_center_A.getX()
    yvalue_center_A = point_center_A.getY()
    xvalue_circumference_A = point_circumference_A.getX()
    yvalue_circumference_A = point_circumference_A.getY()

    xequation_A = (xvalue_circumference_A - xvalue_center_A) ** 2
    yequation_A = (yvalue_circumference_A - yvalue_center_A) ** 2
    radius_A = math.sqrt(xequation_A + yequation_A)

    shape_A = Circle(point_center_A, radius_A)
    shape_A.draw(win)
    instructions.undraw()

    instructions_B = Text(inst_pt, "Click to add two more points: the first click is center and second is circumference")
    instructions_B.draw(win)

    point_center_B = win.getMouse()
    point_center_B.draw(win)
    point_circumference_B = win.getMouse()
    point_circumference_B.draw(win)

    xvalue_center_B = point_center_B.getX()
    yvalue_center_B = point_center_B.getY()
    xvalue_circumference_B = point_circumference_B.getX()
    yvalue_circumference_B = point_circumference_B.getY()

    xequation_B = (xvalue_circumference_B - xvalue_center_B) ** 2
    yequation_B = (yvalue_circumference_B - yvalue_center_B) ** 2
    radius_B = math.sqrt(xequation_B + yequation_B)

    shape_B = Circle(point_center_B, radius_B)
    shape_B.draw(win)
    instructions_B.undraw()

    difference = math.sqrt(((point_center_A.getX() - point_center_B.getX()) ** 2) +
                 ((point_center_A.getY() - point_center_B.getY()) ** 2))


    if (radius_B + radius_A) < difference:
        message = Text(inst_pt, "The circles do not overlap.")
        message.draw(win)
    else:
        message = Text(inst_pt, "The circles overlap.")
        message.draw(win)

    close_window = Text(final_pt, "Click to close the window")
    close_window.draw(win)
    win.getMouse()
    win.close()
    win.close()


def main():
    testTens()
    addTen([1, 2, 3])
    squareEach([1, 2, 3])
    sumList([1, 2, 3])
    toNumbers(["1", "2", "3"])
    writeSumOfSquares()
    starter()
    leapYear(2000)
    circleOverlap()
    pass

main()