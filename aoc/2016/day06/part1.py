from pathlib import Path

with (Path(__file__).parent / 'input.txt').open() as f:
    lines = [line.strip() for line in f]
columns = [[] for _ in range(len(lines[0]))]
for line in lines:
    for col_index, char in enumerate(line):
        columns[col_index].append(char)
final = [max(set(col), key=col.count) for col in columns]
print(''.join(final))
