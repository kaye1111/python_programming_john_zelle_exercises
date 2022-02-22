# Exercise 5: Modify the convert.py program (Section 2.2) so it computes and 
#   prints a table of celsius temperatures and the Fahrenheit equivalents every 
#   10 degrees from 0C to 100C.

# Import tabulate module
from tabulate import tabulate 

def main():

    # assign the variable before the loop
    celsius = 0
    fahrenheit = 0

    # Create lists for the values to form the table
    CelsiusData = []
    FahrData = []
    ForI = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for i in ForI:
        celsius = i
        fahrenheit = 9/5 * celsius + 32
        CelsiusData.append(celsius)     # add values to the list
        FahrData.append(fahrenheit)

    data = [[CelsiusData[0], FahrData[0]],      # Once again, not sure how to do this better,
            [CelsiusData[1], FahrData[1]],      #   if there is a way.
            [CelsiusData[2], FahrData[2]],
            [CelsiusData[3], FahrData[3]],
            [CelsiusData[4], FahrData[4]],
            [CelsiusData[5], FahrData[5]],
            [CelsiusData[6], FahrData[6]],
            [CelsiusData[7], FahrData[7]],
            [CelsiusData[8], FahrData[8]],
            [CelsiusData[9], FahrData[9]],
            [CelsiusData[10], FahrData[10]]]


    # set header names
    col_names = ["Celsius", "Fahrenheit"]

    print(tabulate(data, headers = col_names))


main()