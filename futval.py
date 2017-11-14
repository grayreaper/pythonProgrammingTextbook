# futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future

###This is not working properly!!
###This is not working properly!!
###This is not working properly!!
###This is not working properly!!
###This is not working properly!!
###This is not working properly!!
###This is not working properly!!
###This is not working properly!!
###This is not working properly!!
#this is a test fork

def main():
    print("This program calculates the future value")
    print("of an investment.")

    total = eval(input("Enter the amount of initial principal: $"))
    add = eval(input("Enter any additional amount you plan to add each year: $"))
    apr = eval(input("Enter the annual percentage rate as a decimal: "))
    compound = eval(input("How many times per year does the interest compound?\nEnter 1 if you don't know. ")) 
    years = eval(input("How many years will this be invested?"))
        
    for i in range(years * compound):
        total = (1 + (apr / compound)) * (total + add)

    print("The value in", years, "years will be $",total)

main()
                     

