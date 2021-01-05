values = [100, 500, 1_000, 5_000, 10_000, 25_000, 50_000, 100_000, 500_000, 1_000_000]
numbers = {
    "1": 100,
    "2": 500,
    "3": 1_000,
    "4": 5_000,
    "5": 10_000,
    "6": 25_000,
    "7": 50_000,
    "8": 100_000,
    "9": 500_000,
    "10": 1_000_000,
}

for _ in range(int(input())):
    values.remove(numbers[input()])

offer = int(input())

average = sum(values) / len(values)

if average < offer:
    print("deal")
else:
    print("no deal")
