wins = sum(input() == 'W' for _ in range(6))

if wins >= 5:
    print(1)
elif wins >= 3:
    print(2)
elif wins >= 1:
    print(3)
else:
    print(-1)
