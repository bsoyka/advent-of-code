from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    lines = [line.strip() for line in f]
columns = [[] for _ in range(len(lines[0]))]
final = []
for line in lines:
    for col_index, char in enumerate(line):
        columns[col_index].append(char)
for col in columns:
    final.append(min(set(col), key=col.count))
print("".join(final))
