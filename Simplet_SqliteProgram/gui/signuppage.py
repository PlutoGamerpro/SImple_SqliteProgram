import sqlite3
import gui.user_exists


def signup():
    print("Signup page")
    print("Please enter your details to create an account.")
    username = ""
    password = ""
    role = ""

    while True:

        username = input("Username: ")
        if len(username) < 3:
            print("Password must be at least 6 characters long.")

        elif gui.user_exists.user_exists(username):
            print("Username already exists. Please choose a different username.")

        else:
            break
    while True:
        password = input("Password: ")
        if (len(password) < 6):
            print("Password must be at least 6 characters long.")

        else:
            break

    while True:
        role = input("Role (student/teacher/admin): ")
        if role not in ["student", "teacher", "admin"]:
            print("Invalid role. Please enter 'student', 'teacher', or 'admin'.")
        else:
            break

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
        )
        """)

    cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
        """, (username, password, role))

    conn.commit()
    conn.close()

    print("Brugeren er oprettet!")
