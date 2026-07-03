import sqlite3
import gui.updateuser
import gui.deleteuser
import gui.getalldata
import gui.searchuser
import gui.searchuser
import gui.ClassesAndGrades
import gui.ClassesAndGrades


import sqlite3
import hashlib


def signout():
    print("Signing out...")


def AfterLoginPage(user):
    while True:
        print("\nAfter-login menu:")

        if user["role"] == "admin":
            print("1 Update user")
            print("2 Delete user")
            print("3 Get all users & Classes")
            print("4 Search users")
            print("6 Create Class")
            print("7 Give Grades")
            print("8 See Grades")
            print("9 Sign out")

        print("10 Update user (self)")
        print("11 Sign out")

        choice = input("Enter your choice: ")

        match choice:

            case "1" if user["role"] == "admin":
                gui.updateuser.updateuser(user)

            case "2" if user["role"] == "admin":
                gui.deleteuser.deleteuser(user)

            case "3" if user["role"] == "admin":
                gui.getalldata.getallusers(user)
                gui.getalldata.getallclasses(user)

            case "4" if user["role"] == "admin":
                gui.searchuser.searchuser(user)

            case "6" if user["role"] == "admin":
                gui.ClassesAndGrades.AddClasses(user)

            case "7" if user["role"] == "admin":
                gui.ClassesAndGrades.Grades(user)

            case "8" if user["role"] == "admin":
                gui.ClassesAndGrades.SeeGrades(user)

            case "9" if user["role"] == "admin":
                print("Signing out...")
                return

            case "10":
                gui.updateuser.UpdateUserSelf(user)

            case "11":
                print("Signing out...")
                return

            case _:
                print("Invalid choice.")


def login():
    print("Login page")

    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Hent bruger inkl. salt
    cursor.execute("""
        SELECT id, username, password, salt, role
        FROM users
        WHERE username = ?
    """, (username,))

    result = cursor.fetchone()
    conn.close()

    if result is None:
        print("Invalid username or password.")
        return

    user_id, db_username, db_hash, db_salt, role = result

    # Recreate hash using stored salt
    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(db_salt),
        100000
    ).hex()

    if new_hash == db_hash:
        print("User is logged in!")

        user = {
            "id": user_id,
            "username": db_username,
            "role": role
        }

        AfterLoginPage(user)

    else:
        print("Invalid username or password.")


""" OLD VERSION THAT WORKS BUT NOT WITH SALT / HACHED PASSOWRDS
This module handles the login functionality for the School Management System.
def signout():
    print("Signing out...")


def AfterLoginPage(user):
    while True:
        print("\nAfter-login menu:")
        # available for everyone

        if user["role"] == "admin":
            print("1 Update user")
            print("2 Delete user")
            print("3 Get all users & Classes")
            print("4 Search users")
            print("6 Create Class")
            print("7 Give Grades")
            print("8 See Grades")
            print("9 Sign out")

        print("10 Update user")
        print("11 Sign out")

        choice = input("Enter your choice: ")

        match choice:
            case "1" if user["role"] == "admin":
                print("Update user")
                gui.updateuser.updateuser(user)

            case "2" if user["role"] == "admin":
                print("Delete user")
                gui.deleteuser.deleteuser(user)

            case "3" if user["role"] == "admin":
                print("Get all users & Classes")
                gui.getalldata.getallusers(user)
                gui.getalldata.getallclasses(user)

            case "4" if user["role"] == "admin":
                print("Search users")
                gui.searchuser.searchuser(user)

            case "5" if user["role"] == "admin":
                print("Signing out...")
                return False

            case "6" if user["role"] == "admin":
                print("Classes")
                gui.ClassesAndGrades.AddClasses(user)

            case "7" if user["role"] == "admin":
                print("Grades")
                gui.ClassesAndGrades.Grades(user)

            case "8" if user["role"] == "admin":
                print("See Grades")
                gui.ClassesAndGrades.SeeGrades(user)

            case "9" if user["role"] == "admin":
                print("Signing out...")
                return False

            case "10" if user["role"] != "admin":
                print("Update user")
                gui.updateuser.UpdateUserSelf(user)

            case "11" if user["role"] != "admin":
                print("Signing out...")
                return False

            case _:
                print("Invalid choice. Please try again.")


def login():
    print("Login page")
    print("Please enter your credentials to log in.")

    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
"""
#  cursor.execute("""
#     SELECT * FROM users WHERE username = ? AND password = ?
#  """, (username, password))
"""
    result = cursor.fetchone()
    conn.close()

    if result:
        print("User is logged in!")

        # build session user object
        user = {
            "id": result[0],
            "username": result[1],
            "password": result[2],
            "role": result[3] if len(result) > 3 else "user"
        }

        AfterLoginPage(user)

    else:
        print("Invalid username or password.")
"""
