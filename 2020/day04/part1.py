from itertools import groupby
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    passport_lines = [line.strip() for line in f.readlines()]

passports = [
    " ".join(list(y))
    for x, y in groupby(passport_lines, key=lambda x: x != "")
    if x
]


valid = 0

for passport in passports:
    field_names = [field.split(":")[0] for field in passport.split(" ")]

    fields_needed = 7 - sum(
        required_field in field_names
        for required_field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    )

    if fields_needed == 0:
        valid += 1

print(valid)
