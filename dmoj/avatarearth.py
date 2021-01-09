b_x, b_y = map(int, input().split(" "))
x_1, y_1, x_2, y_2 = map(int, input().split(" "))

print("Yes" if x_1 < b_x < x_2 and y_1 < b_y < y_2 else "No")
