from pathlib import Path
from re import match

with (Path(__file__).parent / "input.txt").open() as f:
    bag_lines = [line.strip() for line in f.readlines()]

bags = {}

for line in bag_lines:
    color = match(r"(.+) bags contain", line).group(1)
    contents_str = line.split("contain ")[1][:-1]

    contents = []

    if contents_str != "no other bags":
        for content in contents_str.split(", "):
            content_color = match(r"\d+ (.+) bags?", content).group(1)

            contents.append(content_color)

    bags[color] = contents


def has_shiny_gold(color):
    if "shiny gold" in bags[color]:
        return True
    else:
        return any(has_shiny_gold(content_color) for content_color in bags[color])


matches = sum(1 for color in bags.keys() if has_shiny_gold(color))

print(matches)
