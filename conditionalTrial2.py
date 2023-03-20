try:
    score = input("Enter a number between 0.0 and 1.0: ")
    fscore = float(score)
    if (fscore >= 1.0):
        print("You didn't follow instructions")
        exit()
    elif (fscore >= 0.9):
        print("A")
    elif (fscore >= 0.8):
        print("B")
    elif (fscore >= 0.7):
        print("C")
    elif (fscore >= 0.6):
        print("D")
    else:
        print("F")
except:
    print("Please enter numerical numbers")
    exit()
