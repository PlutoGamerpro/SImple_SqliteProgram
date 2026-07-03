import gui.updateuser
import gui.searchuser
import gui.deleteuser
import gui.signuppage
import gui.login


def handle(choice):
    match choice:
        case "1":
            gui.signuppage.signup()

        case "2":
            gui.login.login()

        case "3":
            print("Exiting...")
            return False
        case _:
            print("Invalid choice.")
    return True


def IfLogedIn():
    print("Checking if user is logged in...")

    return False


print("Welcome to the School Management System!")

while True:
    input_choice = input(
        "\n"
        "Do you want to:\n"
        "1 Sign up\n"
        "2 Log in\n"
        "3 Exit\n"
        "Enter choice: "
    )

    if input_choice not in ["1", "2", "3"]:
        print("Invalid choice. Try again.")
        continue

    if not handle(input_choice):
        break
