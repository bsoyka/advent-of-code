from bsoyka_aoc_utils import get_data
from loguru import logger

INSTRUCTIONS = get_data(2021, 2, split=True)
logger.debug("Loaded instructions list")

horizontal, depth = 0, 0

for instruction in INSTRUCTIONS:
    command, amount = instruction.split(" ")

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
