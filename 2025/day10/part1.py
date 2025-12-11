from itertools import combinations
from pathlib import Path

from loguru import logger


def get_all_possible_button_combinations(num_buttons: int) -> list[tuple[int]]:
    buttons = list(range(num_buttons))
    all_subsets = []
    for r in range(num_buttons + 1):
        for combo in combinations(buttons, r):
            all_subsets.append(combo)
    return all_subsets


def test_buttons(
    buttons: list[set[int]], indices_to_press: tuple[int], desired_lights: list[bool]
) -> bool:
    lights = [False for _ in desired_lights]

    for bi in indices_to_press:
        button_lights = buttons[bi]
        for li in button_lights:
            lights[li] = False if lights[li] else True

    return lights == desired_lights


class FactoryMachine:
    def __init__(
        self,
        light_diagram: list[bool],
        buttons: list[set[int]],
        joltage_requirements: list[int],
    ):
        self.light_diagram = light_diagram
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements

    @classmethod
    def from_input_line(cls, machine_line: str) -> FactoryMachine:
        input_parts = machine_line.split()

        raw_light_diagram, *raw_buttons, raw_joltage_requirements = input_parts

        light_diagram = list(
            map(lambda c: True if c == "#" else False, raw_light_diagram[1:-1])
        )
        buttons = list(
            map(lambda button: set(map(int, button[1:-1].split(","))), raw_buttons)
        )
        joltage_requirements = list(map(int, raw_joltage_requirements[1:-1].split(",")))

        return cls(light_diagram, buttons, joltage_requirements)

    @property
    def fewest_presses(self) -> int:
        for button_combination in get_all_possible_button_combinations(
            len(self.buttons)
        ):
            if test_buttons(self.buttons, button_combination, self.light_diagram):
                return len(button_combination)

        raise ValueError


if __name__ == "__main__":
    INPUT_LINES = (Path(__file__).parent / "input.txt").read_text().splitlines()
    logger.debug("Loaded input data")

    result = sum(
        FactoryMachine.from_input_line(input_line).fewest_presses
        for input_line in INPUT_LINES
    )
    logger.success("Result: {}", result)
