from collections import Counter

for _ in range(int(input())):
    c = Counter(input().split(" "))
    most = c.most_common(1)[0]

    if most[1] >= 2:
        print(most[0])
    else:
        print("???")
