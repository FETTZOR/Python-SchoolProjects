#! /usr/bin/python3
from math import sqrt


def ask_from_user(question, valid_answer):
    while True:

        user_input = input(question)
        if user_input in valid_answer:
            break
        else:
            print("not a valid answer, try again")
    return user_input


def triangle_side_asker(leg, task):
    if task == "hypotenuse":
        input_text_to_send = "give " + leg + " leg: "
    elif task == "leg":
        input_text_to_send = "give hypotenuse "
    while True:
        try:
            side = int(input(input_text_to_send))
            break
        except:
            print("Only integers are allowed")

    return side


def side_calculation(side1, side2, task):
    if task == "hypotenuse":
        side = sqrt(side2 ** 2 + side1 ** 2)
    else:
        side = sqrt(side2 ** 2 - side1 ** 2)
    return side

def asking_area():
    question2 = "Do you want to also know the area of tringle, yes or no "
    question2_answers = ["yes", "no"]
    user_wants_to_know_area = ask_from_user(question2, question2_answers)

    if user_wants_to_know_area == "yes":
        sides = [side1_from_user, side2_from_user, answer1]
        sides.sort()
        area = (sides[0] * sides[1]) / 2
        print("area of the triangle is", area)
    else:
        print("ok, have a good day")

if __name__ == '__main__':
    question1 = "You can calculate hypotenuse or leg of a right triangle, answer: hypotenuse or leg "
    question1_answers = ["hypotenuse", "leg"]

    task = ask_from_user(question1, question1_answers)

    side1_from_user = triangle_side_asker("first", "hypotenuse")
    if task == "hypotenuse":
        side2_from_user = triangle_side_asker("second", task)
    elif task == "leg":
        side2_from_user = triangle_side_asker("", task)

    answer1 = side_calculation(side1_from_user, side2_from_user, task)

    print("Lenght of asked ", task, " is ", answer1)

    area_of_triangle = asking_area()


