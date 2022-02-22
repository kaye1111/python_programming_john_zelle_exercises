# Exercise 1: A user friendly program should print an introduction that tells
#   the user what the program does. Modify the convert.py program from Section
#   2.2 to print an introduction.


def main():
    print("This program converts the temperature from Celsius to Fahrenheit.")

    celsius = eval(input("What is the temperature in degrees Celsius?: "))
    fahrenheit = 9/5 * celsius + 32
    
    print("The temperature is ", fahrenheit, " degrees Fahrenheit.")

main()
