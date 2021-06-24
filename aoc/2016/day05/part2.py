import hashlib
import re
from pathlib import Path

with (Path(__file__).parent / 'input.txt').open() as f:
    prefix = f.read().strip()
regex = re.compile(r'^0{5}[0-7].')
index = 0
final = [None for _ in range(8)]
while None in final:
    while True:
        m = hashlib.md5()
        m.update(f'{prefix}{index}'.encode('utf-8'))
        index += 1
        if regex.match(m.hexdigest()):
            if final[int(m.hexdigest()[5])] is not None:
                continue
            final[int(m.hexdigest()[5])] = m.hexdigest()[6]
            break
print(''.join(final))
