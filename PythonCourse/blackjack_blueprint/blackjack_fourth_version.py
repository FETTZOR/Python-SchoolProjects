# import random
#
# class BlackjackFourthVersion:
#     def __init__(self, game_type):
#         self.game_type = game_type
#
#         def make_a_new_deck(self):
#             deck_of_cards = [i for i in range(52)]
#             for i in range(13):
#                 for y in range(4):
#                     if i < 10:
#                         deck_of_cards[i + y * 13] = i + 1
#                     elif i >= 10:
#                         deck_of_cards[i + y * 13] = 10
#             random.shuffle(deck_of_cards)
#             return deck_of_cards
#
#
#         def draw_card(self, deck):
#             card = deck.pop()
#             return card
#                     if hand[i] == 1:
#                         hand[i] = 11
#                         break
#             elif sum_of_hand > 21:
#                 for i in range(len(hand)):
#                     if hand[i] == 11:
#                         hand[i] = 1
#                         break
#
#
#
#
#         def calculate_hand(self, hand):
#             sum_of_hand = sum(hand)
#             if sum_of_hand <= 11:
#                 for i in range(len(hand)):
#             sum_of_hand = sum(hand)
#             return sum_of_hand
#
#         def print_hands(self, dealer_hand_local, player_hand_local):
#             if self.game_type == "cmd":
#                 print("Dealer has", dealer_hand_local)
#                 print("Player has", player_hand_local)








