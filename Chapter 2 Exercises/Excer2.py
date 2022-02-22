# Exercise 2: Make it so the convert.py program does not immediately exit
#   when the code is done running. To do this, use an input statement at the end
#   of the program so that it pauses to give the user a chance to read the 
#   results. 

def main():
    print("This program converts the temperature from Celsius to Fahrenheit.")

    celsius = eval(input("What is the temperature in degrees Celsius?: "))
    fahrenheit = 9/5 * celsius + 32
    
    print("The temperature is ", fahrenheit, " degrees Fahrenheit.")

    input("Press the <Enter> key to quit.")

main()