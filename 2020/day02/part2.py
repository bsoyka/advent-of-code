with open("input.txt") as f:
    password_lines = [line.strip() for line in f.readlines()]

password_sets = [
    (
        [int(num) for num in line.split(" ")[0].split("-")],
        line.split(" ")[1][:-1],
        line.split(" ")[2],
    )
    for line in password_lines
]

good = 0

for password_set in password_sets:
    count = 0

    for position in password_set[0]:
        if password_set[2][position - 1] == password_set[1]:
            count += 1

    if count == 1:
        good += 1

print(good)
