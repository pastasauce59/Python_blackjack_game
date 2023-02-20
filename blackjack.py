############### Blackjack House Rules #####################

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

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        
def deal_card():
    """Returns a card from the deck."""
    return random.choice(cards)

def calculate_score(list_of_cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    #Checking for Blackjack
    if list_of_cards[0] + list_of_cards[1] == 21:
        return 0
    
    #Checking for Ace
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    
    return sum(list_of_cards)

def end_game():
    """Calculates and compares user and computer score, prints final hands and declares winner"""
    your_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    if computer_score == 0:
        print("Computer wins with a Blackjack! 🃏 🤖")
    elif your_score == 0:
        print("You win with a Blackjack! 🃏 😃")
    elif your_score > 21:
        print("You went over and lose!")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif your_score == computer_score:
        print("Draw game, there is no winner.")
    elif your_score > computer_score:
        print("You win!")
    elif computer_score > your_score:
        print("Computer wins the game.")

keep_playing = True
while keep_playing:
    begin = input("Do you want to play a game of Blackjac: Type 'y' or 'n': ")
    if begin == 'y':
        import os
        os.system('clear')
        print(logo)

        user_cards = []
        computer_cards = []

        #For testing Blackjack
        # user_cards = [11,10]
        # computer_cards = [10,11]

        for n in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        #Draws cards for computer's hand
        if calculate_score(computer_cards) != 0:
            while calculate_score(computer_cards) < 17:
                computer_cards.append(deal_card())

        user_draws_another = True
        while user_draws_another:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            if user_score == 0 or computer_score == 0 or user_score > 21:
                end_game()
                user_draws_another = False
            else:
                draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw_another == 'y':
                    user_cards.append(deal_card())
                    #re-declaring user_score incase of ace found in hand the user_cards will reflect the appended 1 and removed 11.
                    #Without this the user_cards would display incaccurately with the 11 remaining but udpated score reflecting a 1.
                    user_score = calculate_score(user_cards)
                    print(f"Your cards: {user_cards}, current score: {user_score}")
                    print(f"Computer's first card: {computer_cards[0]}")
                else:
                    end_game()
                    user_draws_another = False
    else:
        keep_playing = False
        print("Thanks for playing!")