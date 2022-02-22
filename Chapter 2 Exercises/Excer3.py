# Modify avg2.py program (Section 2.5.3) to find the average of three exam scores.

def main():
    print("This program computes the average of three exam scores.")

    # simultaneous assignment - only works with eval
    score1, score2, score3 = eval(input("Enter three test scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

main()