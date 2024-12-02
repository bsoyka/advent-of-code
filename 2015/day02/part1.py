from typing import List, Tuple

from aocd import get_data

from utils import smallest_side, surface_area

gifts: List[Tuple[int, ...]] = [
    tuple(map(int, line.strip().split("x")))
    for line in get_data(year=2015, day=2).splitlines()
]

print(sum(surface_area(*gift) + smallest_side(*gift) for gift in gifts))
