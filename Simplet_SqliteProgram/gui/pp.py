
import sqlite3
import gui.updateuser
import gui.deleteuser
import gui.getalldata
import gui.searchuser
import gui.searchuser
import gui.ClassesAndGrades
import gui.ClassesAndGrades
import tkinter as tk

import sqlite3
import hashlib


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
