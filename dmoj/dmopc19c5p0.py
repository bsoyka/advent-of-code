participants, cutoff = map(int, input().split(' '))

for _ in range(participants):
    name, score = input().split(' ')

    if int(score) > cutoff:
        print(f'{name} will advance')
    else:
        print(f'{name} will not advance')
