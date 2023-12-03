# Simple logging
from loguru import logger

import regex as re

# Personal utilities
from bsoyka_aoc_utils import get_data

DIGIT_WORDS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
DIGIT_EXPRESSION = re.compile(r"(\d|" + r"|".join(DIGIT_WORDS.keys()) + r")")


def convert_digit(digit_match: re.Match) -> int:
    """Converts a matched digit word or number to a one-digit string

    Args:
        digit_str (re.Match): The digit as it was matched in the input

    Returns:
        str: The digit as a string
    """
    digit_str = digit_match[0]
    if digit_str.isdigit():
        return digit_str
    return DIGIT_WORDS[digit_str]


CALIBRATION_LINES: list[str] = get_data(2023, 1, split=True)
logger.debug("Loaded calibration lines")

result: int = 0

for calibration_line in CALIBRATION_LINES:
    digits = list(
        map(
            convert_digit,
            re.finditer(DIGIT_EXPRESSION, calibration_line, overlapped=True),
        ),
    )

    calibration_value = int(digits[0] + digits[-1])
    result += calibration_value

logger.success("Result: {}", result)
