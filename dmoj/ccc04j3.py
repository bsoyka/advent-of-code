first_count = int(input())
second_count = int(input())

first_words = []
second_words = []

for _ in range(first_count):
    first_words.append(input())
for _ in range(second_count):
    second_words.append(input())

for first in first_words:
    for second in second_words:
        print(f"{first} as {second}")
