# The code below is a simple Contact Management System that allows you to manage your contacts.
# It was created by Okesh

while True:
    print("\nChoose what you want to do today")
    print("1. Save a contact" \
      "\n2. Retrieve a contact" \
      "\n3. View all contacts" \
      "\n4. Exit")
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        print("You chose to save a contact.")
        print("Please enter the following details: ")
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        try:
            file = open("Contacts.txt", "x") # Try to create a new file
            file.write(f"{name} - {number}\n")
            print("Contact Saved.")
        except FileExistsError:
            file = open("Contacts.txt", "a") # Appends to the file if it already exists
            file.write(f"{name} - {number}\n")
            print("Contact Saved.")
        finally:
            file.close()

    elif choice == "2":
        print("You chose to retrieve a contact.")
        search_contact = input("\nEnter the contact you want to retrieve: ")
        try:
            file = open("Contacts.txt", "r") # Open file to check for searched contact
            filecontent = file.readlines()
            found = False
            for contact in filecontent:
                name, number = contact.strip().split(" - ")
                if name.lower() == search_contact:
                    print(f"Contact {search_contact} found!")
                    print(f"Name:  {name}")
                    print(f"Number: {number}")
                    found = True
            if not found:
                print("Contact was not found")
        except FileNotFoundError:
            print("There is no contact file found.")
            break
        finally:
            try: 
                file.close()
            except NameError:
                break

    elif choice == "3":
        print("You chose to view all contacts.")
        try:
            file = open("Contacts.txt", "r") # Try to read the file
            filecontent = file.read() 
            if filecontent == "":
                print("There are no contacts in your file.")
            else:
                print("Viewing all contatcs...")
                for contact in filecontent.splitlines():
                    print(contact)
        except FileNotFoundError:
            print("There is no contact file found.")
            break
        finally:
            try: 
                file.close()
            except NameError:
                break
    elif choice == "4":
        print("Thank you for using Contact Management System."
              "\nExiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    cont = input("\nDo you want to do something else? (yes/no): ")
    if cont.lower() == "no":
        print("Thank you for using Contact Management System.")
        break
    elif cont.lower() == "yes":
        continue
    else:
        print("Invalid input.")
        print("Thank you for using Contact Management System.")
        break
