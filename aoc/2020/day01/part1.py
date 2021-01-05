from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    expenses = [int(line.strip()) for line in f.readlines()]

set_expenses = set(expenses)

for expense in expenses:
    if 2020 - expense in set_expenses:
        print(expense * (2020 - expense))
        exit()
