"""
Name: Caroline Greer
lab5.py

Discription: Solve the problems for lab 5

Certification of authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import *

# OPTIONAL!
def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    point_one = win.getMouse()
    point_one.draw(win)
    point_two = win.getMouse()
    point_two.draw(win)
    point_three = win.getMouse()
    point_three.draw(win)
    triangle_shape = Polygon(point_one, point_two, point_three)
    triangle_shape.draw(win)

    # and display its area in the graphics window.
    AX = point_one.getX() - point_two.getX()
    AY = point_one.getY() - point_two.getY()
    BX = point_two.getX() - point_three.getX()
    BY = point_two.getY() - point_three.getY()
    CX = point_three.getX() - point_one.getX()
    CY = point_three.getY() - point_one.getY()
    a_length = abs(((AX ** 2) - (AY ** 2) ** 1/2))
    b_length = abs(((BX ** 2) - (BY ** 2) ** 1/2))
    c_length = abs(((CX ** 2) - (CY ** 2) ** 1/2))
    s_value = (a_length + b_length + c_length) / 2
    area = (s_value * (s_value - a_length) * (s_value - b_length) * (s_value - b_length)) ** 1/2
    perimeter = a_length + b_length + c_length

    per_text = Text(Point(100, 20), round(perimeter, 5))
    per_text.draw(win)
    ar_text = Text(Point(100, 70), round(area, 5))
    ar_text.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_user_input = Entry(Point(win_width / 2 + 10, win_height / 2 + 40), 10)
    red_user_input.draw(win)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_user_input = Entry(Point(green_text_pt.getX() + 60, green_text_pt.getY()), 10)
    green_user_input.draw(win)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_user_input = Entry(Point(blue_text_pt.getX() + 60, blue_text_pt.getY()), 10)
    blue_user_input.draw(win)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_user_input.getText())
        green = int(green_user_input.getText())
        blue = int(blue_user_input.getText())
        colors = color_rgb(red, green, blue)
        shape.setFill(colors)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("Enter the values to be entered as a string: ")
    print(string[0])
    print(string[-1])
    print(string[1:4])
    print(string[0] + string[-1])
    for value in range(len(string)):
        print(string[value])
    for i in range(10):
        print(string[0:3], end=" ")
    print(len(string))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:4]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], values[5]]
    print(x)
    x = values[0] + values[2] + eval(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    string_value = int(input("Enter the number of terms to be displayed: "))
    list = [2, 4, 6]
    total = 0
    for i in range(string_value):
        module = i % 3
        total = total + list[module]
        print(list[module], end=" ")
    print("sum = ", total)


    def main():
    # target()
    # triangle()
    # color_shape()
    pass


main()
