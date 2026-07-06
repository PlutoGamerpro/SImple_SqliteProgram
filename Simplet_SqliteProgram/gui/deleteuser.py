import tkinter as tk
from tkinter import messagebox
import sqlite3


def deleteuser(user):
    if user["role"] != "admin":
        messagebox.showerror("Permission Denied",
                             "You do not have permission to delete users.")
        return

    delete_window = tk.Toplevel()
    delete_window.title("Delete User")
    delete_window.geometry("300x150")

    tk.Label(delete_window, text="Username").pack(pady=5)

    entry_username = tk.Entry(delete_window)
    entry_username.pack(pady=5)

    def delete():
        username = entry_username.get().strip()

        if not username:
            messagebox.showerror("Error", "Enter a username.")
            return

        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM users WHERE username = ?",
            (username,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showinfo("Result", "User not found.")
        else:
            messagebox.showinfo("Success", "User deleted.")

        conn.close()
        delete_window.destroy()

    tk.Button(delete_window,
              text="Delete User",
              command=delete).pack(pady=10)
