from itertools import count

for _ in range(int(input())):
    for x in count(start=int(input()) + 1):
        if str(x ** 3)[-3:] == '888':
            print(x)
            break
