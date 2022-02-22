# A program that determines the distance to a lightning strike based on the time elapsed between the flash
#   and sound of thunder. The speed of sound is appr. 1100 ft/sec and 1 mile
#   is 5280 ft.

def main():

    print("This program is to determine the distance to a lightning strike.")

    time = float(input("Enter the time elapsed between the flash and the sound of the thunder in seconds: "))

    distance = (time * 1100) / 5280

    print("The lightning strike is", distance, "miles away.")

main() 
