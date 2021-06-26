from string import digits
from typing import List

for _ in range(int(input())):
    name = input().lower()
    phrases: List[str] = []

    for letter in name:
        if letter == 'a':
            phrases.append('Hi!')
        elif letter == 'e':
            phrases.append('Bye!')
        elif letter == 'i':
            phrases.append('How are you?')
        elif letter == 'o':
            phrases.append('Follow me!')
        elif letter == 'u':
            phrases.append('Help!')
        elif letter in digits:
            phrases.append('Yes!')

    print(' '.join(phrases))
