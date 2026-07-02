import sqlite3


def signup():
    print("Signup page")
    print("Please enter your details to create an account.")

    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO users (username, password)
    VALUES (?, ?)
    """, (username, password))

    conn.commit()
    conn.close()

    print("Brugeren er oprettet!")
