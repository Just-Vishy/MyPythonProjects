from art import logo
from art import vs

# creating a function called
def higher_lower():
    from game_data import data
    import random

    list = []
    chosen_list = random.choice(data)
    list.append(chosen_list)

    currentScore = 0
    scoring = 0
    shouldContinue = True
    while shouldContinue:
        chosen_list = random.choice(data)

        if chosen_list == list[0]:
            chosen_list = random.choice(data)

        list.append(chosen_list)

        nameA = list[0]['name']
        descriptionA = list[0]['description']
        follower_countA = list[0]['follower_count']
        countryA = list[0]['country']

        nameB = list[1]['name']
        descriptionB = list[1]['description']
        follower_countB = list[1]['follower_count']
        countryB = list[1]['country']
        
        print(logo)

        if scoring > 0:
            print(f"You're right! Current Score: {currentScore}.")

        scoring += 1

        print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}")

        print(vs)
        print(f"Against B: {nameB}, a {descriptionB}, from {countryB}")

        
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        A = follower_countA
        B = follower_countB

        if A > B and answer == "a":
            currentScore += 1
            list.remove(list[1])

        elif A < B and answer == "b":
            currentScore += 1
            list.remove(list[0])

        else:
            shouldContinue = False
            print(logo)
            print(f"Sorry, that's wrong. Final Score: {currentScore}")


higher_lower()
