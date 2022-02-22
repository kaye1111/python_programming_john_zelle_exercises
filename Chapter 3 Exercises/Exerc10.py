# Write a program to determine the length of a ladder required to reach
#   a certain height when leaned against a house. The height and the angle are given 
#   as inputs. Note: angle must be in radians. Prompt for an angle in degrees and convert.

import math

def main():
    
    print("This program determines the length of a ladder required to reach a given height", end=" ")
    print("when leaned against a house.")

    height = float(input("Enter the height of the house: "))
    angle = float(input("Enter the angle of the ladder in degrees: "))

    radians = (math.pi / 180) * angle
    length = height / math.sin(radians)

    print("The length of the ladder is", length)

main()