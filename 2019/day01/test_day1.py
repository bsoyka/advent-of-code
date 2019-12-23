from part1 import part_1
from part2 import part_2


def test_part_1():
    with open("input.txt") as f:
        assert part_1([line.strip() for line in f.readlines()]) == 3271095


def test_part_2():
    with open("input.txt") as f:
        assert part_2([line.strip() for line in f.readlines()]) == 4903759
