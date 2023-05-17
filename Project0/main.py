import random
import json


def new_existing_user():
    print("Enter a number")
    new_existing = input("1. Existing User or 2. New User: ")
    if new_existing == "1":
        return 1
    elif new_existing == "2":
        return 2


def get_user_profile():
    name = input("Enter a Name: ")
    surname = input("Enter your Surname: ")
    email = input("Enter your Email Address: ")
    province = input("Enter Province: ")
    password = input("Enter a Password: ")
    while password == "":
        password = input("Enter a Password: ")

    user_profile = {
        "Name": name,
        "Surname": surname,
        "Email": email,
        "Province": province,
        "Password": password
    }
    return user_profile


def getting_name(surname):
    username_name = ""
    x = 0
    for profile in surname["Name"]:
        if x in range(3):
            username_name += profile
        x += 1
    return username_name


def getting_num():
    username_number = ""
    for _ in range(3):
        x = random.randint(0, 9)
        username_number += str(x)
    return username_number


def getting_province(surname):
    username_surname = ""
    x = 0
    for profile in surname["Province"]:
        if x in range(3, 6):
            username_surname += profile
        x += 1
    return username_surname


def get_username():
    username = " "
    username += getting_name(users_profile)
    username += getting_num()
    username += getting_province(users_profile)
    return username


def existing_user_login():
    username = input("Enter Username: ")
    for user in Database:
        if username in user["Username"] and username != "":
            check_password = input("Enter Password: ")
            if check_password in user["Password"] and check_password != "" and check_password == user["Password"]:
                login = f"Logging In"
                return login
            else:
                invalid_pass = "Invalid Password"
                return invalid_pass
    else:
        status = "User not found"
        return status


def reset_password():
    username = input("Enter Username: ")
    surname = input("Enter your Surname: ")
    email = input("Enter your Email Address: ")
    province = input("Enter Province: ")

    for user in Database:
        checks = 0
        if username in user["Username"] and username != "":
            checks += 1
        if surname in user["Surname"] and surname != "":
            checks += 1
        if email in user["Email"] and email != "":
            checks += 1
        if province in user["Province"] and province != "":
            checks += 1

        if checks == 4:
            new_password = input("Enter a new password: ")
            user["Password"] = new_password
            return user
    print("Unfortunately your details don't match, hence you can't reset your password")


with open("Database.txt", "r") as data:
    file_lines = data.readlines()

Database = []

for line in file_lines:
    dictionary = json.loads(line)
    Database.append(dictionary)

Options = new_existing_user()
System_ON = True
No_Continue = False
while System_ON:
    if Options == 2:
        users_profile = get_user_profile()
        got_username = get_username()
        print(f"Your Username is {got_username}")
        users_profile["Username"] = got_username
        Database.append(users_profile)
        with open("Database.txt", "r+") as data:
            for file in Database:
                files = json.dumps(file)
                data.write(files)
                data.write("\n")
        login_or_not = input("1. Login\n2. Menu\n3. Exit\n: ").lower()
        if login_or_not == "1":
            user_named = existing_user_login()
            print(user_named)
            if user_named == "User not found":
                Options = new_existing_user()
            elif user_named == "Invalid Password":
                get_check = input("forgot password? [Y/n]: ").lower()
                if get_check == "y":
                    resetting = reset_password()
                    if resetting != "Unfortunately your details don't match, hence you can't reset your password":
                        with open("Database.txt", "r+") as data:
                            for file in Database:
                                files = json.dumps(file)
                                data.write(files)
                                data.write("\n")
            elif user_named == "Logging In":
                System_ON = False
        elif login_or_not == "2":
            Options = new_existing_user()
        else:
            System_ON = False
            No_Continue = True

    elif Options == 1:
        user_named = existing_user_login()
        print(user_named)
        if user_named == "User not found":
            for _ in range(2):
                Options = new_existing_user()
        elif user_named == "Invalid Password":
            get_check = input("forgot password? [Y/n]: ").lower()
            if get_check == "y":
                resetting = reset_password()
                if resetting != "Unfortunately your details don't match, hence you can't reset your password":
                    with open("Database.txt", "r+") as data:
                        for file in Database:
                            files = json.dumps(file)
                            data.write(files)
                            data.write("\n")
        elif user_named == "Logging In":
            System_ON = False
    else:
        print("Invalid Option, Please Try Again")
        Options = new_existing_user()


def get_contact():
    name = input("Enter Contact Name: ")
    country = input("Enter your Country Code: +")
    contact_number = int(input("Enter Contact : "))
    contacts_profile = {
        "contact_name": name,
        'country': country,
        "contact_number": contact_number
    }

    return contacts_profile


if not No_Continue:
    state_on = True
    while state_on:
        logout_not = input(": ").lower()
        if logout_not == "logout":
            state_on = False

