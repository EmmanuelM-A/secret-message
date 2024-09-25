
EXIT = 3

def welcome_message():
    print("Welcome to Secrey!")

    print("Select an option to precoeed:\n1 - Encrypt Message\n2 - Decrypt Message\n3 - Exit")


def get_selected_option():
    option = input("Option: ")

    if option.isdigit:
        return int(option)
    else:
        print("Please select an option!")


def main():
    while True:
        welcome_message()

        selected_option = get_selected_option()

        type(selected_option)

        if selected_option == EXIT:
            print("Exit")
            return
        else:
            print(f"Option Selected: {selected_option}")
    
        print()

    print("Thank you!")


main()
    




