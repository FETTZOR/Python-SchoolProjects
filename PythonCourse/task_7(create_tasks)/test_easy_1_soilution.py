import pytest
import easy_1_solution as ez


def test_easy_1(capsys):
    ez.vehicle_prices(23)
    captured = capsys.readouterr()
    count = 1
    assert captured.out == f"{count} bicycle\n"
    ez.vehicle_prices(6543)
    captured = capsys.readouterr()
    assert captured.out == f"{count} medium tractor\n"
