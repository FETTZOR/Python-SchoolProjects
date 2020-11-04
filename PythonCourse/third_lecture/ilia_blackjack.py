import random


def make_a_new_deck():
    short_list = [i for i in range(1, 14)]
    short_list[12] = 10
    short_list[11] = 10
    short_list[10] = 10
    new_deck = short_list * 5
    random.shuffle(new_deck)
    return new_deck


def draw_card(deck):
    take_one_card_from_deck = deck.pop()
    return take_one_card_from_deck


def print_hands(dealer_hand_local, player_hand_local):
    print("dealer has ")
    print(dealer_hand_local)
    print("player has ")
    print(player_hand_local)


if __name__ == '__main__':
    game_deck = make_a_new_deck()
    dealer_hand = []
    player_hand = []

    for x in range(3):
        dealer_hand.append(draw_card(game_deck))

    for y in range(2):
        player_hand.append(draw_card(game_deck))

    print_hands(dealer_hand, player_hand)
