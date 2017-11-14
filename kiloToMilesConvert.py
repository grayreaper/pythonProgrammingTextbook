# kiloToMilesConvert.py
#   This program converts kilometers to miles.
# BY: Gray Reaper

def main():
    print("This program converts a distance in kilometers to miles.")

    kilo = eval(input("Enter the distance in kilometers: "))
    miles = kilo * 0.62137
    print("The distance in miles is", miles)
    input("Press ENTER to exit")

main()
