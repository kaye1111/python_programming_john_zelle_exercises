# Write a program to find the sum of the first n natural numbers, where the
#   value of n is provided by the user.

def main():
    print("This program finds the sum of the first n natural numbers.")

    n = int(input("Enter the value for n: "))
    sum = n

    for factor in range(1, n, 1):
        sum = sum + factor

    print("The sum is", sum)

main()
