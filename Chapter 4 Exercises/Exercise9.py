# Rectangle Information. This program displays information about a rectangle drawn
#   by the user.
#   Input: Two mouse clicks for the opposite corners of a rectangle.
#   Output: Draw the rectangle. Print the perimeter and area of the rectangle.

import math
from graphics import *

def main():

    win = GraphWin("Rectangle Information", 600, 600)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("gray")
    
    introRect = Rectangle(Point(-4.5, 8.5), Point(4.5, 9.5))
    introRect.setFill("white")
    introRect.draw(win)
    introText = Text(Point(0, 9), "Click anywhere to draw a Rectangle.")
    introText.draw(win)
    
    point1 = win.getMouse()
    p1x = point1.getX()
    p1y = point1.getY()

    pointCirc1 = Circle(Point(p1x, p1y), 0.1)
    pointCirc1.setFill("red")
    pointCirc1.draw(win)

    point2 = win.getMouse()
    p2x = point2.getX()
    p2y = point2.getY()

    pointCirc1.undraw()
    rectangleInput = Rectangle(Point(p1x, p1y), Point(p2x, p2y))
    rectangleInput.setFill("cyan2")
    rectangleInput.draw(win)

    outputBox = Rectangle(Point(5, 7.5), Point(9.5, 9.5))
    outputBox.setFill("white")
    outputBox.draw(win)

    length = abs(p1y - p2y)
    width = abs(p1x - p2x)
    area = length * width
    perimeter = 2 * (length + width)

    areaText = Text(Point(7, 9), "Area:")
    areaText.setStyle("bold italic")
    areaText.setSize(11)
    areaText.draw(win)
    perimeterText = Text(Point(6.5, 8), "Perimeter:")
    perimeterText.setStyle("bold italic")
    perimeterText.setSize(11)
    perimeterText.draw(win)

    areaOutput = Text(Point(8.5, 9), round(area, 2))
    areaOutput.setTextColor("red")
    areaOutput.setStyle("bold")
    areaOutput.setSize(11)
    areaOutput.draw(win)
    perimeterOutput = Text(Point(8.5, 8), round(perimeter, 2))
    perimeterOutput.setTextColor("red")
    perimeterOutput.setStyle("bold")
    perimeterOutput.setSize(11)
    perimeterOutput.draw(win)

    introText.setText("Click anywhere to quit.")
    introText.setTextColor("red")
    introText.setStyle("bold")

    win.getMouse()
    win.close()

main()