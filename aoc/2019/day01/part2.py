from pathlib import Path


def mass(module):
    rs = 0
    ch = module + 0
    while (ch := ch // 3 - 2) > 0:
        rs += ch
    return rs


def part_2(modules):
    return sum([mass(int(module)) for module in modules])


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open() as f:
        print(part_2([line.strip() for line in f.readlines()]))
