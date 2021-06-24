from collections import Counter

_, votes = input(), input()

vote_count = Counter(votes)

if vote_count['A'] == vote_count['B']:
    print('Tie')
else:
    print(vote_count.most_common()[0][0])
