import random

list_for_dice = []
list_for_roll = []


def dice_sides():
    if len(list_for_roll) == 0:
        number_of_sides_in_dice = int(input("How many-sided dice you want to cast? "))
        how_much_dice_sides = [i for i in range(1, number_of_sides_in_dice + 1)]
        list_for_roll.append(how_much_dice_sides)
        return how_much_dice_sides
    else:
        prev_item = list_for_roll[-1]
        return prev_item


def how_many_rolls():
    if len(list_for_dice) == 0:
        ask_how_many_rolls = int(input("How many rolls do you want?"))
        list_for_dice.append(ask_how_many_rolls)
        return ask_how_many_rolls
    else:
        prev_item = list_for_dice[-1]
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
    answer = input("User do you want to roll again?"
                       "\n1)yes "
                       "\n2)end "
                       "\n3)change dice "
                       "\n4)change rolls "
                       "\n5)change both ")
    if answer == '1' or answer == 'yes':
        random_number_from_dice_list(dice_sides())
    elif answer == '2' or answer == 'end':
        print("Bye")
    elif answer == '3' or answer == "change dice":
        list_for_roll.clear()
        random_number_from_dice_list(dice_sides())
    elif answer == '4' or answer == "change rolls":
        list_for_dice.clear()
        random_number_from_dice_list(dice_sides())
    elif answer == '5' or answer == "change both":
        list_for_roll.clear()
        list_for_dice.clear()
        random_number_from_dice_list(dice_sides())
    else:
        random_number_from_dice_list(dice_sides())


random_number_from_dice_list(dice_sides())

# print(dice_d6[random.randrange(6)])
# after result as from user if she or he wants to roll again,
# or change dice, number of rolls or both
# if the user answers end, end program.
