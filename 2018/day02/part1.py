from collections import Counter

with open("input.txt") as f:
    boxes = [line.strip() for line in f]

two_letters = 0
three_letters = 0

for box in boxes:
    two = False
    three = False
    items = Counter(box).items()
    for letter, count in items:
        if count == 2 and not two:
            two_letters += 1
            two = True
        elif count == 3 and not three:
            three_letters += 1
            three = True
        if two and three:
            break
print(two_letters * three_letters)
