import tkinter as tk
import sqlite3
import hashlib

import gui.updateuser
import gui.deleteuser
import gui.getalldata
import gui.searchuser
import gui.ClassesAndGrades


# ----------------------------
# Main Window
# ----------------------------
window = tk.Tk()
window.title("School Login")
window.geometry("400x500")

current_user = None

# ----------------------------
# Helpers
# ----------------------------


def clear_window():
    """Remove all widgets from the window."""
    for widget in window.winfo_children():
        widget.destroy()


def signout():
    global current_user
    current_user = None
    show_login_page()


# ----------------------------
# UI: MENU PAGE
# ----------------------------
def show_menu(user):
    clear_window()

    tk.Label(
        window,
        text=f"Welcome {user['username']}",
        font=("Arial", 16)
    ).pack(pady=20)

    tk.Button(
        window,
        text="Update Profile",
        width=30,
        command=lambda: gui.updateuser.UpdateUserSelf(user)
    ).pack(pady=5)

    if user["role"] == "admin":

        tk.Button(
            window,
            text="Update User",
            width=30,
            command=lambda: gui.updateuser.updateuser(user)
        ).pack(pady=5)

        tk.Button(
            window,
            text="Delete User",
            width=30,
            command=lambda: gui.deleteuser.deleteuser(user)
        ).pack(pady=5)

        tk.Button(
            window,
            text="Get All Users",
            width=30,
            command=lambda: gui.getalldata.getallusers(user)
        ).pack(pady=5)

        tk.Button(
            window,
            text="Get All Classes",
            width=30,
            command=lambda: gui.getalldata.getallclasses(user)
        ).pack(pady=5)

        tk.Button(
            window,
            text="Search User",
            width=30,
            command=lambda: gui.searchuser.searchuser(user)
        ).pack(pady=5)

        tk.Button(
            window,
            text="Create Class",
            width=30,
            command=lambda: gui.ClassesAndGrades.AddClasses(user)
        ).pack(pady=5)

        tk.Button(
            window,
            text="Give Grades",
            width=30,
            command=lambda: gui.ClassesAndGrades.Grades(user)
        ).pack(pady=5)

        tk.Button(
            window,
            text="See Grades",
            width=30,
            command=lambda: gui.ClassesAndGrades.SeeGrades(user)
        ).pack(pady=5)

    tk.Button(
        window,
        text="Sign Out",
        width=30,
        command=signout
    ).pack(pady=20)


# ----------------------------
# LOGIN FUNCTION
# ----------------------------
def login():
    global current_user

    username = entry_user.get()
    password = entry_pass.get()

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, password, salt, role
        FROM users
        WHERE username = ?
    """, (username,))

    result = cursor.fetchone()
    conn.close()

    if not result:
        success_label.config(text="Invalid username or password.", fg="red")
        return

    user_id, db_username, db_hash, db_salt, role = result

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        bytes.fromhex(db_salt),
        100000
    ).hex()

    if password_hash != db_hash:
        success_label.config(text="Invalid username or password.", fg="red")
        return

    current_user = {
        "id": user_id,
        "username": db_username,
        "role": role
    }

    show_menu(current_user)


# ----------------------------
# LOGIN PAGE
# ----------------------------
def show_login_page():
    global entry_user, entry_pass, success_label

    clear_window()

    tk.Label(window, text="Login", font=("Arial", 18)).pack(pady=20)

    tk.Label(window, text="Username").pack()
    entry_user = tk.Entry(window)
    entry_user.pack()

    tk.Label(window, text="Password").pack()
    entry_pass = tk.Entry(window, show="*")
    entry_pass.pack()

    success_label = tk.Label(window, text="")
    success_label.pack(pady=10)

    tk.Button(
        window,
        text="Login",
        width=20,
        command=login
    ).pack(pady=10)


# ----------------------------
# START
# ----------------------------
show_login_page()
window.mainloop()
