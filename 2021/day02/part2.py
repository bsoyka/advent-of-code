# Input data loading
from aocd import get_data

# Simple logging
from loguru import logger

data_raw = get_data(year=2021, day=2).splitlines()

data_clean = []

for line in data_raw:
    data_clean.append(line.strip())

logger.info("Loaded depths list")

result = 0

logger.success("Result: {}", result)
