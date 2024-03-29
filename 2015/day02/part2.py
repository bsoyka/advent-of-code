from typing import List, Tuple

# Input data loading
from aocd import get_data

# Utilities for this day
from utils import smallest_perimeter

gifts: List[Tuple[int, int, int]] = [
    tuple(map(int, line.strip().split("x")))
    for line in get_data(year=2015, day=2).splitlines()
]

print(
    sum(
        smallest_perimeter(length, width, height) + (length * width * height)
        for length, width, height in gifts
    )
)
