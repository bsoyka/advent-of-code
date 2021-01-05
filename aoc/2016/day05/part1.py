from hashlib import md5
from pathlib import Path
from re import compile

with (Path(__file__).parent / "input.txt").open() as f:
    prefix = f.read().strip()

regex = compile(r"0{5}.")

index = 0
final = ""

for _ in range(8):
    while True:
        m = md5(f"{prefix}{index}".encode("utf-8")).hexdigest()

        index += 1

        if regex.match(m):
            final += m[5]
            break

print(final)
