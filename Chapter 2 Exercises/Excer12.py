# Exercise 12: Write an interactive Python calculator program. It should allow the user to 
#   type a mathematical expression, and then print the value of the expression.
#   Include a loop so the user can perform many calculations, say, up to 100. 


def main():

    print("This program acts as a calculator.")

    for i in range(100):
        equation = eval(input("Enter an equation: "))
        print("Answer: ", equation)

main()