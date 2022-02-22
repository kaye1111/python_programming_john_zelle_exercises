# Line Segment Information: This program allows the user to draw a line segment 
#    and then displays some graphical and textual information about the line segment.
#   Inputs: Two mouse clicks for the end point of the line segment.
#   Outputs: Draw the midpoint of the segment in cyan.
#               Draw the line.
#               Print the length and the slope of the line.

from graphics import *
import math

def main():

    win = GraphWin("Line Segment Information", 600, 600)
    win.setCoords(-10, -10, 10, 10)

    greetingText = Text(Point(0, 9), "Click anywhere to create a line.")
    greetingText.draw(win)

    point1 = win.getMouse()
    p1x = point1.getX()
    p1y = point1.getY()

    point1Circ = Circle(Point(p1x, p1y), 0.1)
    point1Circ.setOutline("red")
    point1Circ.setFill("red")
    point1Circ.draw(win)

    point2 = win.getMouse()
    p2x = point2.getX()
    p2y = point2.getY()

    point2Circ = Circle(Point(p2x, p2y), 0.1)
    point2Circ.setOutline("red")
    point2Circ.setFill("red")
    point2Circ.draw(win)

    inputLine = Line(Point(p1x, p1y), Point(p2x, p2y))
    inputLine.draw(win)

    point1Circ.setOutline("black")
    point1Circ.setFill("black")
    point2Circ.setOutline("black")
    point2Circ.setFill("black")

    dxMid = (p1x + p2x) / 2
    dyMid = (p1y + p2y) / 2

    midPoint = Circle(Point(dxMid, dyMid), 0.1)
    midPoint.setOutline("cyan4")
    midPoint.setFill("cyan2")
    midPoint.draw(win)

    dx = p2x - p1x
    dy = p2y - p1y
    slope = dy / dx
    length = math.sqrt((dx ** 2) + (dy ** 2))

    slopeText = Text(Point(7.25, 9), "Slope = ")
    slopeText.setStyle("bold italic")
    slopeText.setSize(11)
    slopeText.draw(win)

    lengthText = Text(Point(7, 8.25), " Length =")
    lengthText.setStyle("bold italic")
    lengthText.setSize(11)
    lengthText.draw(win)

    slopeOutput = Text(Point(9, 9), round(slope, 2))
    slopeOutput.setTextColor("red")
    slopeOutput.setSize(11)
    slopeOutput.draw(win)

    lengthOutput = Text(Point(9, 8.25), round(length, 2))
    lengthOutput.setTextColor("red")
    lengthOutput.setSize(11)
    lengthOutput.draw(win)

    greetingText.setText("Click anywhere to quit.")
    greetingText.setTextColor("red3")

    win.getMouse()
    win.close()

main()
