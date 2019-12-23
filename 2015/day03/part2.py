with open("input.txt") as f:
    start = f.readlines()[0].strip()
current = [0, 0]
current2 = [0, 0]
visited = [[0, 0]]
robo = False
for move in start:
    if robo:
        if move == ">":
            current2[0] += 1
        elif move == "<":
            current2[0] -= 1
        elif move == "^":
            current2[1] += 1
        elif move == "v":
            current2[1] -= 1

        if current2 not in visited:
            visited.append([current2[0], current2[1]])
        robo = False
    else:
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
        robo = True
print(len(visited))
