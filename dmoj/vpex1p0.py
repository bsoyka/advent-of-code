start = [int(x) for x in input().split(' ')]

dm = divmod(*start)

print(' '.join(str(x) for x in dm))
