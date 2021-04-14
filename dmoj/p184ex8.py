candidates = {char: 0 for char in "ABCDEF"}
spoiled = 0

for _ in range(int(input())):
    vote = input()

    if vote in candidates.keys():
        candidates[vote] += 1
    else:
        spoiled += 1

for char in "ABCDEF":
    print(candidates[char])

print(spoiled)
