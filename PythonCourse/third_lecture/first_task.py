import random


def make_a_new_deck():
    short_list = [i for i in range(1, 14)]
    short_list[12] = 10
    short_list[11] = 10
    short_list[10] = 10
    norm_list = short_list * 5
    random.shuffle(norm_list)
    print(norm_list)
    # deck_of_card = [i for i in range(52)]
    # for i in range(13):
    # for y in range(4):
    # if < 10:
    # deck_of_cards[i+y*13] = i + 1
    # elif deck_of_cards[i + y * 13] = 10
    # print(deck_of_cards)
    # return deck_of_cards


deck = make_a_new_deck()


def draw_card():
    norm_list = make_a_new_deck()
    temp = norm_list.pop()
    print(temp)
    return temp
