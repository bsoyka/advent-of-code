input()
hobbies = input().split(' ')
count = sum(len(hobby) <= 10 for hobby in hobbies)
print(count)
