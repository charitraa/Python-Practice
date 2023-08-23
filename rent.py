import main
import datetime


def renting():
    main.showequip()
    cname = input("Enter your name: ")

    try:
        eqname = int(
            input("Enter the corresponding number of what you want to rent: ")) - 1
        equipment_data = []
        with open("read.txt", "r") as file:
            for line in file:
                no, name, brand, price, quantity = line.strip().split(", ")
                equipment = {
                    "No": no,
                    "Name": name,
                    "Brand": brand,
                    "Price": price,
                    "Quantity": int(quantity)
                }
                equipment_data.append(equipment)

        equipments = equipment_data[eqname]
        if equipments["Quantity"] > 0:
            rentaldate = datetime.datetime.now()
            while True:
                try:
                    number = int(
                        input(f"Enter how many pieces of {equipments['Name']} you want to rent: "))
                    if number <= equipments["Quantity"]:
                        break
                    else:
                        print("stock unavialabe")
                except:
                    print("please enter a valid number")

            while True:
                try:
                    rentdays = int(
                        input(f"Enter the rental duration in days for {equipments['Name']}. "))
                    break
                except ValueError:
                    print("Please enter a valid number.")

            rentfor5 = rentdays // 5
            if rentdays % 5 != 0:
                rentfor5 += 1

            pricee = float(equipments["Price"].replace("$", ""))
            totalRentPrice = pricee * rentfor5
            print("Total Price:", totalRentPrice, "$")
            # subtarct the value of quantity with taken quantity
            replace = str((equipments["Quantity"] - number))
            value = str(equipments["Quantity"])

            # replace the value of quantity in txt file
            with open('read.txt', 'r') as file:
                filedata = file.read()
            filedata = filedata.replace(value, replace)
            with open('read.txt', 'w')as file:
                file.write(filedata)

                # invoice
                invoice = f'''==== Invoice of Renting ====
        Customer Name: {cname}
        Equipment Details:
        Name: {equipments['Name']}
        Brand: {equipments['Brand']}
        Quantity: {number}
        Price per 5 days: {equipments['Price']}
        ===================================
        '''
            filename = f"{cname}_invoice.txt"
            with open(filename, "w") as filevariable:
                filevariable.write(invoice)
            print(invoice)  # Print the invoice content

        else:
            print("Sorry, we are out of stock.")
    except Exception as e:
        print(e)
