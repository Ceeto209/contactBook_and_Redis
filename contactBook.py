contact_book = {}
file = 'contact_book.txt'

def load_contacts():
    try:
        with open(file, 'r') as book:
            for line in book:
                contact_name, contact_number = line.strip().split(':')
                contact_book[contact_name] = contact_number
    except FileNotFoundError:
        # If the file does not exist, start with an empty contact book
        pass

def save_contacts():
    with open(file, 'w') as book:
        for contact_name, contact_number in contact_book.items():
            book.write(f"{contact_name}:{contact_number}\n")
def main():
    load_contacts()
    while True:
        menu()
        option = input("Enter option: ")
        try:
            user_option = int(option)
        except ValueError:
            print("Error: did not enter a integer")
            save_and_close()
            break

        if user_option == 1:
            add_contact()
        elif user_option == 2:
            view_contacts()
        elif user_option == 3:
            search_contact()
        elif user_option == 4:
            delete_contact()
        elif user_option == 5:
            save_and_close()
            print("Closing")
            break
        else:
            print(f"{option} is an invalid choice. Please a number [1 to 5]")

def menu():
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Remove a contact")
    print("5. Exit")

def add_contact():
    print("Who would you like to add?")
    contact_name = input("Name: ")
    contact_number = input("Phone number: ")
    contact_book[contact_name] = contact_number
    with open(file, 'a') as book:
        book.write(f"{contact_name}:{contact_number}\n")

    print(f"{contact_name}'s number has been saved as {contact_number}.\n")

def view_contacts():
    with open(file, 'r') as book:
        print("Contact List:")
        for line in book:
            contact_name, contact_number = line.strip().split(':')
            print(f"Name: {contact_name}, Phone Number: {contact_number}")

def search_contact():
    search = input("Who would you like to look for?: ")
    found = False
    with open(file, 'r') as book:
        for line in book:
            contact_name, contact_number = line.strip().split(':')
            if contact_name == search:
                print(f"{contact_name}, Phone Number: {contact_number}")
                found = True
                break
    if not found:
        print(f"{search} not found.")

def delete_contact():
    delete = input("Who would you like to delete?: ")
    updated_contacts = []
    found = False
    with open(file, 'r') as book:
        for line in book:
            contact_name, contact_number = line.strip().split(':')
            if contact_name == delete:
                found = True
                print(f"Deleted {delete}'s contact.")
            else:
                updated_contacts.append(line.strip())
    if not found:
        print(f"{delete} was not found.")

    with open(file, 'w') as book:
        for contact in updated_contacts:
            book.write(contact + '\n')

def save_and_close():
    with open(file, 'w') as book:
        for contact_name, contact_number in contact_book.items():
            book.write(f"{contact_name}:{contact_number}\n")
    print("Contacted saved.")

main()