import pytest
import day_3 as day3


@pytest.mark.parametrize("data_input,expected", [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
])
def test_part1_samples(data_input, expected):
    assert day3.part1(data_input) == expected


@pytest.mark.parametrize("data_input,expected", [
    (1, 2),
    (3, 4),
    (500, 747),
    (747, 806),
])
def test_part2_samples(data_input, expected):
    assert day3.part2(data_input) == expected
