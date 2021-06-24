for _ in range(int(input())):
    input()

    print(''.join(''.join(x) for x in zip(input(), input()))[::-1])
