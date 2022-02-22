# Exercise 9: Write a program that converts from Fahrenheit to Celsius.

def main():
    
    print("This program converts temperatures from Fahrenheit to Celsius.")

    fahrenheit = eval(input("Enter a temperature in degrees Fahrenheit: "))
    celsius = 5/9 * (fahrenheit - 32)

    print("The temperature", fahrenheit, "degrees Fahrenheit is", celsius, "degrees Celsius.")

main()