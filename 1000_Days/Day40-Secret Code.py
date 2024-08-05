message = input("Enter the messeage: ")

words = message.split(" ")
code = int(input("Enter 1 for Code or 0 for Decode"))
code = True if (code == 1) else False
if (code):
    newWords = []
    for i in words:
        if (len(i) >= 3):
            a = "qyv"
            b = "axw"
            cal = a + i[1:] + i[0] + b
            newWords.append(cal)
        else:
            newWords.append(i[::-1])
    print(" ".join(newWords))
else:
    newWords = []
    for i in words:
        if (len(i) >= 3):
            cal = i[3:-3]
            cal = cal[-1]+cal[:-1]
            newWords.append(newWords)
        else:
            newWords.append(i[::-1])

    print(" ".join(newWords))
