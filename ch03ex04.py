# ch03ex04.py
#   This program calculate the distance to a lightning strike based on time lapsed between flash and sound
#   By: Gray Reaper

def main():

    print("This program calculates the distance to a lightning strike based on")
    print("the amount of time lapse between flash and sound of thunder.")
    print()
    done = "y"



    while done == "y":
        time = float(input("How many seconds passed between flash and sound? "))
        distance = (time * 1100.0) / 5280.0



        print("The lightning strike was", distance,"miles away.")
        print()
        done = input("Would you like to calculate another lightning strike? y/n: ")
#   while loop for invalid characters loops for "y"
    while done != "y" or "n":
        print()
        print("I couldn't understand your answer,")
        done = input("Would you like to calculate another lightning strike? y/n: ")

    if done == "n":
        print()

main()