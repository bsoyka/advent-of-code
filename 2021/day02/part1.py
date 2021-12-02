# Input data loading
from aocd import get_data

# Simple logging
from loguru import logger

instructions = get_data(year=2021, day=2).splitlines()
logger.debug("Loaded instruction data")

horizontal, depth = 0, 0

for instruction in instructions:
    command, amount = instruction.strip().split(" ")

    amount = int(amount)

    match command:
        case "forward":
            horizontal += amount
            logger.trace("Moved forward {}", amount)
        case "down":
            depth += amount
            logger.trace("Moved down {}", amount)
        case "up":
            depth -= amount
            logger.trace("Moved up {}", amount)

logger.info("Final horizontal position: {}", horizontal)
logger.info("Final depth: {}", depth)

logger.success("Result: {}", horizontal * depth)
