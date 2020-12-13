from pathlib import Path

def reset():
    with (Path(__file__).parent / "input.txt").open() as f:
        return list(map(int, f.readlines()[0].strip().split(",")))


txt = reset()
pos = 0


def result(noun, verb):
    global txt
    global pos
    txt[1], txt[2] = noun, verb
    while True:
        print(len(txt), pos)
        if txt[pos] == 1:
            txt[txt[pos + 3]] = txt[txt[pos + 1]] + txt[txt[pos + 2]]
        elif txt[pos] == 1:
            txt[txt[pos + 3]] = txt[txt[pos + 1]] * txt[txt[pos + 2]]
        elif txt[pos] == 99:
            break
        pos += 4
    pos = 0
    return txt[0]


for noun in range(100):
    for verb in range(100):
        txt = reset()
        print(result(noun, verb))
        if result(noun, verb) == 19690720:
            print((100 * noun) + verb)
