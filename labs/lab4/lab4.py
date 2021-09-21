"""
Name: Caroline Greer
lab4.py

Discription: Solve the problems for lab 4

Certification of authenticity:
I worked with Jessica and Leslie on the problems
"""

from graphics import *
from math import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add Square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(20, 20), Point(60, 60))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shapeb = shape.clone()
        shapeb.move(dx, dy)
        shapeb.draw(win)

    undo_instructions = instructions.undraw()
    close_window = Text(inst_pt, "Click again to quit")
    close_window.draw(win)
    win.getMouse()
    win.close()

squares()




def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    pass

    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add two points")
    instructions.draw(win)

    point_one = win.getMouse()
    point_one.draw(win)
    point_two = win.getMouse()
    point_two.draw(win)
    shape = Rectangle(point_one, point_two)
    shape.draw(win)

    xvalue_one = point_one.getX()
    yvalue_one = point_one.getY()
    xvalue_two = point_two.getX()
    yvalue_two = point_two.getY()

    length = abs(xvalue_one - xvalue_two)
    width = abs(yvalue_one - yvalue_two)
    perimeter = 2 * (length + width)
    area = (length * width)

    per_text = Text(Point(100,20), perimeter)
    per_text.draw(win)
    ar_text = Text(Point(30, 20), area)
    ar_text.draw(win)

    close_window = Text(inst_pt, "Click to close the window")
    close_window.draw(win)
    win.getMouse()
    win.close()

rectangle()




def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add two points: the first click is center and second is for circumference")
    instructions.draw(win)

    point_center = win.getMouse()
    point_center.draw(win)
    point_circumference = win.getMouse()
    point_circumference.draw(win)

    xvalue_center = point_center.getX()
    yvalue_center = point_center.getY()
    xvalue_circumference = point_circumference.getX()
    yvalue_circumference = point_circumference.getY()

    xequation = (xvalue_circumference - xvalue_center) ** 2
    yequation = (yvalue_circumference - yvalue_center) ** 2
    radius = sqrt(xequation + yequation)

    shape = Circle(point_center, radius)
    shape.draw(win)

    undo_text = instructions.undraw()
    ar_text = Text(inst_pt, radius)
    ar_text.draw(win)
    win.getMouse()

    undo_radius = ar_text.undraw()
    close_window = Text(inst_pt, "Click to close the window")
    close_window.draw(win)
    win.getMouse()
    win.close()

circle()



def pi():
    num = eval(input("Input number of terms to sum: "))
    num = 4
    den = 1
    switch = 1
    sum = 0
    for i in range(0, num):
        remainder = i % 2
        den = (den + 2 * remainder)
        switch = switch * (-1) # I think this is what you were saying in your explination on the board?
        pi = pi + (den * switch)
        #print(den, end="")

    # I know this is not correct, again, but I ran out of time
    # i was trying to get my sequence going to the denominator, then do the swtich to alternate, then sum it all
pi()



def main():
    squares()
    circle()
    rectangle()
    pi()

main()
