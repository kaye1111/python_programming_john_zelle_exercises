# Write a program to find the sum of the cubes of the first n natural
#   numbers where the value of n is provided by the user.

def main():

    print("This program finds the sum of the cubes of the first n natural numbers.")

    n = int(input("Enter the value of n: "))
    sum = 0

    for factor in range(1, n + 1, 1):
        sum = sum + (factor ** 3)

    print("The sum is", sum)

main()