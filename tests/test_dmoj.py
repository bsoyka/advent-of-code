from pathlib import Path
from subprocess import PIPE, Popen
from sys import executable
from types import LambdaType
from typing import List, Union

from pytest import mark, fail

from .dmoj_data import problems

all_tests: List[List[Union[str, list]]] = [
    [problem, *test] for problem, tests in problems.items() for test in tests
]
dmoj_dir = Path(__file__).parent.parent / 'dmoj'


@mark.parametrize('problem,test_input,expected_output', all_tests)
def test_dmoj_problems(problem: str, test_input, expected_output):
    if not isinstance(test_input, list):
        test_input = [test_input]

    problem_path = str(dmoj_dir / f'{problem}.py')
    p = Popen([executable, problem_path], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    output, errors = p.communicate(
        ('\n'.join(map(str, test_input)) + '\n').encode('utf-8')
    )

    assert not errors

    if isinstance(expected_output, LambdaType):
        assert expected_output(output.decode('utf-8').splitlines())
    else:
        if not isinstance(expected_output, list):
            expected_output = [expected_output]

        assert output.decode('utf-8').splitlines() == list(
            map(str, expected_output)
        )


@mark.parametrize(
    'problem',
    list({p.stem for p in dmoj_dir.glob('*.py')} - set(problems.keys())),
)
def test_missing_answers(problem: str):
    fail(f"Problem {problem} doesn't have any examples for testing")
