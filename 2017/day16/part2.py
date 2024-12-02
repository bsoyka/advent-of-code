from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    steps = [(step[0], step[1:]) for step in f.read().strip().split(",")]
dancers = [char for char in "abcdefghijklmnop"]
dance_list = []
while True:
    for step in steps:
        if step[0] == "s":
            num = int(step[1])
            dancers = dancers[-1 * num :] + dancers[: -1 * num]
        elif step[0] == "x":
            pos = list(map(int, step[1].split("/")))
            dancers[pos[0]], dancers[pos[1]] = dancers[pos[1]], dancers[pos[0]]
        elif step[0] == "p":
            change = step[1].split("/")
            a, b = dancers.index(change[0]), dancers.index(change[1])
            dancers[a], dancers[b] = dancers[b], dancers[a]
    dance_list.append(dancers)
    if dancers == [char for char in "abcdefghijklmnop"]:
        break
sequence = len(dance_list)
remaining = 1_000_000_000 % sequence
dancers = [char for char in "abcdefghijklmnop"]
for _ in range(remaining):
    for step in steps:
        if step[0] == "s":
            num = int(step[1])
            dancers = dancers[-1 * num :] + dancers[: -1 * num]
        elif step[0] == "x":
            pos = list(map(int, step[1].split("/")))
            dancers[pos[0]], dancers[pos[1]] = dancers[pos[1]], dancers[pos[0]]
        elif step[0] == "p":
            change = step[1].split("/")
            a, b = dancers.index(change[0]), dancers.index(change[1])
            dancers[a], dancers[b] = dancers[b], dancers[a]
print("".join(dancers))
