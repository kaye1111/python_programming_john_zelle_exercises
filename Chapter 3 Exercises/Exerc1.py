# Exercise 1: Write a program to calculate the volume and surface area of a
#   sphere from its radius, given as input. 

# import math module
import math

def main():

    print("This program calculates the volume and surface area of a sphere from the radius.")

    radius = float(input("Enter the radius of a sphere: "))

    volume = 4/3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2

    print("The volume of the sphere is", volume, "and the surface area of the sphere is", area)

main()