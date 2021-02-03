#! /usr/bin/python3
# original author: Emil Khaibrakhmanov
# I the author grant the use of this code for teaching: yes

import easy_3_solution as ez3
import pytest


def test_km_to_miles():
    assert ez3.km_to_miles(1) == 0.62
    assert ez3.km_to_miles(3) == 1.86
    assert ez3.km_to_miles(77) == 47.85


def test_miles_to_km():
    assert ez3.miles_to_km(1) == 1.61
    assert ez3.miles_to_km(3) == 4.83
    assert ez3.miles_to_km(77) == 123.92
