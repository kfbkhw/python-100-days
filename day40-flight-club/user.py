class Users:

    def __init__(self):
        print("Welcome to Hailey's Flight Club!\nWe find the best flight deals and email you.")
        self.user_list = []

    def user_info(self):
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email = input("What is your email?\n")
        verify_email = input("Please type your email again.\n")
        if email == verify_email:
            if self.user_data(first_name, last_name, email):
                print("You're in the club!")
        else:
            print("Please check your email.")
            self.user_info()
        return self.user_list

    def user_data(self, first_name, last_name, email):
        self.user_list.append(
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
            }
        )
        return True
