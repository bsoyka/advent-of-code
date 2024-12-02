import sys
from hashlib import md5
from re import match

from aocd import get_data

key = get_data(year=2015, day=4)

number: int = 0

while True:
    number += 1
    HASHED = md5(f"{key}{number}".encode("utf-8")).hexdigest()

    if match(r"^0{5,}", HASHED):
        print(number)
        sys.exit()
