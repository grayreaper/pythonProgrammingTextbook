# factorial.py
#   This program calculates the factorial of a number.
#   BY: Gray Reaper

def main():
    print("This program calculates the factorial of a number.")
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of", n,"is", fact)

main()
