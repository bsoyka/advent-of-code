from pathlib import Path

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_TEXT = f.read()

logger.debug("Loaded input data")

RANGES = INPUT_TEXT.split(",")


def is_number_repeat(num: int) -> bool:
    """Determines whether a number is a smaller number concatenated some number
    of times with itself.

    Args:
        num: The number to test.

    Returns: Whether the number is "invalid" by the problem criteria.
    """
    num_str = str(num)

    # If a number is a smaller number concatenated with itself some number of
    # times, when we remove all instances of the smaller number, we should get
    # an empty string.

    start_substrings = {num_str[:index] for index in range(1, (len(num_str) // 2) + 1)}

    for substring in start_substrings:
        if num_str.replace(substring, "") == "":
            return True

    return False


result = 0

for id_range in RANGES:
    start, end = map(int, id_range.split("-"))

    for number in range(start, end + 1):
        if is_number_repeat(number):
            result += number

logger.error("Result: {}", result)
