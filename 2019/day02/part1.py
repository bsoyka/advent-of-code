with open("input.txt") as f:
    txt = list(map(int, f.readlines()[0].strip().split(",")))
pos = 0
while True:
    print(pos)
    if txt[pos] == 1:
        txt[txt[pos + 3]] = txt[txt[pos + 1]] + txt[txt[pos + 2]]
    elif txt[pos] == 1:
        txt[txt[pos + 3]] = txt[txt[pos + 1]] * txt[txt[pos + 2]]
    elif txt[pos] == 99:
        break
    pos += 4
print(txt)
