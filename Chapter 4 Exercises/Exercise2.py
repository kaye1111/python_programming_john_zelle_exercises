# An archery Target consists of a central circle of yellow surrounded by concentric
#   rings of red, blue, black, and white. Each ring has the same width, which is the 
#   same as the radius of the yellow circle. Write a program that draws such a target.
#   Hint: Objects drawn later will appear on top of objects drawn earlier.

# This could be nicer-looking with additional functions, but I'm sticking with this since
#   I have not gotten to the functions portion of the book yet. 

from graphics import *

def main():

    win = GraphWin("An Archery Target")
    win.setCoords(0, 0, 100, 100)
    win.setBackground("gray")

    whiteCircle = Circle(Point(50,50), 25)
    whiteCircle.setOutline("white")
    whiteCircle.setFill("white")
    whiteCircle.draw(win)

    blackCircle = Circle(Point(50,50), 20)
    blackCircle.setOutline("black")
    blackCircle.setFill("black")
    blackCircle.draw(win)

    blueCircle = Circle(Point(50,50), 15)
    blueCircle.setOutline("blue")
    blueCircle.setFill("blue")
    blueCircle.draw(win)

    redCircle = Circle(Point(50,50), 10)
    redCircle.setOutline("red")
    redCircle.setFill("red")
    redCircle.draw(win)

    centerCircle = Circle(Point(50,50), 5)
    centerCircle.setOutline("yellow")
    centerCircle.setFill("yellow")
    centerCircle.draw(win)

    quitText = Text(Point(50, 10), "Click again to exit.")
    quitText.draw(win)
    win.getMouse()
    win.close()

main()