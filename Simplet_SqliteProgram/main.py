import gui.signuppage
import gui.login
import gui.getallusers
import gui.deleteuser
import gui.searchuser
print("Welcome to the School Management System!")

input_choice = input(
    "Do you want to (1) Sign up or (2) Log in? Get all Users (3) Search user (4) Delete user (5) Exit(6): ")


while input_choice not in ["1", "2", "3", "4", "5", "6"]:
    print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
    input_choice = input(
        "Do you want to (1) Sign up or (2) Log in? Get all Users (3) Search user (4) Delete user (5) Exit (6): ")

if input_choice == "1":
    gui.signuppage.signup()
elif input_choice == "2":
    gui.login.login()
elif input_choice == "3":
    gui.getallusers.getallusers()
elif input_choice == "4":
    gui.searchuser.searchuser()
elif input_choice == "5":
    gui.deleteuser.deleteuser()
elif input_choice == "6":
    print("Exiting...")
