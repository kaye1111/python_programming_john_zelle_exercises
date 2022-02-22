# Write a program that computes the intersection of a circle with a horizontal line and displays the
#   the information textually and graphically

from graphics import *
import math

def main():

    win = GraphWin("Circle Intersection", 500, 500)
    win.setCoords(-10, -10, 13, 13)

    radiusText = Text(Point(-6, 12), "  Radius:")
    radiusText.setStyle("bold")
    radiusText.draw(win)
    yText = Text(Point(-6.5, 11), "Y-intercept:")
    yText.setStyle("bold")
    yText.draw(win)

    radiusInput = Entry(Point(-3, 12), 5)
    radiusInput.setText("0.0")
    radiusInput.draw(win)
    yInput = Entry(Point(-3, 11), 5)
    yInput.setText("0.0")
    yInput.draw(win)

    button = Rectangle(Point(0, 10.75), Point(3, 12.25))
    button.draw(win)
    buttonText = Text(Point(1.5, 11.5), "Draw")
    buttonText.setStyle("bold")
    buttonText.setTextColor("blue")
    buttonText.draw(win)

    outputTitle = Text(Point(8, 12), "Points of Intersection:")
    outputTitle.setStyle("bold")
    outputTitle.draw(win)
    
    xEqualsText = Text(Point(7, 11), "x =")
    xEqualsText.setStyle("bold italic")
    xEqualsText.draw(win)

    outputText = Text(Point(9, 11), " ")
    outputText.setTextColor("red")
    outputText.draw(win)

    win.getMouse()

    buttonText.setText("Quit")
    buttonText.setTextColor("red")

    radius = float(radiusInput.getText())
    yInt = float(yInput.getText())

    circle = Circle(Point(0,0), radius)
    circle.draw(win)

    yLine = Line(Point(-9, yInt), Point(9, yInt))
    yLine.draw(win)

    x = math.sqrt((radius ** 2) - (yInt ** 2))

    xIntCircP = Circle(Point(x, yInt), 0.1)
    xIntCircP.setOutline("red")
    xIntCircP.setFill("red")
    xIntCircP.draw(win)

    xIntCircN = Circle(Point(-x, yInt), 0.1)
    xIntCircN.setOutline("red")
    xIntCircN.setFill("red")
    xIntCircN.draw(win)

    xInterc = round(x, 1), - round(x, 1)

    outputText.setText(xInterc)

    win.getMouse()
    win.close()

main()
