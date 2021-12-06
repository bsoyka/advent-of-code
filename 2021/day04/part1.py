import sys
from itertools import groupby

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data
from bsoyka_aoc_utils.bingo import BingoCard

DATA_LINES: list[str] = get_data(2021, 4, split=True)

DATA_LINE_GROUPS = [
    list(y) for x, y in groupby(DATA_LINES, key=lambda x: x != "") if x
]

CALL_NUMBERS = [
    int(number) for number in DATA_LINE_GROUPS.pop(0)[0].split(",")
]

BINGO_CARDS = [BingoCard.from_data(data) for data in DATA_LINE_GROUPS]

logger.debug("Loaded call numbers and bingo cards data")

for call_number in CALL_NUMBERS:
    for card in BINGO_CARDS:
        card.mark_number(call_number)

        if card.won:
            RESULT = card.unmarked_sum * call_number

            logger.success("Result: {}", RESULT)
            sys.exit()
