import re

from bsoyka_aoc_utils import get_data
from loguru import logger

INSTRUCTION_NUMBERS = re.compile(r"^move (\d+) from (\d+) to (\d+)$")

inputs: list[str] = get_data(2022, 5, split=True)
logger.debug("Loaded input data")

separator_index = inputs.index("")
crates_input, instructions = (
    inputs[:separator_index],
    inputs[separator_index + 1:],
)

# TODO: Automate stack parsing

# List crate stacks from bottom to top
stacks = [
    ["F", "D", "B", "Z", "T", "J", "R", "N"],
    ["R", "S", "N", "J", "H"],
    ["C", "R", "N", "J", "G", "Z", "F", "Q"],
    ["F", "V", "N", "G", "R", "T", "Q"],
    ["L", "T", "Q", "F"],
    ["Q", "C", "W", "Z", "B", "R", "G", "N"],
    ["F", "C", "L", "S", "N", "H", "M"],
    ["D", "N", "Q", "M", "T", "J"],
    ["P", "G", "S"],
]

for instruction in instructions:
    count, start, end = map(
        int, INSTRUCTION_NUMBERS.match(instruction).groups()
    )

    crates = stacks[start - 1][-count:]
    del stacks[start - 1][-count:]
    stacks[end - 1].extend(crates)

result = "".join(stack[-1] for stack in stacks)

logger.success("Result: {}", result)
