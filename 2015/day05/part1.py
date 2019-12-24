from string import ascii_lowercase

with open("input.txt") as f:
    strings = [line.strip() for line in f.readlines()]


def vowels(inp):
    return sum([inp.count(vowel) for vowel in ["a", "e", "i", "o", "u"]])


def doubles(inp):
    return sum([inp.count(pair * 2) for pair in ascii_lowercase])


def bad_substrings(inp):
    return sum([inp.count(sub) for sub in ["ab", "cd", "pq", "xy"]])


nice = 0
for test_str in strings:
    if bad_substrings(test_str):
        continue
    if vowels(test_str) >= 3 and doubles(test_str) >= 1:
        nice += 1
print(nice)
