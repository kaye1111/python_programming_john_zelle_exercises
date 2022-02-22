# Modify the graphical future value program so that the input (principal and Apr) also are done
#   in a graphical fashion using Entry objects.

from graphics import *

def main():

    win = GraphWin("Investment Growth Chart", 600, 600)
    win.setCoords(-2, -500, 12, 13000)
    
    Text(Point(-1,0), " 0.0K").draw(win)
    Text(Point(-1, 2500), " 2.5K").draw(win)
    Text(Point(-1, 5000), " 5.0K").draw(win)
    Text(Point(-1, 7500), " 7.5K").draw(win)
    Text(Point(-1, 10000), "10.0K").draw(win)
    
    princText = Text(Point(3, 12000), "Initial Principal:")
    princText.setStyle("bold")
    princText.draw(win)
    aprText = Text(Point(2, 11500), "   Annualized Interest Rate:")
    aprText.setStyle("bold")
    aprText.draw(win)
    princInput = Entry(Point(6, 12000), 5)
    princInput.setText("0.0")
    princInput.draw(win)
    aprInput = Entry(Point(6, 11500), 5)
    aprInput.setText("0.0")
    aprInput.draw(win)

    button = Rectangle(Point(8, 11500), Point(10, 12000))
    button.draw(win)
    buttonText = Text(Point(9, 11750), "Enter")
    buttonText.draw(win)

    win.getMouse()

    buttonText.setText("Quit")
    principal = float(princInput.getText())
    apr = float(aprInput.getText())

    # Draw bar for Initial principal
    bar = Rectangle(Point(0,0), Point(1, principal))
    bar.setOutline("green4")
    bar.setFill("green1")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setOutline("green4")
        bar.setFill("green1")
        bar.setWidth(2)
        bar.draw(win)

    win.getMouse()
    win.close()

main()
