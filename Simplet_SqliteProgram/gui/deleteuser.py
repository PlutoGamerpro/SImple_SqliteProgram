import sqlite3


def deleteuser():
    print("Delete user page")
    print("Deleting a user from the database.")

    username = input("Username: ")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users WHERE username = ? 
    """, (username,))

    conn.commit()
    conn.close()

    print("User deleted (if it existed).")
