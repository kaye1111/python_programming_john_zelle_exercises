# Write a program that implements Newton's Method for guessing a square root. The program
#   should prompt the user for the value to find the square root of (x) and the number of times
#   to improve the guess. Starting with a guess value of x / 2, your program should loop the 
#   specified number of times applying Newton's method and report the final value of guess. Also 
#   subtract your estimate from the value of math.sqrt(x) to show how close it is.

import math

def main():

    print("This program implements Newton's Method for guessing the square root of a number.")

    x = float(input("Enter the value you would like the guess the square root of: "))
    repeat = int(input("Enter the number of times you would like to improve the guess: "))
    guess = x / 2
    sqrootx = math.sqrt(x)

    for i in range(repeat):
        guess = (guess + (x / guess)) / 2

    diffGuess = sqrootx - guess

    print("The final guessed value is: ", guess)
    print("The actual square root of", x, "is", sqrootx, ", and the difference between the actual square root", end = " ")
    print("and the guessed square root is: ", diffGuess)

main()