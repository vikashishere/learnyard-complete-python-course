#  Project 1: Contact Management System (CLI App)

#  Concepts Reinforced:
# Dictionaries (for storing contacts)
# Strings (search, format, input sanitization)
# Functions
# Error handling with try-except
# Loops & menu system

# Contact Management System

contacts = {}

def show_menu():
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter contact name: ").strip().lower()
    phone = input("Enter phone number: ").strip()

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"{name.title()} -> {phone}")

def search_contact():
    name = input("Enter name to search: ").strip().lower()
    phone = contacts.get(name)
    if phone:
        print(f"{name.title()} -> {phone}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip().lower()
    try:
        del contacts[name]
        print("Contact deleted.")
    except KeyError:
        print("Contact not found.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")


# 🔁 Reinforcement Ideas:
# Add email address and store as dict of dicts (contacts[name] = {"phone": x, "email": y})
# Add validation: phone must be digits only
# Add export to a .txt file (after file I/O is taught)