# Two points in a plane are specified using the coordinates (x1, y1) and (x2, y2).
#   Write a program that calculates the slope of a line through two (non-vertical) points
#   entered by the user.

def main(): 
    print("This program calculates the slope of a line through two points.")

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    slope = (y2 - y1) / (x2 - x1)

    print("The slope of the line is", slope)

main()