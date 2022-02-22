# Write a program that draws 5 dice on the screen depicting a straight
# (1, 2, 3, 4, 5 or 2, 3, 4, 5, 6)

from graphics import *

# Recursive function call to draw dice. This doesn't presently operate properly if used
# def draw_dice(dice, limit, starting_value):
#     newDie = dice.clone()
#     newDie.move(2,0)
#     newDie.draw(win)
#     numCirc2Top = numCirc.clone()
#     numCirc2Top.move(1.75,0.25)
#     numCirc2Top.draw(win)
#     numCircBot = numCirc2Top.clone()
#     numCircBot.move(0.5, -0.5)
#     numCircBot.draw(win)
#     limit = limit -1
#     starting_value = starting_value + 1

#     draw_dice(newDie, limit, starting_value) 

def main():

    win = GraphWin("Five Dice", 320, 240)
    win.setCoords(0.0, 0.0, 7.0, 5.0)
    win.setBackground("gray")

    # Dice with one
    diceOne = Rectangle(Point(1, 3), Point(2, 4))
    diceOne.setFill("white")
    diceOne.draw(win)
    numCirc = Circle(Point(1.5, 3.5), 0.10)
    numCirc.setFill("black")
    numCirc.draw(win)

    # Dice with a two
    diceTwo = diceOne.clone()
    diceTwo.move(2,0)
    diceTwo.draw(win)
    numCirc2Top = numCirc.clone()
    numCirc2Top.move(1.75,0.25)
    numCirc2Top.draw(win)
    numCircBot = numCirc2Top.clone()
    numCircBot.move(0.5, -0.5)
    numCircBot.draw(win)

    # Dice with a three
    diceThree = diceTwo.clone()
    diceThree.move(2,0)
    diceThree.draw(win)
    numCirc3Top = numCirc2Top.clone()
    numCirc3Top.move(2.5,0)
    numCirc3Top.draw(win)
    numCirc3Bot = numCircBot.clone()
    numCirc3Bot.move(1.5, 0)
    numCirc3Bot.draw(win)
    numCirc3Mid = numCirc3Bot.clone()
    numCirc3Mid.move(0.25, 0.25)
    numCirc3Mid.draw(win)


    # Dive with a four
    diceFour = diceOne.clone()
    diceFour.move(1,-2)
    diceFour.draw(win)
    numCirc4TopL = numCirc.clone()
    numCirc4TopL.move(0.75, -1.75)
    numCirc4TopL.draw(win)
    numCirc4TopR = numCirc4TopL.clone()
    numCirc4TopR.move(0.5, 0)
    numCirc4TopR.draw(win)
    numCirc4BotL = numCirc4TopL.clone()
    numCirc4BotL.move(0, -0.5)
    numCirc4BotL.draw(win)
    numCirc4BotR = numCirc4BotL.clone()
    numCirc4BotR.move(0.5, 0)
    numCirc4BotR.draw(win)

    # Dice with a five
    diceFive = diceFour.clone()
    diceFive.move(2,0)
    diceFive.draw(win)
    num5TopL, num5TopR, num5BotL, num5BotR = numCirc4TopL.clone(), numCirc4TopR.clone(), numCirc4BotL.clone(), numCirc4BotR.clone()
    num5TopL.move(2, 0)
    num5TopR.move(2, 0)
    num5BotL.move(2, 0)
    num5BotR.move(2, 0)
    num5Mid = num5BotL.clone()
    num5Mid.move(0.25, 0.25)
    num5TopL.draw(win)
    num5TopR.draw(win)
    num5BotL.draw(win)
    num5BotR.draw(win)
    num5Mid.draw(win)

    quitText = Text(Point(3.5, 0.20), "Click anywhere to quit.")
    quitText.draw(win)
    win.getMouse()
    win.close()

main()