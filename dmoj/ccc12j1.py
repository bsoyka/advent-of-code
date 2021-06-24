limit, speed = int(input()), int(input())
over = speed - limit

if over > 30:
    print('You are speeding and your fine is $500.')
elif over > 20:
    print('You are speeding and your fine is $270.')
elif over > 0:
    print('You are speeding and your fine is $100.')
else:
    print('Congratulations, you are within the speed limit!')
