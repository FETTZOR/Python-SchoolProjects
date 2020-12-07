from PythonCourse.test_code import testing_easy_and_normal_with_material
import pytest
import mock


def test_side_calculation_hypotenuse():
    side1 = 2
    side2 = 3
    task = "hypotenuse"
    # c = a2 + b2
    expected = 3.61
    assert round(testing_easy_and_normal_with_material.side_calculation(side1, side2, task), 2) == expected


def test_side_calculation_hypotenuse_exception():
    try:
        testing_easy_and_normal_with_material.side_calculation('x', 4, "hypotenuse")
        assert False
    except TypeError:
        assert True


def test_side_calculation_leg():
    side1 = 4
    side2 = 5
    task = "leg"
    expected = 3
    assert round(testing_easy_and_normal_with_material.side_calculation(side1, side2, task), 2) == expected


def test_side_calculation_leg_exception():
    try:
        testing_easy_and_normal_with_material.side_calculation('x', 3, "leg")
        assert False
    except TypeError:
        assert True


def test_triangle_side_asker():
    with mock.patch('builtins.input', return_value=2):
        assert testing_easy_and_normal_with_material.triangle_side_asker('', 'leg') == 2


def test_triangle_side_asker_hypo():
    with mock.patch('builtins.input', return_value=2):
        assert testing_easy_and_normal_with_material.triangle_side_asker('', 'hypotenuse') == 2


def test_ask_from_user():
    # homework.ask_from_user([1, 4], [8, 4])
    # captured = capsys.readouterr()
    with mock.patch('builtins.input',
                    return_value='You can calculate hypotenuse or leg of a right triangle, answer: hypotenuse or leg '):
        assert testing_easy_and_normal_with_material.ask_from_user('',
                                      'hypotenuse') == 'You can calculate hypotenuse or leg of a right triangle, answer: hypotenuse or leg '
# def triangle_side_asker(leg, task):
#     if task == "hypotenuse":
#         input_text_to_send = "give " + leg + " leg: "
#     elif task == "leg":
#         input_text_to_send = "give hypotenuse "
#     while True:
#         try:
#             side = int(input(input_text_to_send))
#             break
#         except:
#             print("Only integers are allowed")
#
#     return side
# Easy + make also tehst for triangle_side_asker() and ask_from_user
#
# test different cases.

