# Write a program that prompts the user for a 4-digit year and then outputs the 
#    value of the epact.

def main():
    print("This program show the value of the epact of a specified year.")

    year = int(input("Enter a 4-digit year: "))

    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    print("The value of the epact is", epact)

main()