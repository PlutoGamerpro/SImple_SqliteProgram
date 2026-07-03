import sqlite3
import gui.updateuser
import gui.deleteuser
import gui.getallusers
import gui.searchuser
import gui.searchuser


def signout():
    print("Signing out...")


def AfterLoginPage(user):
    while True:
        print("\nAfter-login menu:")
        # available for everyone

        if user["role"] == "admin":
            print("1 Update user")
            print("2 Delete user")
            print("3 Get all users")
            print("4 Search users")
            print("5 Sign out")
        print("6 Update user")
        print("7 Sign out")

        choice = input("Enter your choice: ")

        match choice:
            case "1" if user["role"] == "admin":
                print("Update user")
                gui.updateuser.updateuser(user)

            case "2" if user["role"] == "admin":
                print("Delete user")
                gui.deleteuser.deleteuser(user)

            case "3" if user["role"] == "admin":
                print("Get all users")
                gui.getallusers.getallusers(user)

            case "4" if user["role"] == "admin":
                print("Search users")
                gui.searchuser.searchuser(user)

            case "5" if user["role"] == "admin":
                print("Signing out...")
                return False

            case "6":
                print("Update user")
                gui.updateuser.UpdateUserSelf(user)
                break

            case "7":
                print("Signing out...")
                return False

            case _:
                print("Invalid choice. Please try again.")


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
        print("User is logged in!")

        # build session user object
        user = {
            "id": result[0],
            "username": result[1],
            "password": result[2],
            "role": result[3] if len(result) > 3 else "user"
        }

        AfterLoginPage(user)

    else:
        print("Invalid username or password.")
