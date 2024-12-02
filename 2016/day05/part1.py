import re
from hashlib import md5

from aocd import get_data

prefix = get_data(year=2016, day=5)

regex = re.compile(r"0{5}.")

INDEX: int = 0
FINAL: str = ""

for _ in range(8):
    while True:
        HASH = md5(f"{prefix}{INDEX}".encode("utf-8")).hexdigest()

        INDEX += 1

        if regex.match(HASH):
            FINAL += HASH[5]
            break

print(FINAL)
