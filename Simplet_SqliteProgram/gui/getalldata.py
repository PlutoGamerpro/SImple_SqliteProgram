import sqlite3
from tkinter import messagebox
import tkinter as tk


def getallusers(user):
    if user["role"] != "admin":
        print("You do not have permission to view all users.")
        return
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, role FROM users")
    users = cursor.fetchall()

    conn.close()

    window = tk.Toplevel()
    window.title("All Users")

    tk.Label(window, text="Users List").pack()

    for u in users:
        tk.Label(window, text=f"{u[0]} | {u[1]} | {u[2]}").pack()


def getallclasses(user):
    if user["role"] != "admin":
        print("You do not have permission to view all classes.")
        return
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, class_name FROM classes")
    classes = cursor.fetchall()

    conn.close()

    window = tk.Toplevel()
    window.title("All Classes")

    tk.Label(window, text="Classes List").pack()

    for c in classes:
        tk.Label(window, text=f"{c[0]} | {c[1]}").pack()


"""
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
"""
