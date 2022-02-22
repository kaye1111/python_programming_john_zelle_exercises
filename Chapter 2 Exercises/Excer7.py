# Exercise 7: You have an investment plan where you invest a certain fixed amount every year. 
#   Modify futval.py to compute the total accumulation of your investment. The inputs 
#   to the program will be the amount to invest each year, the interest rate, and the number 
#   of years for the investment.

def main():
    print("This program calculates the future value", end=" ")
    print("of an investment.")

    principal = eval(input("Enter the fixed amount to invest each year: "))
    apr = eval(input("Enter the annual interest rate as a decimal: "))
    years = eval(input("Enter the number of years: "))
    initialPrincipal = principal

    for i in range(years):
        principal = principal * (1 + apr)
        principal = principal + initialPrincipal

    print("The value in", years, "years is:", principal)

main()