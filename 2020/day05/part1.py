from typing import List

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

SEATS: List[str] = get_data(2020, 5, split=True)
logger.debug("Loaded seats list")

# Each seat ID is just a binary number with 10 bits, where F and L are 0
# and R and B are 1.

TRANS = str.maketrans("FBLR", "0101")  # Create translation dictionary

# Get all seat IDs
SEAT_IDS = [int(seat.translate(TRANS), base=2) for seat in SEATS]

logger.success("Result: {}", max(SEAT_IDS))
