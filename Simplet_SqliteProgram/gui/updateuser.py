import tkinter as tk
from tkinter import messagebox
import sqlite3
import gui.user_exists


def UpdateUserSelf(user):
    window = tk.Toplevel()
    window.title("Update Profile")
    window.geometry("350x220")

    tk.Label(window, text="New Username").pack(pady=5)
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="New Password").pack(pady=5)
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    def update():
        new_username = entry_username.get().strip()
        new_password = entry_password.get()

        if len(new_username) < 3:
            messagebox.showerror(
                "Error",
                "Username must be at least 3 characters long."
            )
            return

        if (new_username != user["username"] and
                gui.user_exists.user_exists(new_username)):
            messagebox.showerror(
                "Error",
                "Username already exists."
            )
            return

        if len(new_password) < 6:
            messagebox.showerror(
                "Error",
                "Password must be at least 6 characters long."
            )
            return

        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Replace new_password with your hashed password here
        cursor.execute("""
            UPDATE users
            SET username = ?, password = ?
            WHERE id = ?
        """, (new_username, new_password, user["id"]))

        conn.commit()
        conn.close()

        user["username"] = new_username

        messagebox.showinfo("Success", "Profile updated.")
        window.destroy()

    tk.Button(window, text="Update", command=update).pack(pady=15)


def updateuser(user):
    if user["role"] != "admin":
        messagebox.showerror(
            "Permission Denied",
            "You do not have permission to update users."
        )
        return

    window = tk.Toplevel()
    window.title("Update User")
    window.geometry("350x300")

    tk.Label(window, text="Username to Update").pack(pady=5)
    entry_old = tk.Entry(window)
    entry_old.pack()

    tk.Label(window, text="New Username").pack(pady=5)
    entry_new = tk.Entry(window)
    entry_new.pack()

    tk.Label(window, text="New Password").pack(pady=5)
    entry_pass = tk.Entry(window, show="*")
    entry_pass.pack()

    def update():
        old_username = entry_old.get().strip()
        new_username = entry_new.get().strip()
        new_password = entry_pass.get()

        if len(new_username) < 3:
            messagebox.showerror(
                "Error",
                "Username must be at least 3 characters long."
            )
            return

        if (new_username != old_username and
                gui.user_exists.user_exists(new_username)):
            messagebox.showerror(
                "Error",
                "Username already exists."
            )
            return

        if len(new_password) < 6:
            messagebox.showerror(
                "Error",
                "Password must be at least 6 characters long."
            )
            return

        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Replace new_password with your hashed password here
        cursor.execute("""
            UPDATE users
            SET username = ?, password = ?
            WHERE username = ?
        """, (new_username, new_password, old_username))

        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showinfo("Result", "User not found.")
        else:
            messagebox.showinfo("Success", "User updated.")

        conn.close()
        window.destroy()

    tk.Button(window, text="Update User", command=update).pack(pady=15)
