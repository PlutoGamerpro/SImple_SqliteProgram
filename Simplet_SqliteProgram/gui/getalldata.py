import sqlite3


def getallusers(user):
    if user["role"] != "admin":
        print("You do not have permission to view all users.")
        return
    print("Get all users page")
    print("Fetching all users from the database.")
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    conn.close()


def getallclasses(user):
    if user["role"] != "admin":
        print("You do not have permission to view all classes.")
        return
    print("Get all classes page")
    print("Fetching all classes from the database.")
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM classes")
    print(cursor.fetchall())

    conn.close()
