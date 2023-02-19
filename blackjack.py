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

# def rand_card():
#         return random.choice(cards)
        
def deal_card():
    # user_cards = [rand_card(), rand_card()]
    # comp_cards = [rand_card(), rand_card()]
    # return [user_cards, comp_cards]
    return random.choice(cards)

def calculate_score(list_of_cards):
    return sum(list_of_cards)

begin = input("Do you want to play a game of Blackjac: Type 'y' or 'n': ")
if begin == 'y':
    user_cards = []
    computer_cards = []
    for n in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    your_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # for card in your_hand:
    #     your_score += card
    # for card in comp_hand:
    #     comp_score += card

    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_another == 'y':
        print('Drawing another card...')
    else:
        print(f"Your final hand: {user_cards}, final score: {your_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        if your_score > computer_score:
            print("You win!")
        elif your_score == computer_score:
            print("Draw game.")
        else:
            print("Computer wins the game.")


    