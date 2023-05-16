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
        elif login_or_not == "n":
            Options = new_existing_user()

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
    country = input("Enter your Country: ")
    contact_number = int(input("Enter Contact : "))
    contacts_profile = {
        "contact_name": name,
        'country': country,
        "contact_number": contact_number
    }

    return contacts_profile


Exit = "Logout"

username_confirm = input("Enter your Username: ")

with open(f"{username_confirm}_List.txt", "w+") as data:
    contacts = data.readlines()

contact_list = []

for line in contacts:
    dictionary = json.loads(line)
    contact_list.append(dictionary)

check2 = input("Select the following Options [Enter number Only]\n1. Show Contact List\n2. Creating New Contact"
               "\n: ").lower()
while check2 == "1" or check2 == "2" or check2 == "3":
    if check2 == "1":
        print(contact_list)
    elif check2 == "2":
        new_contact = get_contact()
        contact_list.append(new_contact)
        with open(f"{username_confirm}_List.txt", "r+") as data:
            for contact in contact_list:
                contacts = json.dumps(contact)
                data.write(contacts)
                data.write("\n")
    elif check2 == "3":
        print("Logging Off")
        break

    check2 = input("Select the following Options [Enter number Only]\n1. Show Contact List\n2. Creating New Contact\n"
                   "3. Logout\n:").lower()


