def parse_input(user_input): 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): #function for adding new contact
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts): # function to change user phone
    name, phone = args
    contacts[name] = phone
    return "The phone is successfully changed"


def show_phone(args, contacts): # function for showing certain contact
    name=args[0]
    if name in contacts:
        return contacts[name]
    return 'Not found'

def all_phones(contacts): #function for returning all contacts
    return f"{contacts}"
    

def main():
    contacts = {}   #'John':"123", 'Jane':"234", 'Steve':"555"
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]: 
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all_phones(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()