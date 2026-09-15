import json
import secrets
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
        json.dump(passwords, file, indent=4)


passwords = load_passwords()


def add_password():
    while True:
        website = input("Enter the website: ").strip()
        if website:
            break
        print("❌ Website cannot be empty.")

    while True:
        username = input("Enter the username: ").strip()
        if username:
            break
        print("❌ Username cannot be empty.")

    for item in passwords:
        if (
            item["website"].lower() == website.lower()
            and item["username"].lower() == username.lower()
        ):
            print("⚠️ This website and username already exist.")
            return

    while True:
        password = input("Enter the password: ").strip()
        if password:
            break
        print("❌ Password cannot be empty.")

    passwords.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_passwords()

    print("✅ Password added successfully!")


def view_passwords():
    if not passwords:
        print("No passwords stored.")
        return

    print("=== All Passwords ===")

    for i, data in enumerate(passwords, start=1):
        masked_password = "*" * len(data["password"])

        print(
            f"{i}. {data['website']} | "
            f"{data['username']} | "
            f"{masked_password}"
        )

def search_password():
    if not passwords:
        print("\n⚠️ No passwords saved yet!")
        return

    search_query = input("Enter website name to search: ").strip().lower()

    if not search_query:
        print("❌ Search query cannot be empty.")
        return

    found = False

    print(f"\n====== Search Results for '{search_query}' ======")

    for item in passwords:
        if search_query in item["website"].lower():
            print(
                f"🌐 Website: {item['website']} | "
                f"👤 Username: {item['username']} | "
                f"🔑 Password: {item['password']}"
            )
            found = True

    if not found:
        print("❌ No matching passwords found.")


def generate_password():
    try:
        length = int(
            input("Enter desired password length (e.g., 12): ")
        )

        if length < 8:
            print("⚠️ Password length should be at least 8 characters.")
            return

        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        generated_pass = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        print(f"\n🔑 Generated Password: {generated_pass}")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")


def delete_password():
    if not passwords:
        print("No passwords stored.")
        return

    print("\n=== Saved Passwords ===")

    for i, data in enumerate(passwords, start=1):
        print(
            f"{i}. Website: {data['website']} | "
            f"Username: {data['username']}"
        )

    try:
        choice = int(
            input("Enter the number of the password to delete: ")
        )

        if 1 <= choice <= len(passwords):
            deleted = passwords.pop(choice - 1)
            save_passwords()

            print(
                f"✅ Deleted password for {deleted['website']}."
            )
        else:
            print("❌ Invalid choice. Please try again.")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")


def main():
    global passwords
    passwords = load_passwords()

    while True:
        print("\n" + "=" * 30)
        print("       PASSWORD MANAGER")
        print("=" * 30)
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Generate Password")
        print("5. Delete Password")
        print("6. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-6): ").strip()

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
            print("\nThank you for using Password Manager! 👋")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
