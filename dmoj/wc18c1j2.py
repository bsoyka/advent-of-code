name = input()

print('Y' if name in [input() for _ in range(5)] else 'N')
