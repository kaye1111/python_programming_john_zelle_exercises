# Exercise 8: Modify the futval.py to use the method of compounding interest quarterly.
#   Prompt the user for the yearly rate (rate), and the number of times that the interest is compounded
#   each year (periods). To compute the value in ten yers, the program will loop 10 * periods times and accrue 
#   rate/period interest on each iteration.

def main():
    print("This program calculates the future value of an investment with interest compounded", end=" ")
    print("quarterly.")

    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the yearly rate: "))
    periods = eval(input("Enter the number of times the interest is compounded each year: "))
    time = eval(input("Enter the span of time the investment is accruing interest: "))

    # nested loop
    for i in range(time):
        for j in range (periods):
            principal = principal * (1 + (rate/periods))

    print("The value in", time, "years is:", principal)


main()