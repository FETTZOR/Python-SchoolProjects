#! /usr/bin/python3
import numpy as np
import random


#

def make_a_new_deck():
    deck_of_cards = [i for i in range(52)]
    for i in range(13):
        for y in range(4):
            if i < 10:
                deck_of_cards[i + y * 13] = i + 1
            elif i >= 10:
                deck_of_cards[i + y * 13] = 10
    random.shuffle(deck_of_cards)
    return deck_of_cards


print(make_a_new_deck())


def draw_card(deck):
    # print(len(deck))
    card = deck.pop()
    # print(len(deck))
    return card


def calculate_hand(hand):  # takes a list as argument, returns int as sum of cards.
    sum_of_hand = sum(hand)
    return sum_of_hand


def print_hands(dealer_hand_local, player_hand_local):
    print("Dealer has", dealer_hand_local)
    print("Player has", player_hand_local)


def ask_if_player_wants_card(player_hand_now):
    question = "you have now " + str(player_hand_now) + ", do you want another card?"
    answer_local = input(question)
    return answer_local


# change program. So that player hand, and dealer hand is an array.
# meaning that when card is drawn it goes to list

# and when we check result we use calculate_hand() function to get result
# when new card is drawn, put that to the hand, what is now type list

while True:
    deck = make_a_new_deck()
    dealer_hand = []
    player_hand = []
    dealer_hand.append(draw_card(deck))
    player_hand.append(draw_card(deck))
    print(deck)
    while True:
        print_hands(dealer_hand, player_hand)
        answer = ask_if_player_wants_card(player_hand)
        if answer == "yes":
            player_hand.append(draw_card(deck))

            if calculate_hand(player_hand) > 21:
                break
        elif answer == "no":
            break
    while True:
        print_hands(dealer_hand, player_hand)
        if calculate_hand(player_hand) > 21:
            print("you went over, you lose")
            break
        elif calculate_hand(dealer_hand) < 16:
            dealer_hand.append(draw_card(deck))

        elif calculate_hand(dealer_hand) > 21:
            print("dealer went over, you win")

            print("Dealer wins!")
            break
        else:
            print("Player wins!")
            break
    new_game = input("Do you want new game, press enter. If you want to end type:no ")
    if new_game == "no":
        break

# Now we have a working game
# First change
# Next we want to change how we handle card with value 1
# In Blackjack Ace can be 1 or 14.
# Change calculate hand() function:
# if sum is less or equal to 11 change first 1 to 11.
# else if sum is more than 21 change first 11 to 1.
# otherwise function works as previously.
# Second change
# if players 2 first cards are same, player can split hand to 2.
# Meaning that player has two hands to play.
#  make a function that ask if player want to split
#  change while loop, so that this splitting is possible.

# [2, 4, 10, 8, 7, 10, 10, 2, 4, 5, 6, 3, 3, 7, 1, 9, 7, 5, 5, 9, 10, 4, 10, 4, 8, 10, 3, 1, 10, 10, 10, 9, 6, 9, 1, 2, 10, 10, 7, 8, 6, 2, 10, 1, 10, 3, 10, 10, 10, 5, 8, 6]
# [10, 5, 6, 10, 10, 1, 3, 4, 5, 6, 10, 10, 10, 10, 5, 8, 9, 9, 5, 10, 9, 4, 4, 7, 8, 10, 3, 10, 1, 10, 8, 3, 2, 7, 10, 1, 9, 3, 6, 2, 2, 7, 10, 2, 6, 10, 1, 10, 8, 4]
# Dealer has [7]
# Player has [10]
# Dealer has [7]
# Player has [10, 4]
# Dealer has [7]
# Player has [10, 4]
# Dealer has [7, 8]
# Player has [10, 4]
# Dealer has [7, 8, 10]
# Player has [10, 4]
# dealer went over, you win