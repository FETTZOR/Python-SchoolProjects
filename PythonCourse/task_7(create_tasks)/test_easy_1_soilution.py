import pytest
import easy_1_soilution as ez


def test_output(capsys):
    ez.vehicle_prices(23)
    captured = capsys.readouterr()
    count = 1
    assert captured.out == f"{count} bicycle\n"


def test_output_2(capsys):
    ez.vehicle_prices(6543)
    captured = capsys.readouterr()
    count = 1
    assert captured.out == f"{count} medium tractor\n"
