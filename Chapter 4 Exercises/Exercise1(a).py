# Alter the program from the last discussion question in the following ways:
#   a.) Make it draw squares instead of circles.

from graphics import *

def main():

    win = GraphWin("Drawing a Square")
    shape = Rectangle(Point(10,10), Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)

    input("Press <Enter> to close.")
    win.close()

main()