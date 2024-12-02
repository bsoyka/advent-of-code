from bsoyka_aoc_utils import get_data
from loguru import logger

CALIBRATION_LINES: list[str] = get_data(2023, 1, split=True)
logger.debug("Loaded calibration lines")

result: int = 0

for calibration_line in CALIBRATION_LINES:
    digits = [character for character in calibration_line if character.isdigit()]

    calibration_value = int(digits[0] + digits[-1])
    result += calibration_value

logger.success("Result: {}", result)
