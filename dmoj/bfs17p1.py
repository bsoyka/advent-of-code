count = 0
input()
hobbies = input().split(" ")
for hobby in hobbies:
    if len(hobby) <= 10:
        count += 1
print(count)
