with open("input.txt") as f:
    lines = [line.strip().split(",") for line in f.readlines()]
line_locs = [set(), set()]
for line_index, line in enumerate(lines):
    current_loc = [0, 0]
    for move in line:
        direction = move[:1]
        number = int(move[1:])
        if direction == "R":
            for _ in range(number):
                current_loc[0] += 1
                line_locs[line_index].add(str(current_loc[:]))
        if direction == "U":
            for _ in range(number):
                current_loc[1] += 1
                line_locs[line_index].add(str(current_loc[:]))
        if direction == "L":
            for _ in range(number):
                current_loc[0] -= 1
                line_locs[line_index].add(str(current_loc[:]))
        if direction == "D":
            for _ in range(number):
                current_loc[1] -= 1
                line_locs[line_index].add(str(current_loc[:]))
intersections = {}
for location in line_locs[0]:
    if location in line_locs[1]:
        location = list(map(int, location[1:-1].split(", ")))
        distance = abs(location[0]) + abs(location[1])
        intersections[distance] = location
print(intersections)
