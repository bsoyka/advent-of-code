# Input data loading
from aocd import get_data

start = get_data(year=2017, day=1)

total: int = 0

for index_1, char_1 in enumerate(start):
    index_2 = (index_1 + 1) % len(start)
    char_2 = start[index_2]

    if char_1 == char_2:
        total += int(char_1)

print(total)
