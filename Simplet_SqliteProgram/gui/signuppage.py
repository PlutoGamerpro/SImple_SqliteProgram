import sqlite3
import hashlib
import os
import gui.user_exists


def signup():
    print("Signup page")
    print("Please enter your details to create an account.")

    while True:
        username = input("Username: ")

        if len(username) < 3:
            print("Username must be at least 3 characters long.")
        elif gui.user_exists.user_exists(username):
            print("Username already exists.")
        else:
            break

    while True:
        password = input("Password: ")

        if len(password) < 6:
            print("Password must be at least 6 characters long.")
        else:
            break

    while True:
        role = input("Role (student/teacher/admin): ").lower()

        if role not in ("student", "teacher", "admin"):
            print("Invalid role.")
        else:
            break

    # Opret et nyt salt til denne bruger
    salt = os.urandom(16)

    # Hash adgangskoden
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100000
    )

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            salt TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    cursor.execute("""
        INSERT INTO users (username, password, salt, role)
        VALUES (?, ?, ?, ?)
    """, (
        username,
        password_hash.hex(),
        salt.hex(),
        role
    ))

    conn.commit()
    conn.close()

    print("Brugeren er oprettet!")
