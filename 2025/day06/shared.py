from math import prod


def solve_problem(input_list: list[str]) -> int:
    """Solve a cephalopod math problem.

    This function supports addition and multiplication.

    Args:
        input_list: The vertical list of inputs, given as the numbers in string
            format followed by the operator.

    Returns:
        The solution to the problem.
    """
    numbers = map(int, input_list[:-1])

    match input_list[-1]:
        case "+":
            return sum(numbers)
        case "*":
            return prod(numbers)

    raise ValueError("invalid operator specified")
