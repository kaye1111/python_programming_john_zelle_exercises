# Exercise 11: Write a program to perform a unit conversion of your own choosing.
#   Make sure that the program prints an intro that explains what it does.
#   The conversion I chose: inches to centimeters

def main():

    print("This program converts inches to centimeters.")

    inch = eval(input("Enter a distance in inches: "))
    centimeter = inch * 2.54

    print(inch, "inches is", centimeter, "centimeters.")

main()