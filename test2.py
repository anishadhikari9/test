phone_directory = {}

print("Welcome to the Phone Directory Management System\n")

while True:
    print("1. Add a record\n2. Search a record\n3. Update a record\n4. Delete a record\n5. Quit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("\nEnter name: ")
        phone = input("Enter 10-digit phone number: ")
        if len(phone) == 10 and phone.isdigit():
            phone_directory[name] = phone
            print("Record added\n")
        else:
            print("Invalid phone number. Please enter a 10-digit number.\n")

    elif choice == "2":
        name = input("\nEnter name to search: ")
        if name in phone_directory:
            print(name + ": " + phone_directory[name] + "\n")
        else:
            print("Record not found\n")

    elif choice == "3":
        name = input("\nEnter name to update: ")
        if name in phone_directory:
            phone = input("Enter new 10-digit phone number: ")
            if len(phone) == 10 and phone.isdigit():
                phone_directory[name] = phone
                print("Record updated\n")
            else:
                print("Invalid phone number. Please enter a 10-digit number.\n")
        else:
            print("Record not found\n")

    elif choice == "4":
        name = input("\nEnter name to delete: ")
        if name in phone_directory:
            del phone_directory[name]
            print("Record deleted\n")
        else:
            print("Record not found\n")

    elif choice == "5":
        print("Thank you for using the Phone Directory Management System!")
        break

    else:
        print("Invalid choice\n")
