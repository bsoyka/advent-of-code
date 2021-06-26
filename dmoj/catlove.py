cats = 0

for _ in range(int(input())):
    if input() == 'cats':
        cats += 1
    else:
        cats -= 1

if cats == 0:
    print('equal')
elif cats > 0:
    print('cats')
else:
    print('dogs')
