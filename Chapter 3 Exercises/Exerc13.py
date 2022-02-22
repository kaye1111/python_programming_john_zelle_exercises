# Write a prorgam to sum a series of numbers entered by the user. The program should first
#   prompt the user for how many numbers are to be summed. The program should then prompt the user 
#   for each of the numbers in turn and print out a total sum after all the numbershave
#   been entered. Hint: use an input statement in the body of the loop.

def main():
    print("This program gives the sum of an input of numbers.")

    numbers = int(input("Enter how many numbers are to be given: "))
    sum = 0

    for i in range(numbers):
        inNum = int(input("Enter a number: "))
        sum = sum + inNum

    print("The sum of these numbers is", sum)

main()