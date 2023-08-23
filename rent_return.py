import main


def returning():
    main.showequip()
    cname = input("Enter your name: ")
    try:
        eqname = int(
            input("Enter the corresponding number of the equipment you want to return: "))-1
        equipment_data = []
        with open("read.txt", "r") as file:
            for line in file:
                no, name, brand, price, quantity = line.strip().split(", ")
                equipment = {
                    "No": no,
                    "Name": name,
                    "Brand": brand,
                    "Price": price,
                    "Quantity": int(quantity),
                }
                equipment_data.append(equipment)

        equipments = equipment_data[eqname]
        if equipments["Quantity"] >= 0:
            while True:
                try:
                    number = int(
                        input(f"Enter how many pieces of  {equipments['Name']}you want to return: "))
                    if 0 < number:

                        break
                    else:
                        print(
                            f"Please enter a valid quantity for {equipments['Name']}.")
                except:
                    print("Please enter  a valid integer.")

            while True:
                try:
                    rentdays = int(
                        input(f"Enter the days you rented {equipments['Name']} for? "))
                    break
                except ValueError:
                    print("Please enter a valid number.")

            while True:
                try:
                    returnday = int(
                        input("Enter how many days you rented the equipment for."))
                    if 0 < returnday:
                        print("Daatebayo, you returned it.")
                        break
                    else:
                        print("Please enter  a valid integer.")
                except:
                    print("Please enter a valid integer.")

            rentfor5 = rentdays // 5
            if rentdays % 5 != 0:
                rentfor5 += 1

            days = rentfor5*5
            overprice = 0

            if returnday > days:
                overduedays = returnday - days
                overprice = overduedays * 10
                print(overprice)
            else:
                print("")

            replace = str((equipments["Quantity"] + number))
            value = str(equipments["Quantity"])

            # replace the value of quantity in txt file
            with open('read.txt', 'r') as file:
                filedata = file.read()
            filedata = filedata.replace(value, replace)
            with open('read.txt', 'w')as file:
                file.write(filedata)
            # invoice for returning*************

            invoice = f'''==== Invoice of Equipment Return ====
            Customer Name: {cname}
            Equipment Details:
            Name: {equipments['Name']}
            Brand: {equipments['Brand']}
            Quantity Returned: {number}
            Rental Days: {number}
            Rented Days: {rentdays}
            Return Days: {returnday}
            ===================================
                '''
            print("overcharge amount= ", overprice)
            filename = f"{cname}_return_invoice.txt"
            with open(filename, "w") as filevaraible:
                filevaraible.write(invoice)
            print(invoice)

        else:
            print("Please enter the correct number by reviewing the table.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
