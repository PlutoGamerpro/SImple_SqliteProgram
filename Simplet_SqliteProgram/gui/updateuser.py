import sqlite3
import gui.user_exists


def UpdateUserSelf(user):
    print("Update user page")

    username = user["username"]
    while True:

        new_username = input("Enter the new username: ")
        if (len(new_username) < 3):
            print("Username must be at least 3 characters long.")

        elif gui.user_exists.user_exists(new_username):
            print("Username already exists. Please choose a different username.")

        else:
            break

    while True:
        new_password = input("Enter the new password: ")
        if (len(new_password) < 6):
            print("Password must be at least 6 characters long.")

        else:
            break
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users SET username = ?, password = ? WHERE username = ?
    """, (new_username, new_password, username))

    conn.commit()
    conn.close()

    print("User updated.")


def updateuser(user):
    if user["role"] != "admin":
        print("You do not have permission to update users.")
        return
    print("Update user page")
    print("Updating a user's information in the database.")

    username = input("Enter the username of the user to update: ")

    new_username = ""
    new_password = ""

    while True:

        new_username = input("Enter the new username: ")
        if (len(new_username) < 3):
            print("Username must be at least 3 characters long.")

        elif gui.user_exists.user_exists(new_username):
            print("Username already exists. Please choose a different username.")

        else:
            break

    while True:
        new_password = input("Enter the new password: ")
        if (len(new_password) < 6):
            print("Password must be at least 6 characters long.")

        else:
            break

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users SET username = ?, password = ? WHERE username = ?
    """, (new_username, new_password, username))

    conn.commit()
    conn.close()

    print("User updated (if it existed).")
