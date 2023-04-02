############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

def add(value1, value2):
    """Adding Value1 and Value2 and returning it"""
    return value1 + value2

def senario(myAnswer, computerAnswer):
    """Checking the senario and returning a value based on which is True"""
    if myAnswer == 0:
        return "Win with a Blackjack 😎"
    elif computerAnswer == 0:
        return "Lose, opponent has Blackjack 😱"
    elif myAnswer > computerAnswer and myAnswer <= 21:
        return "You win 😃"
    elif computerAnswer > myAnswer and computerAnswer <= 21:
        return "You lose 😤"
    elif myAnswer > 21 and computerAnswer < 21:
        return "You went over. You lose 😭"
    elif myAnswer < 21 and computerAnswer > 21:
        return "Opponent went over. You win 😁"
    elif myAnswer > 21 and computerAnswer > 21:
        return "You went over. You lose 😤"
    elif myAnswer == computerAnswer:
        return "Draw 🙃"
    
def blackjack():
    """Black Jack code"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   
    playingGameOrNot = input("Do you want to play Blackjack Game (Y or N): ").lower()
    
    if playingGameOrNot == "y":
        print(logo)
        mylist = []
        chosen_card = random.choice(cards)
        mylist.append(chosen_card)
        chosen_card = random.choice(cards)
        mylist.append(chosen_card)
        answer = add(mylist[0], mylist[1])
        if answer == 21:
            answer = 0
        print(f" Your deck is {mylist} and current score is: {answer}")

        computerlist = []
        chosen_card = random.choice(cards)
        computerlist.append(chosen_card)
        computeranswer = chosen_card
        print(f" Computer's first card is {computeranswer}")

        repeating = True
        checking = 0
        while repeating:
            if checking <= 21 and not answer == 0:
                Quest1 = input("Type 'y' to HIT and 'n' to PASS: ").lower()
                if Quest1 == "y":
                    chosen_card = random.choice(cards)
                    mylist.append(chosen_card)
                    answer = 0
                    for position in range(len(mylist)):
                        calculate = mylist[position]
                        answer += calculate
                        checking = answer
                        if chosen_card == 11 and checking > 21:
                            mylist.remove(11)
                            mylist.append(1)
                            answer -= 10
                            checking = answer
                    print(f"    Your deck is {mylist} and current score is: {answer}")
                    print(f"Computer's first card is {computeranswer}")
                    
                else:   
                    repeating = False
                    checking = 22            
                    chosen_card = random.choice(cards)
                    computerlist.append(chosen_card)
                    computeranswer = add(computerlist[0], computerlist[1])
                    if computeranswer == 21:
                        computeranswer = 0
                    if computeranswer <= 21 and computeranswer > 0:
                        chosen_card = random.choice(cards)
                        computerlist.append(chosen_card)
                        computeranswer = 0
                        for position in range(len(computerlist)):
                            calculate = computerlist[position]
                            computeranswer += calculate
                            if chosen_card == 11 and computeranswer > 21:
                                computerlist.remove(11)
                                computerlist.append(1)
                                computeranswer -= 10
                    print(f"    Your deck is {mylist} and current score is: {answer}")
                    print(f"Computer's deck is {computerlist} and current score is: {computeranswer}")
                    
            else:
                repeating = False
                chosen_card = random.choice(cards)
                computerlist.append(chosen_card)
                chosen_card = random.choice(cards)
                computerlist.append(chosen_card)
                if computeranswer > 0:
                    computeranswer = 0
                    for position in range(len(computerlist)):
                        calculate = computerlist[position]
                        computeranswer += calculate
                        if chosen_card == 11 and computeranswer > 21:
                                computerlist.remove(11)
                                computerlist.append(1)
                                computeranswer -= 10
                print(f"    Your deck is {mylist} and current score is: {answer}")
                print(f"Computer's deck is {computerlist} and current score is: {computeranswer}")

        print(senario(myAnswer=answer,computerAnswer=computeranswer))
        blackjack()
    
blackjack()