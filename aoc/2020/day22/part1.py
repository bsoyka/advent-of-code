from itertools import groupby
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    lines = [line.strip() for line in f.readlines()]

player_1, player_2 = [
    [int(card) for card in y]
    for x, y in groupby(lines, lambda x: x == "" or x[:6] == "Player")
    if not x
]

while len(player_1) > 0 and len(player_2) > 0:
    p1_card = player_1.pop(0)
    p2_card = player_2.pop(0)

    if p1_card > p2_card:
        player_1.append(p1_card)
        player_1.append(p2_card)
    else:
        player_2.append(p2_card)
        player_2.append(p1_card)

if len(player_1) > 0:
    winner = player_1
else:
    winner = player_2

score = sum(index * card for index, card in enumerate(winner[::-1], start=1))

print(score)
