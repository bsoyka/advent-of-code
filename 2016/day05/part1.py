import re
import hashlib
with open("input.txt") as f:
    prefix = f.read().strip()
regex = re.compile(r"^0{5}.")
index = 0
final = ""
for _ in range(8):
    while True:
        m = hashlib.md5()
        m.update(f"{prefix}{index}".encode("utf-8"))
        index += 1
        if regex.match(m.hexdigest()):
            print(index, m.hexdigest(), m.hexdigest()[5])
            final += m.hexdigest()[5]
            break
print(final)