from PythonCourse.test_code import test_and_tested_material_hard as hard
import pytest
import mock


def test_print_hands(capsys):
    hard.asking_area()
    captured = capsys.readouterr()
    assert captured.out == "Do you want to also know the area of tringle, yes or no "

def test_ask_if_player_wants_card():
    # This line replaces user input, with pre defined value.
    with mock.patch('builtins.input', return_value="yes"):
        # Then the normal assert line.
        assert hard.asking_area() == "yes"
