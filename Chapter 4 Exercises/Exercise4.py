# Write a program that draws a winter scene with a Christmas 
#   tree and a snowman.

from graphics import *

def main():

    win = GraphWin("Merry Christmas!!!", 320, 240)
    win.setCoords(0, 0, 320, 240)
    win.setBackground("gray")

    ground = Rectangle(Point(0,0), Point(320, 40))
    ground.setOutline("white")
    ground.setFill("white")
    ground.draw(win)

    # snowman
    bottomMan = Circle(Point(250, 70), 30)
    bottomMan.setFill("white")
    bottomMan.draw(win)

    middleMan = Circle(Point(250, 120), 25)
    middleMan.setFill("white")
    middleMan.draw(win)

    topMan = Circle(Point(250, 162), 22)
    topMan.setFill("white")
    topMan.draw(win)

    eye = Circle(Point(238, 167), 7)
    eye.setFill("black")
    eye.draw(win)
    eyeCopy = eye.clone()
    eyeCopy.move(22, 0)
    eyeCopy.draw(win)

    nose = Polygon(Point(250, 162), Point(250, 157), Point(239, 159.5))
    nose.setOutline("orange")
    nose.setFill("orange")
    nose.draw(win)

    button = Circle(Point(250, 132.5), 2)
    button.setFill("black")
    button.draw(win)
    buttonCopy1 = button.clone()
    buttonCopy1.move(0, -10)
    buttonCopy1.draw(win)
    buttonCopy2 = buttonCopy1.clone()
    buttonCopy2.move(0, -10)
    buttonCopy2.draw(win)

    hatBottom = Rectangle(Point(230, 178), Point(270, 183))
    hatBottom.setFill("black")
    hatBottom.draw(win)

    hatTop = Rectangle(Point(235, 183), Point(265, 200))
    hatTop.setFill("Black")
    hatTop.draw(win)

    # Christmas tree
    bark = Rectangle(Point(75, 40), Point(95, 60))
    bark.setOutline("brown")
    bark.setFill("brown")
    bark.draw(win)

    bottomTree = Polygon(Point(85, 100), Point(50, 60), Point(120, 60))
    bottomTree.setOutline("green")
    bottomTree.setFill("green")
    bottomTree.draw(win)

    middleTree = bottomTree.clone()
    middleTree.move(0, 25)
    middleTree.draw(win)

    topTree = middleTree.clone()
    topTree.move(0,25)
    topTree.draw(win)

    snowFlurry = Circle(Point(0,0), 3)
    snowFlurry.setOutline("white")
    snowFlurry.setFill("white")

    onText = Text(Point(160, 10), "Click around to make some snow flurries!")
    onText.draw(win)

    # Snow
    for i in range(10):
        p = win.getMouse()
        c = snowFlurry.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        snowFluCopy = snowFlurry.clone()
        snowFluCopy.move(dx, dy)
        snowFluCopy.draw(win)

    onText.setText("BEAUTIFUL! Click anywhere to quit.")
    onText.setFace("helvetica")
    onText.setTextColor("cyan3")
    onText.setStyle("bold")

    win.getMouse()
    win.close()

main()