from pathlib import Path
from re import match
from sys import exit

with (Path(__file__).parent / "input.txt").open() as f:
    sue_list = [line.strip() for line in f.readlines()]

known = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1,
}

for sue in sue_list:
    groups = match(
        r"Sue (\d+): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)", sue
    ).groups()

    number = groups[0]

    sue_known = {
        groups[1]: int(groups[2]),
        groups[3]: int(groups[4]),
        groups[5]: int(groups[6]),
    }

    good = True

    for item, count in sue_known.items():
        if not known[item](count):
            good = False

    if good == True:
        print(number)
        exit()
