from typing import List

from aocd import get_data

moves = get_data(year=2015, day=3)

santa: List[int] = [0, 0]
robo_santa: List[int] = [0, 0]

visited: List[List[int]] = [[0, 0]]

ROBO: bool = False

for move in moves:
    if ROBO:
        if move == ">":
            robo_santa[0] += 1
        elif move == "<":
            robo_santa[0] -= 1
        elif move == "^":
            robo_santa[1] += 1
        elif move == "v":
            robo_santa[1] -= 1

        if robo_santa not in visited:
            visited.append([robo_santa[0], robo_santa[1]])
    else:
        if move == ">":
            santa[0] += 1
        elif move == "<":
            santa[0] -= 1
        elif move == "^":
            santa[1] += 1
        elif move == "v":
            santa[1] -= 1

        if santa not in visited:
            visited.append([santa[0], santa[1]])

    ROBO = not ROBO

print(len(visited))
