from pathlib import Path
from string import ascii_lowercase

with (Path(__file__).parent / "input.txt").open() as f:
    strings = [line.strip() for line in f.readlines()]


def vowels(string):
    return sum([string.count(vowel) for vowel in ["a", "e", "i", "o", "u"]])


def doubles(string):
    return sum([string.count(pair * 2) for pair in ascii_lowercase])


def bad_substrings(string):
    return sum([string.count(sub) for sub in ["ab", "cd", "pq", "xy"]])


nice = 0

for test_str in strings:
    if bad_substrings(test_str):
        continue

    if vowels(test_str) >= 3 and doubles(test_str) >= 1:
        nice += 1

print(nice)  # 258
