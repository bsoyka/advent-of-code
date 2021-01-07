longest = 0

for _ in range(int(input())):
    start, stop = map(int, input().split(" "))
    length = stop - start

    if length > longest:
        longest = length

print(longest)
