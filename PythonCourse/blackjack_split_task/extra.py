#! /usr/bin/python3
import random
from datetime import datetime
import csv
import sender


def game_start():
    starting_time = datetime.now()

    starting_time = starting_time.strftime("%H:%M:%S")
    print("Game start =", starting_time)
    return starting_time


def game_end():
    end_game = datetime.now()
    current_time = end_game.strftime("%H:%M:%S")
    print("Game end =", current_time)
    return current_time


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
    card = deck.pop()
    return card


def calculate_hand(hand):
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


if __name__ == '__main__':
    game_info_for_email_subject = ["Game Started: ", game_start()]

    games_total = 0
    wins = 0
    win_hands = 1
    wins_lost_list = []
    while True:
        deck = make_a_new_deck()
        dealer_hand = []
        winner = []
        player_hands = [[]]
        dealer_hand.append(draw_card(deck))
        player_hands.append(draw_card(deck))
        player_hands[0].append(draw_card(deck))
        player_hands[0].append(draw_card(deck))
        print(deck)
        if player_hands[0][0] == player_hands[0][1]:
            if ask_if_player_wants_card(player_hands[0]) == "yes":
                player_hands.append([])
                player_hands[1].append(player_hands[0].pop())
                player_hands[0].append(draw_card(deck))
                player_hands[1].append(draw_card(deck))
        for i in range(len(player_hands)):
            while True:
                print_hands(dealer_hand, player_hands[i])
                answer = ask_if_player_wants_card(player_hands[i])
                if answer == "yes":
                    player_hands[i].append(draw_card(deck))

                    if calculate_hand(player_hands[i]) > 21:
                        break
                elif answer == "no":
                    break
            hands_went_over = [False, False]
            for i in range(len(player_hands)):
                print_hands(dealer_hand, player_hands)
                if calculate_hand(player_hands[i]) > 21:
                    print("you went over, you lose the hand")
                    hands_went_over[i] = True
            if all(hands_went_over) == True:
                print("you lose all hands")
            elif calculate_hand(dealer_hand) < 16:
                while calculate_hand(dealer_hand) < 16:
                    dealer_hand.append(draw_card(deck))
                    print("dealer takes a card")
                    print_hands(dealer_hand, player_hands)

                if calculate_hand(dealer_hand) > 21:
                    print("dealer went over, you win")
                else:
                    for i in range(len(player_hands)):
                        if calculate_hand(dealer_hand) >= calculate_hand(player_hands[i]):
                            print("Dealer wins the hand!")
                        else:
                            print("Player wins the hand!")
                            wins += 1
            new_game = input("Do you want new game, press enter. If you want to end type:no")
            if new_game == "no":
                game_info_for_email_subject.append("Game Ended")
                game_info_for_email_subject.append(game_end())
                game_info_for_email_subject.append("Games Total: ")
                game_info_for_email_subject.append(str(games_total))
                game_info_for_email_subject.append("Wins: ")
                game_info_for_email_subject.append(str(wins))
                time_without_brackets = ' '.join(game_info_for_email_subject)
                lines = games_total

                # writing csv
                with open('game_information.csv', mode='w') as random_val_file:
                    random_writer = csv.writer(random_val_file, delimiter=',')
                    random_writer.writerow(['game', 'played hands', 'wins'])

                # data lines
                with open('game_information.csv', mode='a') as random_val_file:
                    random_writer = csv.writer(random_val_file, delimiter=',')
                    a = 0
                    for a in range(lines):
                        u = wins
                        random_writer.writerow([a, win_hands, wins])

                sender.email_sender(time_without_brackets, "hello")
                break
