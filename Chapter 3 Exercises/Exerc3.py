# Write a program that computes the molecular weight of a carbohydrate 
#   in grams per mole based on the number of hydrogen, carbon, and oxygen attoms in 
#   the molecule.

import math

def main():
    print("This program computes the molecular weight of a carbohydrate.")

    hydrogen = int(input("Enter the number of hydrogen atoms: "))
    carbon = int(input("Enter the number of carbon atoms: "))
    oxygen = int(input("Enter the number of oxygen atoms: "))

    molWeight = hydrogen * (1.00794) + carbon * (12.0107) + oxygen * (15.9994)

    print("The molecular weight is", molWeight, "g/mol")

main()