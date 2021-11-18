from graphics import Text, Rectangle


class Button:
    def __init__(self, shape, text):
        self.shape = shape
        self.text = text

    def get_label(self):
        return self.text

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, click_point):
        x_cord = click_point.getX()
        y_cord = click_point.getY()
        p1 = self.shape.getP1()
        p1x = p1.getX()
        p1y = p1.getY()
        p2 = self.shape.getP2()
        p2x = p2.getX()
        p2y = p2.getY()
        if p1x <= x_cord <= p2x and p1y <= y_cord <= p2y:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, text):
        self.text = text
