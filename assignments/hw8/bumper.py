"""
Name: Caroline Greer
bumper.py

Problem: write a program that simulates bumper cars

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
import time
from random import *
import math
from graphics import *

def main():
    win = GraphWin("Bumper", 700, 500)
    circle_a = Circle(Point(300, 300), 20)
    red = abs(get_random(255))
    green = abs(get_random(255))
    blue = abs(get_random(255))
    colors = color_rgb(red, green, blue)
    circle_a.setFill(colors)
    circle_a.draw(win)

    circle_b = Circle(Point(200, 200), 20)
    red_b = abs(get_random(255))
    green_b = abs(get_random(255))
    blue_b = abs(get_random(255))
    colors_b = color_rgb(red_b, green_b, blue_b)
    circle_b.setFill(colors_b)
    circle_b.draw(win)

    x = get_random(5)
    y = get_random(5)
    a = get_random(5)
    b = get_random(5)

    while True:
        time.sleep(.005)
        circle_a.move(x, y)
        circle_b.move(a, b)
        if hit_vertical(circle_b, win):
            a = -a
            circle_b.move(a, b)
        if hit_horizontal(circle_a, win):
            y = -y
            circle_a.move(x, y)
        if hit_vertical(circle_a, win):
            x = -x
            circle_a.move(x, y)
        if hit_horizontal(circle_b, win):
            b = -b
            circle_b.move(a, b)
        if did_collide(circle_a, circle_b):
            a = -a
            b = -b
            x = -x
            y = -y
            circle_a.move(a, b)
            circle_b.move(x, y)


def get_random(move_amount):
    move = randint(-move_amount, move_amount)
    return move


def did_collide(circle_a, circle_b):
    center_a = circle_a.getCenter()
    center_b = circle_b.getCenter()
    circle_a_x_value = center_a.getX()
    circle_a_y_value = center_a.getY()
    circle_b_x_value = center_b.getX()
    circle_b_y_value = center_b.getY()
    circle_a_radius = circle_a.getRadius()
    circle_b_radius = circle_b.getRadius()
    distance_ex = (((circle_a_x_value - circle_b_x_value) ** 2) +
                  ((circle_a_y_value - circle_b_y_value) ** 2))
    distance = math.sqrt(distance_ex)
    tot_radius = circle_a_radius + circle_b_radius
    return distance <= tot_radius



def hit_horizontal(circle, win):
    center = circle.getCenter()
    circle_value = center.getY() + circle.getRadius()
    circle_value_neg = center.getY() - circle.getRadius()
    return circle_value >= win.height or circle_value_neg <= 0


def hit_vertical(circle, win):
    center = circle.getCenter()
    circle_value = center.getX() + circle.getRadius()
    circle_value_neg = center.getX() - circle.getRadius()
    return circle_value >= win.width or circle_value_neg <= 0

if __name__ == "__main__":
    main()
