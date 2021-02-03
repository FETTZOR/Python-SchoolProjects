#! /usr/bin/python3
# original author: Emil Khaibrakhmanov
# I the author grant the use of this code for teaching: yes

import normal_4_solution as norm
import pytest


def test_normal():
    assert norm.a_letter_finder("alfa windows omega car beta floor") == "alfa-omega-beta"
    assert norm.a_letter_finder("extra phone media browser pc notebook gamma") == "extra-media-gamma"
    assert norm.a_letter_finder("pycharm drama hydra intellij zebra rider webstorm") == "drama-hydra-zebra"
