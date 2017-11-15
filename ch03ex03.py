# ch03ex03.py
#   This program computes the molecular weight of a carbohydrate

def main():
    print("This program computes the molecular weight of a carbohydrate(in grams per mole).")
    print()

    done = "y"
#   Will allow you to keep calculating weight by pressing "y"
#   Will crash if skipped anything but a number is entered
    while done == "y":
        print()

        hydrogen = float(input("How many hydrogen atoms in the carbohydrate? "))
        carbon = float(input("How many carbon atoms in the carbohydrate? "))
        oxygen = float(input("How many oxygen atoms in the carbohydrate? "))


        weight = (hydrogen * 1.00794) + (carbon * 12.0107) + (oxygen * 15.9994)
        print("The weight of the carbohydrate is", weight, "grams per mole.")
        print()
        done = input("Press y to calculate another carbohydrate or n to quit. ")

#   will ask again for invalid exit/restart response
#   while loop for invalid characters loops for "y"
    while done != "n" or "y":
        done = input("Press y to calculate another carbohydrate or n to quit. ")
#exits program
    if done == "n":
        print()


main()