from string import ascii_lowercase

letter_scores = {y: x for x, y in enumerate(ascii_lowercase, start=1)}

print(sum(letter_scores[letter] for letter in input()))
