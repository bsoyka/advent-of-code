from functools import cache
from itertools import combinations
from pathlib import Path

from loguru import logger


@cache
def get_all_possible_button_combinations(num_buttons: int) -> list[tuple[int]]:
    """Determine all possible ways to press a given number of buttons.

    Args:
        num_buttons: The number of buttons available.

    Returns:
        A list of tuples, each representing a set of buttons to press.
    """
    buttons = list(range(num_buttons))
    all_subsets = []
    for r in range(num_buttons + 1):
        for combo in combinations(buttons, r):
            all_subsets.append(combo)
    return all_subsets


def test_buttons(
    buttons: list[tuple[int]], indices_to_press: tuple[int], desired_lights: list[bool]
) -> bool:
    """Check whether a combination of buttons makes a machine work.

    Args:
        buttons: The available buttons on the machine, each represented as a tuple of
            integer indices mapping to lights on the machine.
        indices_to_press: A tuple of integer indices mapping to buttons to press.
        desired_lights: The desired light pattern for the machine to work.

    Returns:
        Whether pressing the specified buttons causes the machine to display the desired
        light sequence.
    """
    lights = [False for _ in desired_lights]

    for bi in indices_to_press:
        button_lights = buttons[bi]
        for li in button_lights:
            lights[li] = False if lights[li] else True

    return lights == desired_lights


class FactoryMachine:
    """A factory machine, from Advent of Code day 10.

    Attributes:
        light_diagram: The desired light pattern to make the machine work, given as a
            list of boolean values representing whether each light should be on or off.
        buttons: A list of the buttons available on the machine, where each button is a
            tuple of integer indices corresponding to which lights the button toggles.
    """

    def __init__(self, light_diagram: list[bool], buttons: list[tuple[int]]):
        self.light_diagram = light_diagram
        self.buttons = buttons

    @classmethod
    def from_input_line(cls, machine_line: str) -> FactoryMachine:
        """Initialize a factory machine from the format given in the input.

        Args:
            machine_line: A line of input.

        Returns:
            A factory machine object.
        """
        input_parts = machine_line.split()

        light_diagram = list(
            map(lambda c: True if c == "#" else False, input_parts[0][1:-1])
        )
        buttons = list(
            map(
                lambda button: tuple(map(int, button[1:-1].split(","))),
                input_parts[1:-1],
            )
        )

        return cls(light_diagram, buttons)

    @property
    def fewest_presses(self) -> int:
        """The fewest button presses possible to make the machine work."""
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
