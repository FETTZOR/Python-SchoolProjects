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


def wanna_roll_again():
    answer = input("User do you want to roll again?"
                   "\n1)yes "
                   "\n2)end "
                   "\n3)change dice "
                   "\n4)change rolls "
                   "\n5)change both ")
    return answer


def play(dice, rolls):
    result = random_number_from_dice_list(dice, rolls)
    print(f'Sum of your random numbers is {result}')


if __name__ == '__main__':
    dice = dice_sides()
    rolls = how_many_rolls()
    play(dice, rolls)

    while True:
        user_input = wanna_roll_again()
        if user_input == '1' or user_input == 'yes':
            play(dice, rolls)
        elif user_input == '2' or user_input == 'end':
            print("Bye")
            break
        elif user_input == '3' or user_input == "change dice":
            dice = dice_sides()
            play(dice, rolls)
        elif user_input == '4' or user_input == "change rolls":
            rolls = how_many_rolls()
            play(dice, rolls)
        elif user_input == '5' or user_input == "change both":
            dice = dice_sides()
            rolls = how_many_rolls()
            play(dice, rolls)

# after result as from user if she or he wants to roll again,
# or change dice, number of rolls or both
# if the user answers end, end program.
