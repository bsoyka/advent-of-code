from pathlib import Path

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_TEXT = f.readlines()
logger.debug("Loaded instruction data")


location = 50
result = 0

for instruction in INPUT_TEXT:
    direction, distance = instruction[0], int(instruction[1:])

    match direction:
        case "L":
            location -= distance
        case "R":
            location += distance

    location = location % 100

    if location == 0:
        result += 1

logger.success("Result: {}", result)
