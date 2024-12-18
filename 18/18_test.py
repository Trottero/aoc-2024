import pytest
from common.utils import read_file
from part1 import p1
from part2 import p2


@pytest.mark.parametrize(
    "filename, expected, bytes",
    [
        pytest.param(
            "18/test_input.txt", 22, 12, id="Day 18 Part 1 - Test Input",
        ),
    ],
)
def test_p1(filename, expected, bytes):
    # Test cases for p1 function
    assert p1(read_file(filename), bytes) == expected


@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "18/test_input.txt", (6, 1), id="Day 18 Part 2 - Test Input",
        ),
    ],
)
def test_p2(filename, expected):
    # Test cases for p2 function
    assert p2(read_file(filename)) == expected
