import sqlite3
import hashlib
import os
import gui.user_exists
import tkinter as tk
from tkinter import ttk


def signup():

    username = entry_user.get()
    password = entry_pass.get()
    role = combo.get()

    if len(username) < 3:
        error_label.config(text="Username must be at least 3 characters long.")
        return

    if gui.user_exists.user_exists(username):
        error_label.config(text="Username already exists.")
        return

    if len(password) < 6:
        error_label.config(text="Password must be at least 6 characters long.")
        return

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

    sucuess_label.config(text="Signup successful!")
    print("Signup successful!")

    print(username, password, role)


window = tk.Tk()
window.title("Signup")

tk.Label(window, text="Username").pack()
entry_user = tk.Entry(window)
entry_user.pack()

tk.Label(window, text="Password").pack()
entry_pass = tk.Entry(window, show="*")
entry_pass.pack()

label = tk.Label(window, text="Role (student/teacher/admin)")
label.pack(anchor="w", padx=10, pady=(10, 5))


combo = ttk.Combobox(
    window, values=["student", "teacher", "admin"], state="readonly")
combo.pack(padx=10, pady=10)


error_label = tk.Label(window, text="", fg="red")
error_label.pack()

sucuess_label = tk.Label(window, text="", fg="green")
sucuess_label.pack()

tk.Button(window, text="Signup", command=signup).pack()

window.mainloop()

"""
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
"""

#    cursor.execute("""
#       CREATE TABLE IF NOT EXISTS users (
#          id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE NOT NULL,
#        password TEXT NOT NULL,
#       salt TEXT NOT NULL,
#      role TEXT NOT NULL
# )
# """)

# cursor.execute("""
#   INSERT INTO users (username, password, salt, role)
#  VALUES (?, ?, ?, ?)
# """, (
#   username,
#  password_hash.hex(),
# salt.hex(),
# role
#   ))
#
#  conn.commit()
# conn.close()

# print("Brugeren er oprettet!")
