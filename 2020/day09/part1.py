from pathlib import Path
from sys import exit

with (Path(__file__).parent / "input.txt").open() as f:
    numbers = [int(line.strip()) for line in f.readlines()]

window = numbers[:25]

for n in numbers[25:]:
    differences = {n - x for x in window}
    is_valid = len(set(window).intersection(differences))

    if not is_valid:
        print(n)
        exit()
    else:
        window.append(n)
        window.pop(0)
