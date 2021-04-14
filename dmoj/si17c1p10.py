input()

a_values = map(int, input().split(" "))
a_counts = map(int, input().split(" "))

alice = sum(value * count for value, count in zip(a_values, a_counts))

input()

c_values = map(int, input().split(" "))
c_counts = map(int, input().split(" "))

carl = sum(value * count for value, count in zip(c_values, c_counts))

print(alice, carl)
