first_count = int(input())
second_count = int(input())

first_words = [input() for _ in range(first_count)]
second_words = [input() for _ in range(second_count)]

for first in first_words:
    for second in second_words:
        print(f'{first} as {second}')
