from itertools import groupby
from re import match

from bsoyka_aoc_utils import get_data
from loguru import logger

PASSPORT_LINES = get_data(2020, 4, split=True)
PASSPORTS = [
    " ".join(list(y))
    for x, y in groupby(PASSPORT_LINES, key=lambda x: x != "")
    if x
]
logger.debug("Loaded passports data")

valid: int = 0

for passport in PASSPORTS:
    fields = dict(field.split(":") for field in passport.split(" "))

    # Skip if any required field is missing
    if any(
        required_field not in fields
        for required_field in ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
    ):
        continue

    # Skip if any year is invalid
    if any(
        not match(r"^\d{4}$", fields[field]) for field in ["byr", "iyr", "eyr"]
    ):
        continue

    # Check all year values

    if not 1920 <= int(fields["byr"]) <= 2002:
        continue

    if not 2010 <= int(fields["iyr"]) <= 2020:
        continue

    if not 2020 <= int(fields["eyr"]) <= 2030:
        continue

    # Check the height with a regex, get the number and unit
    if not (
        height_match := match(
            r"^(?P<value>\d{2,3})(?P<unit>in|cm)$", fields["hgt"]
        )
    ):
        continue

    # Check inches
    if height_match.group("unit") == "in":
        if not 59 <= int(height_match.group("value")) <= 76:
            continue
    # Check centimeters
    elif not 150 <= int(height_match.group("value")) <= 193:
        continue

    # Check hair color as a valid hex code
    if not match(r"^#[0-9a-f]{6}$", fields["hcl"]):
        continue

    # Check eye color
    if fields["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        continue

    # Check the passport ID as a nine-digit number
    if not match(r"^\d{9}$", fields["pid"]):
        continue

    # All conditions met, valid passport
    valid += 1

logger.success("Result: {}", valid)
