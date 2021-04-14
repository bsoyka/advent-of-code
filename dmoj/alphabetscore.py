from string import ascii_lowercase

letter_scores = dict((y, x) for x, y in enumerate(ascii_lowercase, start=1))

string = input()
score = 0

for letter in string:
    score += letter_scores[letter]

print(score)
