# Triangle Information. Same as the rectangle problem, but with three clicks from the vertices
#    of the triangle.

import math
from graphics import *

def main():

    win = GraphWin("Rectangle Information", 600, 600)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("gray")

    introRect = Rectangle(Point(-4.5, 8.5), Point(4.5, 9.5))
    introRect.setFill("white")
    introRect.draw(win)
    introText = Text(Point(0, 9), "Click anywhere to draw a Triangle")
    introText.draw(win)

    pointA = win.getMouse()
    pAx = pointA.getX()
    pAy = pointA.getY()

    pointCircA = Circle(Point(pAx, pAy), 0.1)
    pointCircA.setFill("red")
    pointCircA.draw(win)

    pointB = win.getMouse()
    pBx = pointB.getX()
    pBy = pointB.getY()

    pointCircB = Circle(Point(pBx, pBy), 0.1)
    pointCircB.setFill("red")
    pointCircB.draw(win)

    pointC = win.getMouse()
    pCx = pointC.getX()
    pCy = pointC.getY()

    pointCircA.undraw()
    pointCircB.undraw()
    triangleInput = Polygon(Point(pAx, pAy), Point(pBx, pBy), Point(pCx, pCy))
    triangleInput.setFill("cyan2")
    triangleInput.draw(win)

    outputBox = Rectangle(Point(5, 7.5), Point(9.5, 9.5))
    outputBox.setFill("white")
    outputBox.draw(win)

    lengthAB = math.sqrt((pAx + pBx) ** 2 + (pAy + pBy) ** 2)
    lengthAC = math.sqrt((pAx + pCx) ** 2 + (pAy + pCy) ** 2)
    lengthBC = math.sqrt((pBx + pCx) ** 2 + (pBy + pCy) ** 2)

    perimeter = lengthAB + lengthAC + lengthBC
    s = perimeter / 2
    area = math.sqrt(s * (s - lengthAB) * (s - lengthAC) * (s - lengthBC))

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