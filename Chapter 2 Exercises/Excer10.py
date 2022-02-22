# Exercise 10: Write a program that converts distances measured in
#   kilometers to miles. One kilometer is approximately 0.62 miles.

def main():

    print("This program converts kilometers to miles.")

    kilometers = eval(input("Enter a distance in kilometers: "))
    miles = kilometers * 0.62

    print(kilometers, "kilometers is", miles, "miles.")

main()