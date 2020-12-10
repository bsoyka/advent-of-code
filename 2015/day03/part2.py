from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    moves = f.read().strip()

santa = [0, 0]
robo_santa = [0, 0]

visited = [[0, 0]]

robo = False

for move in moves:
    if robo:
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

        robo = False
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

        robo = True

print(len(visited))  # 2631
