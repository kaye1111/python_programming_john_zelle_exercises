# Exercise 7: (Advanced) Modify the chaos program so it accepts two inputs and
#   prints a table with two columns similar to the one in Section 1.8. 
#       (Note: You will probably not be able to get the columns to line up nicely as
#        those in the example. Chapter 5 discusses how to print numbers with a fixed
#        number of decimal places.)

# import the tabulate module
from tabulate import tabulate

def main():
    
    print("This program illustrates a chaotic function.")

    x1 = eval(input("Enter a number between 0 and 1: "))
    x2 = eval(input("Enter another number between 0 and 1: "))

    # change the input into a string for the table headers
    x1_string = str(x1)
    x2_string = str(x2)

    # make a list for outputs of both inputs
    x1_output = []
    x2_output = []

    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x1_output.append(x1) # add the value to the list x1_output

    for j in range(10):
        x2 = 3.9 * x2 * (1 - x2)
        x2_output.append(x2) # add the value to the list x2_output

    # create the data
    data = [[None, x1_output[0], x2_output[0]],      # add the value at each position in the list
            [None, x1_output[1], x2_output[1]],      #   to the table
            [None, x1_output[2], x2_output[2]],
            [None, x1_output[3], x2_output[3]],      # Not sure how to better do this? lol
            [None, x1_output[4], x2_output[4]],
            [None, x1_output[5], x2_output[5]],
            [None, x1_output[6], x2_output[6]],
            [None, x1_output[7], x2_output[7]],
            [None, x1_output[8], x2_output[8]],
            [None, x1_output[9], x2_output[9]]]
    
    # Define header names
    col_names = ["input", x1_string, x2_string]

    # Display table
    print(tabulate(data, headers=col_names))


main()