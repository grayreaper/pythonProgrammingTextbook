# convert.py
#   A program t convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("This program converts Celsius temperatures to Fahrenheit.")

    celsius = eval(input("What is the Celsius temperature?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    for i in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        
       # celsius = eval(input("What is the Celsius temperature?"))
        celsius = i
        fahrenheit = 9/5 * celsius + 32
        print(i, "degrees Celsius equals", fahrenheit, "degrees Fahrenheit.")
    input("Press the ENTER key to quit.")
main()
