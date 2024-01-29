import time

Time = int(time.strftime("%H"))
# print(Time)

if (Time >= 1 and Time <= 12):
    print("Good Morning")

else:
    print("Good Evening")
