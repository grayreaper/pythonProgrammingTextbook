# convertF2C.py
#   A program to convert Fahrenheit temps to Celsius
#   BY: Gray Reaper

def main():
    print("This program converts Fahrenheit temperatures to Celsius.")

    fahrenheit = eval(input("What is the Fahrenheit temperature?"))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature is", celsius, "degrees Celsius.")
    for i in [0, 32, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 212]:
        
        fahrenheit = i
        celsius = (fahrenheit - 32) * 5 / 9
        print(i, "degrees Fahrenheit equals", celsius, "degrees Celsius.")
    input("Press the ENTER key to quit.")
main()
