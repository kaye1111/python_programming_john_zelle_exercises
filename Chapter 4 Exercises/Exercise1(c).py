# Alter the program from the last discussion question by:
#   Print a message on the window "Click again to quit" after the loop and wait
#   for a final click before closing the window.

from graphics import *

def main():

    win = GraphWin("Blah", 200, 200)
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

    quitText = Text(Point(100, 190), "Click again to exit.")
    quitText.draw(win)
    win.getMouse()
    win.close()

main()