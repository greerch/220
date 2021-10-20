"""
Name: Caroline Greer
vigenere.py

Problem: write a program to implement the Vigenere cipher

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from graphics import GraphWin, Entry, Text, Point, Rectangle

def encode(message, keyword):
    win = GraphWin("Vigenere", 700, 500)
    win.setCoords(0, 0, 10, 10)

    message_label = Text(Point(2.5, 8, ), "Message to code")
    message_input = Entry(Point(4.8, 8), 30)
    message_label.draw(win)
    message_input.draw(win)

    keyword_label = Text(Point(2.5, 7, ), "Keyword")
    keyword_input = Entry(Point(4.1, 7), 15)
    keyword_label.draw(win)
    keyword_input.draw(win)

    encode_text = Text(Point(5, 4), "Encode")
    encode_text.setSize(15)
    botton_outline = Rectangle(Point(4, 5), Point(6, 3))
    encode_text.draw(win)
    botton_outline.draw(win)

    output_text = Text(Point(5, 2), " ")
    output_text.draw(win)

    win.getMouse()

    message = message_input.getText()
    message = message.lower()
    keyword = keyword_input.getText()
    encoded_message = ""
    for i in range(len(message)):
        num = ord(message[i])
        key = ord(keyword[i % len(keyword)])
        shift = num + key
        encoded_message = encoded_message + chr(shift)
    return encoded_message

    win.getMouse()

    encode_text.undraw()
    botton_outline.undraw()
    resulting_message = Text(Point(5, 3, ), "Resulting Message")
    resulting_message.draw(win)
    output_text.setText(encoded_message)
    close_message = Text(Point(5, 1, ), "Click anywhere to close")
    close_message.draw(win)


def main():
    win = GraphWin("Vigenere", 700, 500)
    win.setCoords(0, 0, 10, 10)
    encode('This program will be great', 'python')
    win.getMouse()
    win.close()

if __name__ == '__main__':

    main()