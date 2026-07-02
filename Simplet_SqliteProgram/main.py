import gui.signuppage
import gui.login
import gui.getallusers
import gui.deleteuser
import gui.searchuser


def handle(choice):
    match choice:
        case "1":
            gui.signuppage.signup()
        case "2":
            gui.login.login()
        case "3":
            gui.getallusers.getallusers()
        case "4":
            gui.searchuser.searchuser()
        case "5":
            gui.deleteuser.deleteuser()
        case "6":
            print("Exiting...")
            return False
        case _:
            print("Invalid choice.")
    return True


print("Welcome to the School Management System!")

while True:
    input_choice = input(
        "\n"
        "Do you want to:\n"
        "1 Sign up\n"
        "2 Log in\n"
        "3 Get all users\n"
        "4 Search user\n"
        "5 Delete user\n"
        "6 Exit\n"
        "Enter choice: "
    )

    if input_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Try again.")
        continue

    if not handle(input_choice):
        break
