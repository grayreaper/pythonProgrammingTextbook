# feetToMilesConvert.py
#   This program converts feet to miles
#   BY: Gray Reaper

def main():
    print("This Program converts a distance in feet to miles")
    feet = eval(input("Enter the distance in feet: "))
    miles = feet / 5280
    print("The distance in miles is", miles)
    input("Press ENTER to exit.")

main()
