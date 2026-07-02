import sqlite3


def getallusers():
    print("Get all users page")
    print("Fetching all users from the database.")
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    conn.close()
