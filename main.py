from datetime import datetime, timedelta
from collections import defaultdict

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except (KeyError, IndexError):
            return "Invalid input. Check your data."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error    
def add_contact(args, contacts):
    if len(args) >= 2:
        name = args[0]
        # Combine the remaining elements in args to form the phone number
        phone = ' '.join(args[1:])
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command. Please provide both name and phone number."

def hello():
    return "How can I help you?"

@input_error
def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(contacts, name):
    return contacts.get(name, "Contact not found.")

@input_error
def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add" and len(args) >= 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_contact(contacts, args[0], args[1]))
        elif command == "phone" and len(args) == 1:
            print(show_phone(contacts, args[0]))
        elif command == "all" and not args:
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


