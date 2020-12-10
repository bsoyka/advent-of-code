with open("input.txt") as f:
    expenses = [int(line.strip()) for line in f.readlines()]

set_expenses = set(expenses)

for expense in expenses:
    for expense2 in expenses:
        if 2020 - expense - expense2 in set_expenses:
            print(expense * expense2 * (2020 - expense - expense2))
            exit()
