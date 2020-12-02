import numpy as np
import random


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
    if sum_of_hand <= 11:
        for i in range(len(hand)):
            if hand[i] == 1:
                hand[i] = 11
                break
    elif sum_of_hand > 21:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                break
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
if __name__ == "main":

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
                break
            elif calculate_hand(dealer_hand) >= calculate_hand(player_hand):
                print("Dealer wins!")
                break
            else:
                print("Player wins!")
                break
        new_game = input("Do you want new game, press enter. If you want to end type:no ")
        if new_game == "no":
            break