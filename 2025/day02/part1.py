from pathlib import Path

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_TEXT = f.read()

logger.debug("Loaded input data")

RANGES = INPUT_TEXT.split(",")


def is_number_repeat(num: int) -> bool:
    num_str = str(num)

    if len(num_str) % 2:
        return False

    half_point = len(num_str) // 2

    first_half, second_half = num_str[:half_point], num_str[half_point:]

    return first_half == second_half


result = 0

for id_range in RANGES:
    start, end = map(int, id_range.split("-"))

    for number in range(start, end + 1):
        if is_number_repeat(number):
            result += number

logger.success("Result: {}", result)
