from hashlib import md5
from pathlib import Path
from re import match
from sys import exit

with (Path(__file__).parent / 'input.txt').open() as f:
    key = f.read().strip()

number = 0

while True:
    number += 1
    hashed = md5(f'{key}{number}'.encode('utf-8')).hexdigest()

    if match(r'^0{5,}', hashed):
        print(number)
        exit()
