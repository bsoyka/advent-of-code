numbers = {
    '1': 100,
    '2': 500,
    '3': 1_000,
    '4': 5_000,
    '5': 10_000,
    '6': 25_000,
    '7': 50_000,
    '8': 100_000,
    '9': 500_000,
    '10': 1_000_000,
}
values = numbers.values()

for _ in range(int(input())):
    values.remove(numbers[input()])

if sum(values) / len(values) < int(input()):
    print('deal')
else:
    print('no deal')
