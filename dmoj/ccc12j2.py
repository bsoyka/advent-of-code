r1, r2, r3, r4 = (int(input()) for _ in range(4))

if r1 < r2 < r3 < r4:
    print('Fish Rising')
elif r1 > r2 > r3 > r4:
    print('Fish Diving')
elif r1 == r2 == r3 == r4:
    print('Fish At Constant Depth')
else:
    print('No Fish')
