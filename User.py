
def get_selected_option():
    while True:
        option = input("Option: ")

        if option.isnumeric():
            option = int(option)
            
            if 0 < option <= 3:
                return option
            else:
                print("Please select a valid option.\n")
        else:
            print("Please input a number.\n")


def get_user_message():
    return input("Please enter your message below:\n") 