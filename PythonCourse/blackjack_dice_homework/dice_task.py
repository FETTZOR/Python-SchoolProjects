# first import random module
import random


# This time we use the list Comprehension, to make a list
def function_dice_sides():
    number_of_sides_in_dice = int(input("How many-sided dice you want to cast? "))
    dice_sides = [i for i in range(1, number_of_sides_in_dice + 1)]
    return dice_sides


def function_random_number_from_dice_list(choose_sides):
    rolled_dice = random.choice(choose_sides)
    print("Your random numbers is ", rolled_dice)


while True:
    sides = function_dice_sides()
    number = function_random_number_from_dice_list(sides)

# define a function that takes in a number of sides in dice as an argument
# and returns a list that has all numbers of dice
# Ask from the user how many-sided dice he or she wants to cast
# Call the function with the user given answer
# roll the dice by taking random member from the list and return answer to the user using print
