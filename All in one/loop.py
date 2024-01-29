# there are two type of loops:
from datetime import datetime
# 1 - for loop

friends = ['ravi', 'chari', 'rijan', 'abishek']

for element in friends:
    print(element)
print("")
for i in friends:
    print(i)


for i in range(11):
    print(i)


# while loop


while True:
    var = input("Enter :")

    if "hello" in var:
        print("hello there , i am a bot")

    elif "bye" in var:
        print("it be great to see you again")

    elif " how are you " in var:
        print("i am fine")
        print("what was About you")

    elif "time" in var:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"the time is now {time}")

    elif "exit" in var:
        break
