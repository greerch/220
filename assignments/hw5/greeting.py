"""
Name: Caroline Greer
greeting.py

Problem: Write a 'Happy Valentine’s Day' card with a graphic

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

import time
from graphics import GraphWin, Point, Text, Polygon, Line, color_rgb

def main():
    win = GraphWin("Window 1", 700, 500)
    win.setCoords(0, 0, 10, 10)
    colors = color_rgb(255, 62, 150)

    heart = Polygon(Point(3, 5), Point(2.85, 5.9), Point(3.2, 6.4), Point(3.8, 6.5),
                    Point(4.3, 6.1),Point(4.5, 6), Point(4.8, 5.6), Point(5, 5.2),
                    Point(5.2, 5.6), Point(5.5, 6), Point(5.7, 6.1), Point(6.2, 6.5),
                    Point(6.8, 6.4), Point(7.15, 5.9), Point(7, 5),Point(5.15, 2))

    heart.setFill(colors)
    heart.draw(win)

    # arrow
    pnt1 = Point(2, 2)
    pnt2 = Point(3, 3)
    line = Line(pnt1, pnt2)
    line.setArrow('last')
    line.draw(win)

    # text
    text_point = Point(5, 8.5)
    text = Text(text_point, "Happy Valentines Day!")
    text.setSize(35)
    text.setStyle('bold italic')
    text.setTextColor(colors)
    text.draw(win)

    for _ in range(15):
        time.sleep(.1)
        line.move(.1, .1)
    line.setArrow('none')
    heart.setFill("red")

    for _ in range(4):
        time.sleep(.2)
        text.undraw()
        time.sleep(.2)
        text.draw(win)

    close_point = Point(2, 2)
    close = Text(close_point, "Click anywhere to close")
    close.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
