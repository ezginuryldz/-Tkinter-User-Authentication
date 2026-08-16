# -Tkinter-User-Authentication
A simple user authentication system built with Python, Tkinter and SQLite. Includes user registration, login validation and database integration.
# Tkinter User Authentication 🔐

A simple user authentication system developed using **Python, Tkinter and SQLite**.

This project provides a graphical interface where users can create an account and log in using their registered email and password.

## ✨ Features

* 👤 User registration
* 🔐 User login
* 🗄️ SQLite database integration
* 📧 Duplicate email validation
* 🔑 Password input masking
* ✅ Login validation
* ❌ Error messages for invalid input
* 🏠 Main menu navigation
* 🖥️ Simple graphical user interface

## 🛠️ Technologies

* **Python**
* **Tkinter**
* **SQLite**
* **Subprocess**
* **Git / GitHub**

## 📂 Project Structure

```text
Tkinter-User-Authentication/
│
├── main.py          # Main menu
├── gui.py           # Login screen
├── kayit.py         # Registration screen
├── user.db          # SQLite database
└── README.md        # Project documentation
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/Tkinter-User-Authentication.git
```

### 2. Open the project folder

```bash
cd Tkinter-User-Authentication
```

### 3. Run the main menu

```bash
python main.py
```

## 🔄 Application Flow

```text
             Main Menu
              /      \
             /        \
        Register      Login
           |            |
           v            v
        user.db  <--  Validation
```

Users can first create an account from the **Register** screen. Their information is stored in the SQLite database.

After registration, the user can log in using their email and password.

## 🗄️ Database

The project uses **SQLite** to store user information.

The `user` table contains:

| Column    | Description          |
| --------- | -------------------- |
| `isim`    | User's first name    |
| `soyisim` | User's last name     |
| `mail`    | User's email address |
| `sifre`   | User's password      |

## 🎨 Interface

The application uses a simple dark brown themed interface created with Tkinter.

## 📚 What I Learned

While developing this project, I practiced:

* Creating GUI applications with Tkinter
* Working with SQLite databases
* Performing SQL queries in Python
* Connecting a GUI to a database
* User input validation
* Navigating between Python files
* Using Git and GitHub for version control

## ⚠️ Note

This project is created for **educational purposes**.

Passwords are currently stored directly in the SQLite database. In a production application, passwords should be securely hashed before being stored.

## 👩‍💻 Author

**Ezginur Yıldız**

Computer Engineering Student

---

⭐ If you find this project useful, feel free to give it a star!
