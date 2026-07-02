import sqlite3


def updateuser():
    print("Update user page")
    print("Updating a user's information in the database.")

    username = input("Enter the username of the user to update: ")

    new_username = ""
    new_password = ""

    while True:

        new_username = input("Enter the new username: ")
        if (len(new_username) < 3):
            print("Username must be at least 3 characters long.")

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
