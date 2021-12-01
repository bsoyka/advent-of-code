# Input data loading
from aocd import get_data

depths = list(map(int, get_data(year=2021, day=1).splitlines()))

result = sum(
    1 if depths[index - 1] < depth else 0
    for index, depth in enumerate(depths)
    if index != 0
)

print(result)
