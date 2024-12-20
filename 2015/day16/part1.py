import sys
from re import match

from aocd import get_data

sue_list = get_data(year=2015, day=16).splitlines()

known = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
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

    good = all(known[item] == count for item, count in sue_known.items())

    if good:
        print(number)
        sys.exit()
