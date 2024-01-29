# Create the Quiz
print("")
print("********************************** Quiz Game **************************************************")
print("")
print("First of all give your name.")
print("")
name = input("Enter your name ?\n\n")
print("")
question = ["What is the Full Form of CPU ?\n\n", "What is a group of crows called ?\n\n",
            "How many dots appear on a pair of dice ?\n\n", "What year was the United Nations established ?\n\n", "How many minutes are in a full week ?\n\n "]
number = []
i = 0
coin = 0
right = 0
wrong = 0

while (i < 5):
    a = input(question[i])
    number.insert(i, a)
    print("")

    if "center processing unit" == number[i]:
        print("you are right.\n")
        coin += 25
        right += 1

    elif "murder" == number[i]:
        print("you are right.\n")
        coin += 25
        right += 1
    elif "42" == number[i]:
        print("you are right\n")
        coin += 25
        right += 1

    elif "1945" == number[i]:
        print("you are right\n")
        coin += 25
        right += 1

    elif "10080" == number[i]:
        print("you are right")
        coin += 25
        right += 1
    else:
        print("you are wrong\n")
        wrong += 1
    i = i + 1


print(f"you give {right} right answer and {wrong} wrong answer")
