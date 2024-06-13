import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                contact_info = line.strip().split(",")
                contacts.append(contact_info)
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(",".join(contact) + "\n")

def add_contact(name, phone, email, address):
    contacts = load_contacts()
    contacts.append([name, phone, email, address])
    save_contacts(contacts)

def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact[0]}, Phone: {contact[1]}")
    else:
        print("No contacts found.")

def search_contact(search_term):
    contacts = load_contacts()
    found_contacts = []
    for contact in contacts:
        if search_term in contact[0] or search_term in contact[1]:
            found_contacts.append(contact)
    return found_contacts

def update_contact(name, phone, email, address):
    contacts = load_contacts()
    updated = False
    for contact in contacts:
        if contact[0] == name:
            contact[1] = phone
            contact[2] = email
            contact[3] = address
            updated = True
            break
    if updated:
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name):
    contacts = load_contacts()
    deleted = False
    for contact in contacts:
        if contact[0] == name:
            contacts.remove(contact)
            deleted = True
            break
    if deleted:
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_contacts()
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
            print("Contact added successfully.")
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            found_contacts = search_contact(search_term)
            if found_contacts:
                print("Found Contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
            else:
                print("No contacts found.")
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            update_contact(name, phone, email, address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            delete_contact(name)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
