# Create the Quiz
print("")
print("********************************** Quiz Game **************************************************")
print("")
print("First of all give your name.")
print("")
name = input("Enter your name ?\n")
print("")
question = ["What is the Full Form of CPU ?\n\n", "What is a group of crows called ?\n\n",
            "How many dots appear on a pair of dice ?\n\n", "What year was the United Nations established ?\n\n", "How many minutes are in a full week ?\n\n "]
number = ["one", "two", "three", "four", "five", "six"]
i = 0
coin = 0
right = 0
wrong = 0

while (i < 2):

    number[i] = input(question[i])
    print("")

    if "center processing unit" in number[0]:
        print("you are right.\n")
        coin += 25
        right += 1
    elif "center processing unit" != number[0] in number[0]:
        print("you are wrong\n")
        wrong = +1
    elif "murder" in number[1]:
        print("you are right.\n")
        coin += 25
        right += 1
    elif "murder" != number[1] in number[1]:
        print("you are wrong\n")
        wrong = +1
    # elif "42" in number[2]:
    #     print("you are right\n")
    #     coin += 25
    #     right += 1
    # elif "" in number[2]:
    #     print("you are wrong\n")
    #     wrong = +1
    # elif "1945" in number[3]:
    #     print("you are right\n")
    #     coin += 25
    #     right += 1
    # elif "" in number[3]:
    #     print("you are wrong\n")
    #     wrong = +1
    # elif "10080" in number[4]:
    #     print("you are right")
    #     coin += 25
    #     right += 1
    # else:
    #     print("you are wrong\n")
    #     wrong = +1
    i = i + 1


print(f"you give {right} right answer and {wrong} wrong answer")
