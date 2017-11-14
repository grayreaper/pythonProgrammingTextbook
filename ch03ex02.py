# cho3ex02.py
#   Cost per square inch of pizza

import math

def main():
    print("This program computes the cost per")
    print("square inch of pizza.")
    print()

    diam = float(input("Enter ths diameter of the pizza (in inches): "))
    price = int(input("Enter the price of pizza (in cents): "))
    area = math.pi * (diam/2.0)**2
    cost = price / area
    print()
    print("The cost is", cost, "cents per square inch.")

main()