import re
from pathlib import Path

regex = r"([a-z ]+) (-?\d+)"
with (Path(__file__).parent / "input.txt").open() as f:
    instructions = [line.strip() for line in f.readlines()]

deck = list(range(10007))
for instruction in instructions:
    search = re.search(regex, instruction)
    if search is None:
        if instruction == "deal into new stack":
            deck = list(reversed(deck))
    else:
        todo, num = search.groups()[0], int(search.groups()[1])
        if todo == "cut":
            deck = deck[num:] + deck[:num]
        elif todo == "deal with increment":
            new = [None for _ in range(len(deck))]
            current = 0
            for card in deck:
                new[current] = card
                current += num
                while current > len(deck) - 1:
                    current -= len(deck)
            deck = list(new)
print(deck.index(2019))
