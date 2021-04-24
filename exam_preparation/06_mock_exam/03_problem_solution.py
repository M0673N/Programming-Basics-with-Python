size = input()
color = input()
series = int(input())
if size == "Large":
    if color == "Red":
        price = 16
    elif color == "Green":
        price = 12
    else:
        price = 9
elif size == "Medium":
    if color == "Red":
        price = 13
    elif color == "Green":
        price = 9
    else:
        price = 7
else:
    if color == "Red":
        price = 9
    elif color == "Green":
        price = 8
    else:
        price = 5
print(f"{price * series * 0.65:.2f} leva.")
