# Write a program that draws some sort of face.

from graphics import *

def main():

    win = GraphWin("A Smiley Face")
    win.setCoords(0, 0, 100, 100)

    eyeWhite = Circle(Point(30,70), 10)
    eyeWhite.setFill("white")
    eyeWhite.draw(win)
    eyeWCopy = eyeWhite.clone()
    eyeWCopy.move(40,0)
    eyeWCopy.draw(win)

    pupil = Circle(Point(30,70), 4)
    pupil.setFill("red")
    pupil.setOutline("yellow")
    pupil.draw(win)
    pupilCopy = pupil.clone()
    pupilCopy.move(40,0)
    pupilCopy.draw(win)

    nose = Polygon(Point(50,55), Point(45,45), Point(55,45))
    nose.draw(win)

    mouth = Line(Point(30,35), Point(70,35))
    mouth.draw(win)

    quitText = Text(Point(50,15), "Click again to exit...")
    quitText2 = Text(Point(50,5), "OR ELSE.")
    quitText2.setTextColor("red")
    quitText2.setStyle("bold")
    quitText.draw(win)
    quitText2.draw(win)

    win.getMouse()
    win.close()

main()

