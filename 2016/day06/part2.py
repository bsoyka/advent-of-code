from collections import Counter

# Input data loading
from aocd import get_data

lines = [line.strip() for line in get_data(year=2016, day=6).splitlines()]

columns = ("".join(column) for column in zip(*lines))

solution: str = ""

for column in columns:
    least_common = Counter(column).most_common()[:-2:-1][0][0]
    solution += least_common

print(solution)
