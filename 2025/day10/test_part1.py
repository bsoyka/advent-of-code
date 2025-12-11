from part1 import FactoryMachine, get_all_possible_button_combinations
from pytest import fixture


def test_get_all_possible_button_combinations():
    assert get_all_possible_button_combinations(4) == [
        (),
        (0,),
        (1,),
        (2,),
        (3,),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3),
        (0, 1, 2, 3),
    ]


@fixture
def example_machine():
    return FactoryMachine(
        [False, True, True, False],
        [(3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)],
    )


def test_factory_machine_from_input_line():
    machine = FactoryMachine.from_input_line("[.###] (0,2,3) (2) (1,2,3) {19,9,30,28}")

    assert machine.light_diagram == [False, True, True, True]
    assert machine.buttons == [(0, 2, 3), (2,), (1, 2, 3)]


def test_fewest_presses(example_machine):
    assert example_machine.fewest_presses == 2
