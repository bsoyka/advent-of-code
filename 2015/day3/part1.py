with open("input.txt") as f:
    start = f.readlines()[0].strip()
current = [0, 0]
visited = [[0, 0]]
for move in start:
    if move == ">":
        current[0] += 1
    elif move == "<":
        current[0] -= 1
    elif move == "^":
        current[1] += 1
    elif move == "v":
        current[1] -= 1

    if current not in visited:
        visited.append([current[0], current[1]])
print(len(visited))
