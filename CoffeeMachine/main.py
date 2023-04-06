MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Prompt user by asking what they would like

# TODO: 2. Turn off the Coffee Machine by using "off"

# TODO: 3. Print report

# TODO: 4. Check resources sufficient

# TODO: 5. Process coins

# TODO: 6. Check transaction successful

# TODO: 7. Make Coffee

def coffee_machine():
    """This will show a list of programmes for a selection between 3 different Coffee Flavors"""

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    cost = 0

    def report():
        """Prints out the Machine Report"""

        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${cost}")

    turnoff = False
    while not turnoff:
        coffee_type = input(" What would you like? (espresso/latte/cappuccino): ").lower()
        blank = True
        if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
            blank = False
        if coffee_type == "off":
            turnoff = True
        if coffee_type == "report":
            report()

        if not blank:
            coffee_ingredients = MENU[coffee_type]["ingredients"]
            coffee_water = coffee_ingredients["water"]
            if not coffee_type == "espresso":
                coffee_milk = coffee_ingredients["milk"]
            else:
                coffee_milk = 0
            coffee_coffee = coffee_ingredients["coffee"]

            def checking_machine():
                enough_resources = True
                if coffee_water > water:
                    enough_resources = False
                    print("Sorry there is not enough water.")
                if not coffee_type == "espresso":
                    if coffee_milk > milk:
                        print("Sorry there is not enough milk.")
                        enough_resources = False
                if coffee_coffee > coffee:
                    print("Sorry there is not enough coffee.")
                    enough_resources = False
                return enough_resources

            if checking_machine():
                print("Insert Coins")
                quarters = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickles = int(input("How many nickles: "))
                pennies = int(input("How many pennies: "))

                quarters_to_dollar = quarters * 0.25
                dimes_to_dollar = dimes * 0.10
                nickles_to_dollar = nickles * 0.05
                pennies_to_dollar = pennies * 0.01

                monetary_value = quarters_to_dollar + dimes_to_dollar + nickles_to_dollar + pennies_to_dollar
                coffee_cost = MENU[coffee_type]["cost"]
                change = monetary_value - coffee_cost

                if change < 0:
                    print("Sorry that's not enough money. Money refunded")
                elif not change == 0:
                    print(f"Here is your ${round(change, 2)} in change.")

                if change >= 0:
                    cost += MENU[coffee_type]["cost"]
                    water = water - coffee_water
                    milk = milk - coffee_milk
                    coffee = coffee - coffee_coffee
                    print(f"Here is your {coffee_type} ☕. Enjoy!")


coffee_machine()
