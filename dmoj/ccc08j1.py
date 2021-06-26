weight, height = float(input()), float(input())

bmi = weight / height**2

if bmi > 25:
    print('Overweight')
elif 18.5 <= bmi <= 25:
    print('Normal weight')
else:
    print('Underweight')
