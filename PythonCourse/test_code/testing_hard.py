from PythonCourse.test_code import test_and_tested_material_hard as hard
import pytest
import mock
import os
import py


def test_asking_area():
    assert hard.asking_area('no') is None


def test_asking_area_different_answer():
    assert hard.asking_area('asd') is None


# i took a triangle calculation from asking triangle function for test also
def test_asking_area_calculation():
    expected = 7.5
    assert hard.calc_triangle_area(3, 5) == expected
