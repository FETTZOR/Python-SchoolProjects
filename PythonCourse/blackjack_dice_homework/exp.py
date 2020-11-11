import random

listok = []
def dice_sides():
    number_of_sides_in_dice = int(input("How many-sided dice you want to cast? "))
    how_much_dice_sides = [i for i in range(1, number_of_sides_in_dice + 1)]
    return how_much_dice_sides


def how_many_rolls():
    if len(listok) == 0:
        ask_how_many_rolls = int(input("How many rolls do you want?"))
        listok.append(ask_how_many_rolls)
        return ask_how_many_rolls
    else:
        prev_item = listok.pop()
        return prev_item


def random_number_from_dice_list(choose_sides):
    sum_of_dices = 0
    for i in range(how_many_rolls()):
        rolled_dice = random.choice(choose_sides)
        print("Your random numbers is ", rolled_dice)
        sum_of_dices = rolled_dice + sum_of_dices
    print("Sum of dices", sum_of_dices)
    wanna_roll_again()


def wanna_roll_again():
    answer = int(input("User do you want to roll again?"
                       "\n1)Yes "
                       "\n2)End "
                       "\n3)Change Dice "
                       "\n4)Change Number Of Rolls "
                       "\n5)Change Both "))
    if answer == 3:
        random_number_from_dice_list(dice_sides())




random_number_from_dice_list(dice_sides())

# print(dice_d6[random.randrange(6)])
# after result as from user if she or he wants to roll again,
# or change dice, number of rolls or both
# if the user answers end, end program.
