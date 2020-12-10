from itertools import groupby

with open("input.txt") as f:
    passport_lines = [line.strip() for line in f.readlines()]

passports = list(
    " ".join(list(y)) for x, y in groupby(passport_lines, key=lambda x: x != "") if x
)

valid = 0

for passport in passports:
    field_names = [field.split(":")[0] for field in passport.split(" ")]

    fields_needed = 7

    for required_field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if required_field in field_names:
            fields_needed -= 1

    if fields_needed == 0:
        valid += 1

print(valid)
