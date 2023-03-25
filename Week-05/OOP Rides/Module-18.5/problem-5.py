from fileinput import filename
import os

FileName = 'contacts.txt'

def add_contact():
    name = input("Enter the name of the contact: ")
    number = input("Enter the phone number of the contact: ")

    with open(FileName,'r') as file:
        for line in file:
            contact_name,contact_number = line.strip().split(",")
            if name.lower() == contact_name.lower():
                print("This person is already entered.")
                return
            elif number == contact_number:
                add = input("this person's telephone number is already in the database.This could be an error, or a second contact at the same company.Add anyway?(Y/N)").lower()
                if add != "y":
                    return
    #add new contact:
    with open(FileName,"a") as file:
        file.write(f"{name},{number}\n")
    print(f"Added {name} with number {number} to contacts.")
    

def view_contact():
    if not os.path.exists(FileName):  #check for file exists
        print("No contacts found.")
        return

    if os.stat(FileName):  #check for file empty
        print("No contacts found.")
        return
    
    
    with open(FileName,"r") as file:
        for line in file:
            name,number = line.strip().split(",")
            print(f"{name}: {number}")


def delete_contact():
    if not os.path.exists(FileName):
        print("No contacts found.")
        return
    
    name = input("Enter the name of the contact to delete: ")
    contacts = []


    with open(FileName,"r") as file:
        contact_found = False
        for line in file:
            contact_name,number = line.strip().split(",")
            if name.lower() == contact_name.lower():
                contact_found = True
                print(f"{contact_name}: {number}")
            else:
                contacts.append(f"{contact_name},{number}")
        
        if contact_found == False:
            print("Contact not found.")
            return

    with open(FileName,"w") as file:
        file.write("\n".join(contacts))
    print(f"{name} has been deleted from contacts.")

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
        print("Invalid choice,Please try again.")