# Write a program to calculate the area of a triangle given the length
#   of it's three sides.

import math

def main():
    print("The program calculates the area of a triangle.")

    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area of the triangle is", area)

main()