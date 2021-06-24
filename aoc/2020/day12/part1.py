from pathlib import Path

DIRECTIONS = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
ROTATIONS = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}

with (Path(__file__).parent / 'input.txt').open() as f:
    instructions = [line.strip() for line in f.readlines()]

position = [0, 0]
facing = 90


def move(position, count, direction):
    x, y = ROTATIONS[direction]

    position[0] += x * count
    position[1] += y * count

    return position


def left(facing, degrees):
    return (facing - degrees) % 360


def right(facing, degrees):
    return (facing + degrees) % 360


for instruction in instructions:
    command, val = instruction[0], int(instruction[1:])

    if command == 'F':
        position = move(position, val, facing)
    elif command == 'L':
        facing = left(facing, val)
    elif command == 'R':
        facing = right(facing, val)
    else:
        position = move(position, val, DIRECTIONS[command])

print(abs(position[0]) + abs(position[1]))
