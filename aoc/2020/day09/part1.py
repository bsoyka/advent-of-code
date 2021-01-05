from pathlib import Path
from itertools import combinations
from sys import exit

with (Path(__file__).parent / "input.txt").open() as f:
    numbers = [*map(int, [line.strip() for line in f.readlines()])]

index = 25

while True:
    good = False
    print(index)

    for combo in [
        list(combo) for combo in combinations(numbers[index - 25 : index], 2)
    ]:
        print(combo)
        if sum(combo) != numbers[index]:
            good = True
            break

    if not good:
        print(numbers[index])
        exit()

    index += 1
