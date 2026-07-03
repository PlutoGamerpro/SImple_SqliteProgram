import sqlite3


def searchuser(user):
    print("Search user page")
    print("Searching for a user in the database.")
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    username = input("Enter the username to search for: ")
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    results = cursor.fetchall()
    if results:
        print("User found:")
        for row in results:
            print(row)
    else:
        print("User not found.")

    conn.close()
