from aocd import get_data

from utils import bad_substrings, doubles, vowels

strings = get_data(year=2015, day=5).splitlines()

NICE = 0

for test_str in strings:
    if bad_substrings(test_str):
        continue

    if vowels(test_str) >= 3 and doubles(test_str) >= 1:
        NICE += 1

print(NICE)
