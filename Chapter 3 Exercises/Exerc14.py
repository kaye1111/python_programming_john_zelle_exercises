# Write a program that finds the average of a series of numbers entered by the user.
#   The program will first ask the user how many numbers there are.

def main():
    print("This program finds the average of a series of numbers.")

    amountNum = int(input("Enter how many numbers there are: "))
    sum = 0

    for i in range(amountNum):
        num = float(input("Enter a number: "))
        sum = sum + num

    avg = sum / amountNum

    print("The average of these numbers are", avg)

main()