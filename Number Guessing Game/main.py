#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def easy():
    attemptsLeft = 10

    return attemptsLeft

def hard():
    attemptsLeft = 5

    return attemptsLeft

def whatTheNumber():
    from art import logo
    import random

    print(logo)
    
    level = input("Choose your difficulty [Easy or Hard]: ").lower()
    
    if level == "hard":
        attemptsLeft = hard()
    elif level == "easy":
        attemptsLeft = easy()

    chosenNumber = random.randint(0, 100)
    while not attemptsLeft <= 0:
        print(f"You have {attemptsLeft} remaining, Guess the number")
        guess = int(input("What is the Number: "))
        if not guess == chosenNumber:
            attemptsLeft -= 1
        if guess > chosenNumber:
            print("Too High")
            print("Try again")
        elif guess < chosenNumber:
            print("Too Low")
            print("Try again")
        elif guess == chosenNumber:
            attemptsLeft = -1

    if attemptsLeft == 0:
        print("You've run out of guesses, You Lose.")
    elif attemptsLeft == -1:
        print(f"You Got it!!!, The answer was {chosenNumber}.")

whatTheNumber()