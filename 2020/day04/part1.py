from itertools import groupby

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

PASSPORT_LINES = get_data(2020, 4, split=True)
PASSPORTS = [
    " ".join(list(y))
    for x, y in groupby(PASSPORT_LINES, key=lambda x: x != "")
    if x
]
logger.debug("Loaded passports data")

valid: int = 0

for passport in PASSPORTS:
    field_names = [field.split(":")[0] for field in passport.split(" ")]

    if all(
        required_field in field_names
        for required_field in ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
    ):
        valid += 1

logger.success("Result: {}", valid)
