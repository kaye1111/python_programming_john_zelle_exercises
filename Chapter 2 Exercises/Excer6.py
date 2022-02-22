# Exercise 6: Modify the futval.py program (Section 2.7) so the number 
#   of years for the investment is also user input. Change the final message 
#   to reflect the correct number of years.

def main():
    print("This program calculates the future value", end=" ")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as a decimal: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is:", principal)

main()