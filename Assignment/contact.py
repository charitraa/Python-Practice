
# Define a list to store records as dictionaries
records = []

# Function to add an contact


def add_contact(name, phone, email):
    contact = {"Name": name, "Phone": phone, "Email": email}
    records.append(contact)
    print(f"'{name}','{phone}' and '{email}' has been added in contact list")

# Function to list all records


def view_contacts():
    if not records:
        print("No records to display.")
    else:
        for contact in records:
            print(
                f"Name: {contact['Name']}, Phone: {contact['Phone']} and Email: {contact['Email']}")


def search_contact(name):
    for i in records:
        if name == i['Name']:
            print(
                f"Name: {i['Name']}, Phone: {i['Phone']} and Email: {i['Email']}")
        else:
            print("no name found")


# Main program
if __name__ == "__main__":
    print("Welcome to the contact Management system!\n")

    while True:
        print("Options:")
        print("1. Add an contact")
        print("2. List all records")
        print("3. Search for a contact")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("Enter the name: ")
            try:
                phone = int(input("Enter the phone number: "))
                email = input("Enter the email address: ")

                if len(str(phone)) == 10:
                    add_contact(name, phone, email)
                else:
                    print("Phone number should include 10 digits\n")
            except ValueError:
                print("Invalid input.\n")
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter the name to search:")
            search_contact(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.\n")
