"""A contact manager that handles invalid input and missing contacts safely."""

contacts = {}


class DuplicateContactError(Exception):
    """Raised when someone tries to add a name that already exists."""


def add_contact(name, phone):
    """Add a new contact, or raise DuplicateContactError for duplicates."""
    if name in contacts:
        raise DuplicateContactError(f"Contact '{name}' already exists.")
    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Print and return a phone number; return None for missing contacts."""
    try:
        phone = contacts[name]
    except KeyError:
        # A missing name should not close the whole program.
        print("Contact not found.")
        return None
    print(f"{name}: {phone}")
    return phone


def delete_contact(name):
    """Remove a contact, or print a message if the name is missing."""
    try:
        del contacts[name]
    except KeyError:
        # Catch only the missing-dictionary-key error.
        print("Contact not found.")
        return
    print(f"Deleted {name}.")


def main():
    """Display the menu and keep running until the user chooses to exit."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            # Converting letters like 'abc' to an integer raises ValueError.
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            if not name or not phone:
                print("Name and phone number cannot be empty.")
                continue
            try:
                add_contact(name, phone)
            except DuplicateContactError as error:
                print(error)
        elif choice == 2:
            name = input("Enter name to find: ").strip()
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            delete_contact(name)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
