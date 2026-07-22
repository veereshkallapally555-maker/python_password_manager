import json
import random
import string

FILENAME = "passwords.json"

def load_passwords():
    """Load passwords from the JSON file."""
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_passwords():
    """Save passwords to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(Passwords, file, indent=4)

Passwords = load_passwords()

def add_password():

    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    Passwords.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_passwords()

    print("Password added successfully!")


def view_passwords():

    if not Passwords:
        print("No passwords stored.")
        return

    print("=== All Passwords are here! ===")

    for i, data in enumerate(Passwords, start = 1):
        print(f"{i}. {data['website']} | {data['username']} | {data['password']}")


def search_password():
    if not Passwords:

        print("\n⚠️ No passwords saved yet!")
        return

    search_query = input("Enter website name to search: ").strip().lower()
    found = False

    print(f"\n====== Search Results for '{search_query}' ======")
    for item in Passwords:
        if search_query in item['website'].lower():
            print(f"🌐 Website: {item['website']} | 👤 Username: {item['username']} | 🔑 Password: {item['password']}")
            found = True

    if not found:
        print("❌ No matching passwords found.")


def generate_password():
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length < 4:
            print("⚠️ Password length should be at least 4 characters.")
            return
        
        # Combine letters, numbers, and symbols
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate a random password of the requested length
        generated_pass = "".join(random.choice(characters) for _ in range(length))
        
        print(f"\n🔑 Generated Password: {generated_pass}")
        
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")


def delete_password():
    if not Passwords:
        print("No passwords stored.")
        return

    print("\n=== Saved Passwords ===")
    for i, data in enumerate(Passwords, start=1):
        print(f"{i}. Website: {data['website']} | Username:{data['username']}")

    try:
        choice = int(input("Enter the number of the password to delete: "))
        if 1 <= choice <= len(Passwords):
            deleted = Passwords.pop(choice - 1)
            save_passwords()
            print(f"✅ Deleted password for {deleted['website']}.")
        else:
            print("❌ Invalid choice. Please try again.")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

def main():
    global Passwords
    Passwords = load_passwords()

    while True:

        print("=== Password Manager ===")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. generate Password")
        print("5. delete Password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            search_password()

        elif choice == "4":
            generate_password()

        elif choice == "5":
            delete_password()

        elif choice == "6":
            print("Thank You")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()