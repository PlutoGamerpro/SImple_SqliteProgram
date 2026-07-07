import sqlite3
import tkinter as tk
from tkinter import messagebox


def searchuser(user):
    if user["role"] != "admin":
        messagebox.showerror(
            "Permission Denied",
            "You do not have permission to search users."
        )
        return

    window = tk.Toplevel()
    window.title("Search User")
    window.geometry("400x300")

    tk.Label(window, text="Username").pack(pady=5)

    entry_username = tk.Entry(window)
    entry_username.pack(pady=5)

    result_box = tk.Text(window, width=45, height=10)
    result_box.pack(pady=10)

    def search():
        username = entry_username.get().strip()

        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return

        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, username, role FROM users WHERE username = ?",
            (username,)
        )

        results = cursor.fetchall()
        conn.close()

        result_box.delete("1.0", tk.END)

        if results:
            for row in results:
                result_box.insert(
                    tk.END,
                    f"ID: {row[0]}\nUsername: {row[1]}\nRole: {row[2]}\n\n"
                )
        else:
            result_box.insert(tk.END, "User not found.")

    tk.Button(
        window,
        text="Search",
        command=search
    ).pack(pady=5)
