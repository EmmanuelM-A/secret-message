import User

EXIT = 3

def welcome_message():
    print("Welcome to Secrey!")

    print("Select an option to precoeed:\n1 - Encrypt Message\n2 - Decrypt Message\n3 - Exit\n")


def main():
    while True:
        welcome_message()

        selected_option = User.get_selected_option()

        if selected_option == EXIT:
            print("\nProgram exited!")
            return
        else:
            message = User.get_user_message()

            print(f"\nYour message is: '{message}' and you wish to {"encrypt" if selected_option == 1 else "decrypt"}.\n")
            return


main()
    




