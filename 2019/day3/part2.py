# BETWEEN 27888 AND 29122
with open("input.txt") as f:
    lines = [line.strip().split(",") for line in f.readlines()]
line_locs = []
line_locs2 = []
current_loc = [0, 0]
for move_index, move in enumerate(lines[0]):
    print(move_index)
    direction = move[:1]
    number = int(move[1:])
    if direction == "R":
        for _ in range(number):
            current_loc[0] += 1
            line_locs.append(str(current_loc[:]))
    if direction == "U":
        for _ in range(number):
            current_loc[1] += 1
            line_locs.append(str(current_loc[:]))
    if direction == "L":
        for _ in range(number):
            current_loc[0] -= 1
            line_locs.append(str(current_loc[:]))
    if direction == "D":
        for _ in range(number):
            current_loc[1] -= 1
            line_locs.append(str(current_loc[:]))
current_loc = [0, 0]
for move_index, move in enumerate(lines[1]):
    print(move_index)
    direction = move[:1]
    number = int(move[1:])
    if direction == "R":
        for _ in range(number):
            current_loc[0] += 1
            line_locs2.append(str(current_loc[:]))
    if direction == "U":
        for _ in range(number):
            current_loc[1] += 1
            line_locs2.append(str(current_loc[:]))
    if direction == "L":
        for _ in range(number):
            current_loc[0] -= 1
            line_locs2.append(str(current_loc[:]))
    if direction == "D":
        for _ in range(number):
            current_loc[1] -= 1
            line_locs2.append(str(current_loc[:]))
set1 = set(line_locs)
set2 = set(line_locs2)
intersections = set1.intersection(set2)
distances = set()
for intersection in intersections:
    intersection = list(map(int, intersection[1:-1].split(", ")))
    distances.add(abs(intersection[0]) + abs(intersection[1]))
print(intersections)
print(distances)
print(min(distances))
