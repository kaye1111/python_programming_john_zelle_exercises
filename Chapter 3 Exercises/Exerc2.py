# Exercise 2: Write a program that calculates the cost per square inch of a circular pizza,
#   given its diameter and price.

import math

def main():

    print("This program calculates the cost per square inch of a circular pizza.")

    diameter = float(input("Enter the diameter of the pizza: "))
    price = float(input("Enter the price of the pizza: "))

    area = math.pi * (diameter / 2) ** 2
    costPerSqrInch = price / area

    print("The cost of the pizza is $", costPerSqrInch, "per square inch.")

main()