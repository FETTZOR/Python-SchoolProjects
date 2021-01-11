#! /usr/bin/python3
import random
import email_sender_easy as mail
from datetime import datetime
import smtplib
from email.message import EmailMessage

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




def game_end():
    end_game = datetime.now()

    current_time = end_game.strftime("%H:%M:%S")
    print("Game end =", current_time)
    return current_time


if __name__ == '__main__':
    start_time = datetime.now()
    starting_time = start_time.strftime("%H:%M:%S")
    print("Game started =", starting_time)
    time_list = [starting_time]
    start_list_without_brackets = ', '.join(time_list)
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
                print("Dealer wins!")
                break
            else:
                print("Player wins!")
                break
        new_game = input("Do you want new game, press enter. If you want to end type:no ")
        if new_game == "no":
            gmail_user = "hhttajapai@gmail.com"

            with open("pw.txt") as filereader:
                gmail_password = filereader.read()

            to = ['hhttajapai@gmail.com']
            subject = f'game started {start_list_without_brackets} game ended {game_end()}'
            body = ''

            msg = EmailMessage()
            msg.set_content(body)
            msg['Subject'] = subject
            msg['from'] = gmail_user
            msg['To'] = to

            while True:
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                except:
                    print('cannot connect to server')
                    break
                try:
                    server.login(gmail_user, gmail_password)
                except:
                    print("error with username or pw")
                    break
                try:
                    server.send_message(msg)
                except:
                    print("error with senging email")
                    break
                try:
                    server.close()
                except:
                    print("error with server closing")
                    break
                break
            break
