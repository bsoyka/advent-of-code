from copy import copy
from typing import List

# Input data loading
from aocd import get_data

moves = get_data(year=2015, day=3)

santa: List[int] = [0, 0]
visited: List[List[int]] = [[0, 0]]

for move in moves:
    if move == ">":
        santa[0] += 1
    elif move == "<":
        santa[0] -= 1
    elif move == "^":
        santa[1] += 1
    elif move == "v":
        santa[1] -= 1

    if santa not in visited:
        visited.append(copy(santa))

print(len(visited))
