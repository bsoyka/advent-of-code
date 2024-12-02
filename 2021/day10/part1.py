from bsoyka_aoc_utils import get_data
from loguru import logger

CHARS = {"(": ")", "[": "]", "{": "}", "<": ">"}
VALUES = {")": 3, "]": 57, "}": 1197, ">": 25137}

LINES: list[str] = get_data(2021, 10, split=True)
logger.debug("Loaded chunks data")

result: int = 0

for line in LINES:
    stack: list[str] = []

    for char in line:
        if char in CHARS:
            # The character is an opening bracket
            stack.append(char)
        else:
            # The character is a closing bracket
            last_open_char = stack.pop()

            if char != CHARS[last_open_char]:
                result += VALUES[char]
                break

logger.success("Result: {}", result)
