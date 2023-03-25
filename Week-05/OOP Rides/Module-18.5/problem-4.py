import os

FileName = 'contacts.txt'

def add_contact():
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number of the contact: ")
    with open(FileName,"a") as file:
        file.write(f"{name},{number}\n")
    print(f"Added {name} with number {number} to contacts.")

def view_contact():
    with open(FileName,"r") as file:
        for line in file:
            name,number = line.strip().split(",")
            print(f"{name}: {number}")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = []
    with open(FileName,"r") as file:
        for line in file:
            contact_name,number = line.strip().split(",")
            if contact_name != name:
                contacts.append(f"{contact_name},{number}")

    with open(FileName,"w") as file:
        file.write("\n".join(contacts))
    print(f"{name} has been deleted from contacts.")

if not os.path.exists(FileName):
    with open(FileName,"w") as file:
        file.write("")

while True:
    print("\nSelect an option:")
    print("1. Add a contact")
    print("2. View contacts")
    print("3. Delete a contact")
    print("4. Quit")
    choice = input('>Input:')
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice,Please try again")