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
            if check_password in user["Password"]:
                login = f"Logging In"
                return login
            else:
                invalid_pass = "Invalid Password"
                return invalid_pass
    else:
        status = "User not found"
        return status


with open("Database.txt", "r") as data:
    file_lines = data.readlines()

Database = []

for line in file_lines:
    dictionary = json.loads(line)
    Database.append(dictionary)

Options = new_existing_user()
System_ON = True
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

        login_or_not = input("Do you want to login? [Y/n]: ").lower()
        if login_or_not == "y":
            user_named = existing_user_login()
            print(user_named)
            if user_named == "User not found":
                Options = new_existing_user()
            elif user_named == "Logging In":
                System_ON = False
        elif login_or_not == "n":
            Options = new_existing_user()

    elif Options == 1:
        user_named = existing_user_login()
        print(user_named)
        if user_named == "User not found":
            Options = new_existing_user()
        elif user_named == "Logging In":
            System_ON = False
    else:
        print("Invalid Option, Please Try Again")
        Options = new_existing_user()









