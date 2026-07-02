import sqlite3
import gui.updateuser
import gui.deleteuser


def signout():
    print("Signing out...")
    # Placeholder for actual sign-out functionality


def AfterLoginPage(choice):
    match choice:
        case "1":
            print("Update user 1.")
            gui.updateuser.updateuser()  # Call the updateuser function
        case "2":
            print("Delete user 2.")
            gui.deleteuser.deleteuser()  # Call the deleteuser function
        case "3":
            print("Sign out 3.")
            signout()  # Call the signout function
        case _:
            print("Invalid choice. Please try again.")
# Placeholder for actual after-login functionality


def login():
    print("Login page")
    print("Please enter your credentials to log in.")

    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users WHERE username = ? AND password = ?
    """, (username, password))

    result = cursor.fetchone()

    conn.close()

    if result:
        print("Users is logged in!")
        AfterLoginPage(
            input("Enter your choice (1: Update user, 2: Delete user, 3: Sign out): "))
    else:
        print("Invalid username or password.")
