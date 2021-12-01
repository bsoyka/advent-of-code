from collections import Counter

# Input data loading
from aocd import get_data

lines = [line.strip() for line in get_data(year=2016, day=6).splitlines()]

columns = ("".join(column) for column in zip(*lines))

solution: str = ""

for column in columns:
    most_common = Counter(column).most_common(1)[0][0]
    solution += most_common

print(solution)
