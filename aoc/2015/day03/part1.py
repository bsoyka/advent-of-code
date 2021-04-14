from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    moves = f.read().strip()

santa = [0, 0]
visited = [[0, 0]]

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
        visited.append([santa[0], santa[1]])

print(len(visited))
