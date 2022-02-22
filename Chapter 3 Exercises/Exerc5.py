# A coffee shop sells coffee at $10.50 a pound plus the cost of shipping. 
#   Each order ships for $0.86 per pound + $1.50 fixed cost for overhead.
#   Write a program that calculates the cost of an order.

def main():
    print("This program calculates the cost of a coffee order.")

    weight = float(input("Enter the weight of coffee in pounds: "))

    cost = weight * (10.50 + 0.86) + 1.50

    print("The cost of", weight, "pounds of coffee is $", cost)

main()