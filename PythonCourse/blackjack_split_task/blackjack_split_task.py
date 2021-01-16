#! /usr/bin/python3
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


def draw_card(d):
    card = d.pop()
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
    question = "you have now " + str(player_hand_now) + ", do you want another card? yes or no"
    answer_local = input(question)
    return answer_local


def dealer_takes_cards(dealer_hand_local, deck, cards_to_add):
    print("Dealer takes cards")
    new_range = cards_to_add - len(dealer_hand_local)
    for x in range(new_range):
        dealer_hand_local.append(draw_card(deck))


def can_split(player_hand_local, deck):
    split_hand = []
    if len(player_hand_local) > 1 and player_hand_local[0] == player_hand_local[1]:
        question = f'you have cards {player_hand_local}, do you want split our hands? answer yes or no'
        answer_local = input(question)
        if answer_local == "yes":
            split_hand.append([player_hand_local[0]])
            split_hand.append([player_hand_local[1]])
            split_hand[0].append(draw_card(deck))
            split_hand[1].append(draw_card(deck))
            return split_hand
        else:
            return split_hand
    else:
        return split_hand


while True:
    isSplitted = False;
    player_hands = []
    deck = make_a_new_deck()
    dealer_hand = []
    player_hand = []
    dealer_hand.append(draw_card(deck))
    player_hand.append(draw_card(deck))
    answers = []

    while True:
        print_hands(dealer_hand, player_hand)
        if not isSplitted:
            player_hands = can_split(player_hand, deck)

        if len(player_hands) > 0:
            isSplitted = True

            if len(answers) == 0:

                answer = ask_if_player_wants_card(player_hands[0])
                if answer == "yes":
                    player_hands[0].append(draw_card(deck))
                    if calculate_hand(player_hands[0]) > 21:
                        answers.append("no")
                elif answer == "no":
                    answers.append("no")
            else:
                answer = ask_if_player_wants_card(player_hands[1])
                if answer == "yes":
                    player_hands[1].append(draw_card(deck))
                    if calculate_hand(player_hands[1]) > 21:
                        break
                elif answer == "no":
                    break

        else:
            answer = ask_if_player_wants_card(player_hand)
            if answer == "yes":
                player_hand.append(draw_card(deck))

                if calculate_hand(player_hand) > 21:
                    break
            elif answer == "no":
                break

    while True:
        if len(player_hands) > 0:
            dealer_takes_cards(dealer_hand, deck, len(player_hands[0]))
            print_hands(dealer_hand, player_hands)
        else:
            dealer_takes_cards(dealer_hand, deck, len(player_hand))
            print_hands(dealer_hand, player_hand)

        if len(player_hands) > 0:
            if calculate_hand(player_hands[0]) > 21:
                print("you went over, you lose")
            elif calculate_hand(dealer_hand) > 21:
                print("dealer went over, you win")
            else:
                print("Player wins!")

            if calculate_hand(player_hands[1]) > 21:
                print("you went over, you lose")
                break
            elif calculate_hand(dealer_hand) > 21:
                print("dealer went over, you win")
                break
            else:
                print("Player wins!")
                break

        else:
            if calculate_hand(player_hand) > 21:
                print("you went over, you lose")
                break
            elif calculate_hand(dealer_hand) > 21:
                print("dealer went over, you win")
                break
            else:
                print("Player wins!")
                break

    new_game = input("Do you want new game, press enter. If you want to end type:no ")
    if new_game == "no":
        break