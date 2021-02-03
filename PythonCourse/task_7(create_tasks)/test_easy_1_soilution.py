#! /usr/bin/python3
# original author: Emil Khaibrakhmanov
# I the author grant the use of this code for teaching: yes

import pytest
import easy_1_solution as ez


def test_easy_1(capsys):
    ez.vehicle_prices(23)
    captured = capsys.readouterr()
    count = 1
    assert captured.out == "Zero\n"
    ez.vehicle_prices(48000)
    captured = capsys.readouterr()
    assert captured.out == f"{count} medium tractor\n"
