import hard_5_solution as hard
import pytest
import mock


def test_hard():
    with mock.patch('builtins.input', return_value="0"):
        assert hard.StudentAccount().menu() is None


def test_id_emptiness():
    assert hard.StudentAccount().ID == {}


def check_is_credits_value_from_beginning_equals_to_zero():
    assert hard.StudentAccount().credits == 0