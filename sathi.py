
import datetime
import random
import display

# Getting the current date and time
dateAndTime = datetime.datetime.now()
presentDateAndTime = dateAndTime.strftime("%m/%d/%Y")


def showingEquipments(equipments):
    print(equipments)
    with open("equipment_data.txt", "q") as e:
        for product_id, information in equipments.items():
            if information['Quantity'] > 0:
                e.write = (
                    f"{information['Product Name']}, {information['Brand']}, {information['Price']}, {information['Quantity']}\n")

# def updateEquipmentFile(equipments):
#     with open("equipment_data.txt", "w") as f:
#         for product_id, information in equipments.items():
#             f.write(f"{information['Product Name']}, {information['Brand']}, {information['Price']}, {information['Quantity']}\n")


def generate_rent_receipt(customerName, renting, rented_items, total_amount):
    with open(f"{customerName}_Rent_Receipt.txt", "w") as cFile:
        cFile.write("""
<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luna Ivy Shop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Rent Receipt ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>""")
        cFile.write(
            f"Rent No: {renting}\t\t\t\t\t\t\t\t\t\t Date: {presentDateAndTime}\n")
        cFile.write(f"\t\t\t\t\t\t\tCustomer Name: {customerName}\n\n")
        cFile.write(
            "\t__________________________________________________________________________________________\n")
        cFile.write("Product Name".ljust(20) + "Brand".ljust(15) +
                    "Price".ljust(15) + "Quantity".ljust(15) + "Total\n")
        cFile.write(
            "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        for product_id, item_info in rented_items.items():
            product_name = item_info["Product Name"].ljust(20)
            brand = item_info["Brand"].ljust(15)
            price = item_info["Price"].ljust(15)
            quantity = str(item_info["Quantity"]).ljust(15)
            total = str(item_info["Total"]) + "\n"

            cFile.write(product_name + brand + price + quantity + total)
            cFile.write(
                "\t----------------------------------------------------------------------------------------\n")

        cFile.write(
            "\t________________________________________________________________________________________\n")
        cFile.write("Total Price:".rjust(91) + str(total_amount) + "\n")
        cFile.write(
            "\t+===========================================================================================+\n")
        cFile.write(
            "+========================================Thanks For Renting========================================+")


def forCustomer():
    global customerName
    global isInitiated
    isInitiated = True
    print("\n|---------Enter some information of customer for generating receipt.---------")

    while isInitiated:
        customerName = input("Enter the Customer Name:").strip()

        if customerName != "":
            # print("\n||||||||   Please provide the name of the customer ||||||||\n")
            isInitiated = True
            break
        elif customerName.isalpha():
            renting = random.randint(1, 500)
            rented_items = {}  # Store rented items with their details
            with open("_Rent_Receipt.txt", "w") as cFile:
                cFile.write("""
<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luna Ivy Shop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Rent Receipt ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>""")
                cFile.write(
                    f"Rent No: {renting}\t\t\t\t\t\t\t\t\t\t Date: {presentDateAndTime}\n")
                cFile.write(f"\t\t\t\t\t\t\tCustomer Name: {customerName}\n\n")
                cFile.write(
                    "\t__________________________________________________________________________________________\n")
                cFile.write("{:<18} {:<15} {:<15} {:<15}{:}".format("Product Name",
                                                                    "Brand", "Price", "Quantity", "Total"))
                cFile.write(
                    "\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t")
            isInitiated = True
        else:
            print(
                "\n||||||||||  Please, Input Proper String Name Without Space  |||||||||||\n")
    return isInitiated


def renting_equipments(isInitiated):
    nev = display.equipments_x()
    display.prod_tables(nev)

    print("\n")
    global totalAmount
    totalAmount = 0
    rented_items = {}  # Store rented items with their details
    renting = random.randint(1, 500)  # Define 'renting' variable here

    while isInitiated:
        try:
            print(
                "\n\t~~~~~~~~~~~~~Type a Product ID of Equipment you want to rent.~~~~~~~~~~~~~")
            product_id = int(input(" = "))

            if product_id in nev.keys():
                quan = int(input(
                    "\n\t~~~~~~~~~~~~~Enter the quantity of equipment to rent~~~~~~~~~~~~~\n = "))
                if quan <= 0:
                    print("\n|||||||| Please enter a valid value in quantity. |||||||")
                elif quan <= nev[product_id]["Quantity"]:
                    price = int(nev[product_id]["Price"].replace("$", ""))
                    totalAmount += price * quan

                    rented_items[product_id] = {
                        "Product Name": nev[product_id]["Product Name"],
                        "Brand": nev[product_id]["Brand"],
                        "Price": nev[product_id]["Price"],
                        "Quantity": quan,
                        "Total": price * quan
                    }

                else:
                    print("\n|||||||| Insufficient quantity of equipment ||||||||\n")
            else:
                print(
                    "\n||||||||  Product ID not found / Look Product ID carefully!||||||||\n")
                isInitiated = True

            print("\n\tWould you like to rent any other products? (yes / no)?")
            mb = input("=")
            if mb.lower() == "no":
                break
            elif mb.lower() == "yes":
                isInitiated = True
            else:
                print("please enter YES or NO")
        except ValueError:
            print(
                "\n|||||||| Please, provide a valid Product ID as an integer. ||||||||\n")

    # Generate the rent receipt
    generate_rent_receipt(customerName, renting, rented_items, totalAmount)
    replace = str((nev[product_id]["Quantity"] - quan))
    value = str(nev[product_id]["Quantity"])

    # replace the value of quantity in txt file
    with open('equipments_data.txt', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(value, replace)
    with open('equipments_data.txt', 'w')as file:
        file.write(filedata)


def Alltogether(grandPrice):

    while True:

        c_price = grandPrice + 500
        with open(f"_Rent_receipt.txt", "a+") as cn:
            cn.write(
                """\n\t________________________________________________________________\n""")
            cn.write(
                "                   Total Price: $" + str(grandPrice) + "\n")
            cn.write(
                "                   Shipping Charge: $500\n")
            cn.write(
                "                   Total with Shipping charge: $" + str(c_price))
            cn.write(
                """\n\t----------------------------------------------------------------\n""")

            cn.write(
                """\n\t------------------------------  THANK YOU !  ------------------------------\n""")
            print("<<    Successfully rented.   >>")
        return


grandPrice = 0  # Reset grandPrice after processing
Alltogether(grandPrice)
