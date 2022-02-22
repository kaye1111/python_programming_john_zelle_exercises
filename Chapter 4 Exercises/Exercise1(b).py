# Alter the program from the last discussion by:
#   Have each successive click draw an additional square on the screen
#   (rather than moving the existing one.)

from graphics import *

def main():

    win = GraphWin()
    shape = Rectangle(Point(10,10), Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shapeCopy = shape.clone()
        shapeCopy.move(dx,dy)
        shapeCopy.draw(win)

    input("Press <Enter> to exit.")
    win.close()

main()