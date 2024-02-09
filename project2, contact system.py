class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} - Phone: {self.phone_number}"

class ContactSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact added: {contact}")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            print("Contact List:")

            for contact in self.contacts:
                print(contact)


def main():
    contact_system = ContactSystem()

    while True:
        print("Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            new_contact = Contact(name, phone_number)
            contact_system.add_contact(new_contact)

        elif choice == "2":
            contact_system.display_contacts()

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()