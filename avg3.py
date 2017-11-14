# avg3.py
#   A simple program to average 3 exam scores.
#   Illustrates the use of multiple input

def main():
    print("This program computes the average of three exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by commas: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

    input("Press ENTER to exit.")
main()
