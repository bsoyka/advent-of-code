with open("input.txt") as f:
    steps = [(step[0], step[1:]) for step in f.read().strip().split(",")]
dancers = [char for char in "abcdefghijklmnop"]
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
