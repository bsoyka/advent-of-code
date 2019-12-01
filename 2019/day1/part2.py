def mass(module):
    rs = 0
    ch = module + 0
    while (ch := ch // 3 - 2) > 0:
        rs += ch
    return rs


with open("input.txt") as f:
    lines = [mass(int(line.strip())) for line in f.readlines()]
print(sum(lines))  # 4903759
