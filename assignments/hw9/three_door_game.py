from graphics import GraphWin, Point
from random import randint
from hw9.button import *

"""
Name: Caroline Greer
three_door_game.py

Problem: write a program that simulates a secret door chosen and being opened 

Certification of Authenticity:
I certify that this assignment is my work and I got assistance at the CSCI Lab 
"""


def main():

    win = GraphWin("Three Door Game", 600, 400)
    win.setCoords(0, 0, 10, 10)

    text_one = Point(5, 8.5)
    text_two = Point(5, 2)
    intro_text = Text(text_one, "Choose which door is the secret door")
    direction_text = Text(text_two, "Click on one of the doors")

    rec_one = Rectangle(Point(1.5, 4), Point(3.5, 6))
    rec_two = Rectangle(Point(4, 4), Point(6, 6))
    rec_three = Rectangle(Point(6.6, 4), Point(8.5, 6))

    door_one = Button(rec_one, Text(rec_one.getCenter(), "Door one"))
    door_two = Button(rec_two, Text(rec_two.getCenter(), "Door two"))
    door_three = Button(rec_three, Text(rec_three.getCenter(), "Door three"))

    door_one.draw(win)
    door_two.draw(win)
    door_three.draw(win)

    intro_text.draw(win)
    direction_text.draw(win)

# get a secret door
    options = [door_one, door_two, door_three]
    door_opened = randint(0, 2)


# check to see if it clicked
    click = win.getMouse()
    for i in range(3):
        if options[i].is_clicked(click):
            if i == door_opened:
                options[i].color_button("green")
                intro_text.undraw()
                direction_text.undraw()
                yay_text = Text(text_one, "Woot Woot!")
                yay_text.draw(win)
                close_text = Text(text_two, "Click to close")
                close_text.draw(win)
                win.getMouse()
                win.close()
            if i != door_opened:
                options[i].color_button("red")
                intro_text.undraw()
                direction_text.undraw()
                boo_text = Text(text_one, "loser loser")
                boo_text.draw(win)
                close_text = Text(text_two, "Click to close")
                close_text.draw(win)
                win.getMouse()
                win.close()


if __name__ == '__main__':
    main()
