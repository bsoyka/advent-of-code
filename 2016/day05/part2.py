import re
from hashlib import md5
from typing import List, Optional

# Input data loading
from aocd import get_data

prefix = get_data(year=2016, day=5)

regex = re.compile(r"^0{5}[0-7].")

INDEX: int = 0
FINAL: List[Optional[str]] = [None for _ in range(8)]

while None in FINAL:
    while True:
        HASH = md5(f"{prefix}{INDEX}".encode("utf-8")).hexdigest()

        INDEX += 1

        if regex.match(HASH):
            if FINAL[int(HASH[5])] is not None:
                continue

            FINAL[int(HASH[5])] = HASH[6]
            break

print("".join(FINAL))
