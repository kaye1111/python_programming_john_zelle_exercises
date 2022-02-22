# Five-click House. Write a program that allows the user to draw a simple house using
#   five mouse clicks. First two clicks will be the opposite corners of the rectangular frame
#   of the house. Third click will indicate the center of the top edge of a rectangular door.
#   The door should have a total width that is 1/5 of the width of the house frame.
#   the sides of the door should extend from the corners of the top down to the bottom
#   of the frame. The fourth click will indicate the center of a square window.
#   The window is half as wide as the door. The last click will indicate the peak
#   of the roof. The edges of the roof will extend from the point at the peak to the 
#   corners of the top edge of the house frame.

from graphics import *

def main():

    win = GraphWin("A Simple House", 600, 600)
    win.setCoords(-10, -10, 10, 10)

    titleText = Text(Point(0, 9), "Click five times to make a house.")
    titleText.draw(win)
    addendumText = Text(Point(0, 8.25), "(Make sure your second click is below your first click.)")
    addendumText.setTextColor("red4")
    addendumText.setSize(11)
    addendumText.draw(win)

    framePointOne = win.getMouse()
    frameP1x = framePointOne.getX()
    frameP1y = framePointOne.getY()
    locatorCirc = Circle(Point(frameP1x, frameP1y), 0.1)
    locatorCirc.setFill("red")
    locatorCirc.draw(win)

    framePointTwo = win.getMouse()
    frameP2x = framePointTwo.getX()
    frameP2y = framePointTwo.getY()
    
    locatorCirc.undraw()
    
    houseFrame = Rectangle(Point(frameP1x, frameP1y), Point(frameP2x, frameP2y))
    houseFrame.draw(win)

    doorPoint = win.getMouse()
    doorPointx = doorPoint.getX()
    doorPointy = doorPoint.getY()

    doorWidth = (abs(frameP1x - frameP2x)) * 1/5
    doorPointLeft = doorPointx - (doorWidth / 2)
    doorPointRight = doorPointx + (doorWidth / 2)

    door = Rectangle(Point(doorPointLeft, doorPointy), Point(doorPointRight, frameP2y))
    door.draw(win)

    windowCenter = win.getMouse()
    windowX = windowCenter.getX()
    windowY = windowCenter.getY()

    windowWidth = doorWidth / 2
    windowPointOneX = windowX - (windowWidth / 2)
    windowPointOneY = windowY + (windowWidth / 2)
    windowPointTwoX = windowX + (windowWidth / 2)
    windowPointTwoY = windowY - (windowWidth / 2)

    window = Rectangle(Point(windowPointOneX, windowPointOneY), Point(windowPointTwoX, windowPointTwoY))
    window.draw(win)

    roofPeak = win.getMouse()
    roofPeakX = roofPeak.getX()
    roofPeakY = roofPeak.getY()

    roofPointRight = Point(frameP1x, frameP1y)
    roofPointLeft = Point(frameP2x, frameP1y)
    roof = Polygon(Point(roofPeakX, roofPeakY), roofPointRight, roofPointLeft)
    roof.draw(win)

    addendumText.undraw()
    titleText.setText("Click anywhere to quit.")
    titleText.setTextColor("red")
    titleText.setStyle("bold")

    win.getMouse()
    win.close()

main()