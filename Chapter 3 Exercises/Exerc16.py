# A Fibonacci sequence is a sequence of numbers where each successive number is the sum of 
#   the previous two. The calssic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13, ... Write a program
#   that computes the nth Fibonacci number where n is a value input by the user.

def main():

    print("This program computes the nth Fibonacci number.")

    n = int(input("Enter the value of n: "))
    current = 1
    previous = 0
    temp = 0

    for i in range(n-1):
        temp = current
        current = current + previous
        previous = temp

    print("The Fibonacci number at the", n, "th place is", current)

main()
