# Write a program that approximates the value of pi by summing the terms of this
#   series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... The program should prompt the user for n,
#   the number of terms to sum, and then output the sum of the first n terms of the series. Have the program
#   subtract the approx. from the value of math.pi to see how accurate it is.

import math

def main():

    print("This program approximates the value of pi by summing the terms of the series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...")

    n = int(input("Enter the number of terms you wish to sum: "))
    sum1 = 0
    sum2 = 0
    sumF = 0

    for factors in range(1, n * 2, 4):
        sum1 = sum1 + 4 / factors

    for factors2 in range(3, n * 2, 4):
        sum2 = sum2 - 4 / factors2

    sumF = sum1 + sum2
    accur = math.pi - sumF

    print("The sum is", sumF)
    print("pi minus the sum is", accur)

main()