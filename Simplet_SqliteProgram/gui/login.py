import sqlite3
import gui.updateuser
import gui.deleteuser
import gui.getalldata
import gui.searchuser
import gui.searchuser
import gui.ClassesAndGrades
import gui.ClassesAndGrades


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

    cursor.execute("""
        SELECT * FROM users WHERE username = ? AND password = ?
    """, (username, password))

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
