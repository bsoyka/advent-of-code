# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

INSTRUCTIONS = get_data(2021, 2, split_lines=True)
logger.debug("Loaded instructions list")

horizontal, depth, aim = 0, 0, 0

for instruction in INSTRUCTIONS:
    command, amount = instruction.split(" ")

    amount = int(amount)

    match command:
        case "down":
            aim += amount
            logger.trace("Aimed down {}", amount)
        case "up":
            aim -= amount
            logger.trace("Aimed up {}", amount)
        case "forward":
            horizontal += amount
            logger.trace("Moved forward {}", amount)

            depth += aim * amount
            logger.trace("Moved down {}", aim * int(amount))

logger.info("Final horizontal position: {}", horizontal)
logger.info("Final depth: {}", depth)
logger.info("Final aim: {}", aim)

logger.success("Result: {}", horizontal * depth)
