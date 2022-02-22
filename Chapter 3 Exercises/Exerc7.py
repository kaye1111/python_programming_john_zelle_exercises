# Write a program that accepts two points and determines the distance between them.

import math

def main(): 
    print("This program calculates the distance on a line between two points.")

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("The distance between these two points is", distance)

main()