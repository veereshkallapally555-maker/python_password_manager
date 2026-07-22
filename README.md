# 🔐 Password Manager

A secure command-line Password Manager built with Python that generates strong random passwords and manages credentials safely. The application permanently stores data using JSON serialization, making it easy to retrieve and organize login information.

---

## ✨ Features

- ➕ Add new website passwords and usernames
- 📋 View all stored credentials in a clean list
- 🔍 Search passwords by website name
- 🎲 Strong random password generator with custom lengths
- 🗑️ Delete outdated passwords
- 💾 Automatic JSON data storage
- 🔄 Persistent data storage across sessions
- ⚠️ Input validation and exception handling

---

## 🛠️ Technologies Used

- Python 3
- JSON
- Random & String Modules
- File Handling
- Exception Handling
- Data Structures (Lists & Dictionaries)
- Git & GitHub

---

## 📂 Project Structure

password_manager/
│
├── password_manager.py
├── passwords.json
├── README.md
└── .gitignore

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/python-password-manager.git
```

### Navigate to the project

```Bash
cd python-password-manager
```

### Run the application

```Bash
python password_manager.py
```

---

## 📸 Sample Output

```

====== Password Manager ======

1. Add Password
2. View Passwords
3. Search Password
4. Generate Password
5. Delete Password
6. Exit

Enter Choice: 4

Enter desired password length (e.g., 12): 16

🔑 Generated Password: K9#xL2@p9$vM1!qZ
📄 Example passwords.json
JSON
[
    {
        "website": "github.com",
        "username": "veereshkallapally",
        "password": "SuperSecretPassword123!"
    },
    {
        "website": "google.com",
        "username": "veeresh@gmail.com",
        "password": "K9#xL2@p9$vM1!qZ"
    }
]
```

---


## 🎯 Skills Demonstrated

- Python Standard Library (random, string, json)
- Dynamic Data Serialization with JSON
- String Manipulation & Formatting
- Command Line Interface (CLI) UX Design
- Exception & Error Handling
- Version Control with Git & GitHub

---


## 🔮 Future Improvements

- File encryption using cryptography / Fernet
- Master password protection on startup
- Auto-copy passwords to clipboard (pyperclip)
- Password strength analyzer
- Graphical User Interface (Tkinter/PyQt)

---


👨‍💻 Author
Veeresh Kallapally
* GitHub: [@veereshkallapally555-maker](https://github.com/veereshkallapally555-maker)
* LinkedIn: [Veeresh Kallapally](https://www.linkedin.com/in/veeresh-kallapally-a87164390/)

If you found this project helpful, consider giving it a ⭐ on GitHub!