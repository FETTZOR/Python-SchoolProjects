import random

def dice_sides():
    number_of_sides_in_dice = int(input("How many-sided dice you want to cast? "))
    how_much_dice_sides = [i for i in range(1, number_of_sides_in_dice + 1)]
    return how_much_dice_sides


def how_many_rolls():
    ask_how_many_rolls = int(input("How many rolls do you want?"))
    return ask_how_many_rolls


def random_number_from_dice_list(sides, rolls_num):
    sum_of_dices = 0

    for i in range(rolls_num):
        rolled_dice = random.choice(sides)
        print(rolled_dice)
        sum_of_dices = rolled_dice + sum_of_dices
    return sum_of_dices


if __name__ == '__main__':
    sides = dice_sides()
    rolls_num = how_many_rolls()
    rolled_dice = random_number_from_dice_list(sides, rolls_num)
    print(f'Your random numbers is {rolled_dice}')
# also ask how many rolls the user want to do,
# Make as many function calls that are need, to have all the rolls.
# and print separate results and also the sum of results
