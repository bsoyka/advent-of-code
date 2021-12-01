from pathlib import Path


def part_1(modules):
    return sum(int(module) // 3 - 2 for module in modules)


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open() as f:
        print(part_1([line.strip() for line in f.readlines()]))
