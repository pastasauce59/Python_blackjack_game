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
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def rand_card():
        return random.choice(cards)
        
def draw_cards():
    user_cards = [rand_card(), rand_card()]
    comp_cards = [rand_card()]
    return [user_cards, comp_cards]

begin = input("Do you want to play a game of Blackjac: Type 'y' or 'n': ")
if begin == 'y':
    your_hand = draw_cards()[0]
    your_score = 0
    comp_hand = draw_cards()[1]
    comp_score = 0

    for card in your_hand:
        your_score += card

    print(f"Your cards: {your_hand}, current score: {your_score}")
    print(f"Computer's first card: {comp_hand[0]}")

    