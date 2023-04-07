import random


def card_numbers():
    card = ""
    x = 0
    card_number = []
    while x < 16:
        digit = random.randint(0, 9)
        card_number.append(digit)
        x += 1

    for position in range(len(card_number)):
        card_position = card_number[position]
        card += str(card_position)
        if position == 3 or position == 7 or position == 11:
            card += " "
    system = card.split("  ")
    return card


def create_an_account(name, surname, age, country, banking_account, card, pin):
    banking_profile = {
        "name": name,
        "surname": surname,
        "age": age,
        "country": country,
        "banking account": banking_account,
        "card": card,
        "PIN": pin
    }
    return banking_profile


def system_cloud():
    print("Welcome to Zevsify Banking")

    system = []
    database = []
    creating_new_account = True
    while creating_new_account:
        checking = input("Do you want to create a Banking Account: ").lower()
        if checking == "no":
            creating_new_account = False

        person_name = input("Enter your Name: ")
        person_surname = input("Enter your Surname: ")
        person_age = int(input("Enter your Age: "))
        person_country = input("Enter your Country: ")
        banking_account_type = input("Enter Banking Account Type: ")
        pin = int(input("Enter a 4 or 5 digit Pin: "))
        person_card = card_numbers()
        if person_card in system:
            person_card = card_numbers()
        system.append(person_card)
        print(system)

        database.append(
            create_an_account(name=person_name, surname=person_surname, age=person_age, country=person_country, banking_account=banking_account_type,
                              card=person_card, pin=pin))
        print(database)
    print(system)