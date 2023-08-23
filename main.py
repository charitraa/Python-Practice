import time
from tabulate import tabulate
import rent
import rent_return


def topic():
    print(time.asctime(time.localtime(time.time())))
    text = "WELCOME TO DATTEBAYO WELCOME SHOP"
    # dis = 2200 #bringing the text to center
    # print("  " * dis + text)
    print("=" * 20, "WELCOME TO DATTEBAYO WELCOME SHOP", "=" * 20, "\n\n")


def task():
    print(""" Choose what task you want to perform by choosing its respective number.
    1. TO SEE THE DETAILS OF EQUIPMENT.
    2. TO RENT THE EQUIPMENT.
    3. TO RETURN THE EQUIPMENT.
    4. TO END THE PROGRAM.""")


def showequip():
    print("{:<8} {:<33} {:<15} {:<10} {:<5}".format(
        "No.", "Equipment", "Brand", "Price ($)", "Quantity"
    )
    )
    f = open("read.txt")
    data = f.readlines()
    f.close()
    headers = data[0].strip().split(",")
    table_data = [line.strip().split(",") for line in data[1:]]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


while True:
    topic()
    task()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        showequip()
    elif choice == 2:
        showequip()
        rent.renting()
    elif choice == 3:
        showequip()
        rent_return.returning()
    elif choice == 4:
        print("Thank you for using Dattebayo Welcome Shop!")
        break
    else:
        print("Please choose a valid number.")
