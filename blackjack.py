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
# print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        
def deal_card():
    return random.choice(cards)

def calculate_score(list_of_cards):
    #Checking for Ace
    if sum(list_of_cards) > 21:
        for card in list_of_cards:
            if card == 11:
                list_of_cards.remove(11)
                list_of_cards.append(1)
    
    if list_of_cards[0] + list_of_cards[1] == 21:
        #Checking for Blackjack
        return 0
    else:
        return sum(list_of_cards)

def end_game():
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
    print(logo)
    begin = input("Do you want to play a game of Blackjac: Type 'y' or 'n': ")
    if begin == 'y':
        import os
        os.system('clear')
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
            if calculate_score(user_cards) == 0:
                end_game()
                user_draws_another = False
            elif calculate_score(user_cards) <= 21:
                draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw_another == 'y':
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                    print(f"Your cards: {user_cards}, current score: {user_score}")
                    print(f"Computer's first card: {computer_cards[0]}")
                else:
                    end_game()
                    user_draws_another = False
            else:
                end_game()
                user_draws_another = False
    else:
        keep_playing = False
        print("Thanks for playing!")