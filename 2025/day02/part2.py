from pathlib import Path

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_TEXT = f.read()

logger.debug("Loaded input data")

RANGES = INPUT_TEXT.split(",")

def is_number_repeat(num: int)->bool:
    num_str = str(num)

    start_substrings = {num_str[:index] for index in range(1, (len(num_str) // 2) + 1)}

    for start_substring in start_substrings:
        if num_str.replace(start_substring, "") == "":
            return True

    return False

result = 0

for id_range in RANGES:
    start, end = map(int, id_range.split("-"))

    for number in range(start, end+1):
        if is_number_repeat(number):
            result += number

wrong = {21646796736}

if result in wrong:
    logger.error("Result: {}", result)
else:
    logger.success("Result: {}", result)