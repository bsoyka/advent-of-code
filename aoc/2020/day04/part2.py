from itertools import groupby
from pathlib import Path
from re import match

with (Path(__file__).parent / 'input.txt').open() as f:
    passport_lines = [line.strip() for line in f.readlines()]

passports = [
    ' '.join(list(y))
    for x, y in groupby(passport_lines, key=lambda x: x != '')
    if x
]


valid = 0

for passport in passports:
    fields = dict([field.split(':') for field in passport.split(' ')])

    fields_needed = 7 - sum(
        required_field in fields
        for required_field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    )

    if fields_needed != 0:
        continue

    if not 1920 <= int(fields['byr']) <= 2002:
        continue

    if not 2010 <= int(fields['iyr']) <= 2020:
        continue

    if not 2020 <= int(fields['eyr']) <= 2030:
        continue

    height_match = match(r'^(\d{2,3})(in|cm)$', fields['hgt'])

    if not height_match:
        continue

    if height_match.groups()[1] == 'in':
        if not 59 <= int(height_match.groups()[0]) <= 76:
            continue
    elif not 150 <= int(height_match.groups()[0]) <= 193:
        continue
    if not match(r'^#[0-9a-f]{6}$', fields['hcl']):
        continue

    if fields['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        continue

    if not match(r'^\d{9}$', fields['pid']):
        continue

    valid += 1

print(valid)
