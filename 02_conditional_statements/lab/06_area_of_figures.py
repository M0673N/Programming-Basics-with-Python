from math import pi

figure = input()
if figure == "square":
    side = float(input())
    print(side * side)
elif figure == "rectangle":
    side = float(input())
    side_2 = float(input())
    print(side * side_2)
elif figure == "circle":
    radius = float(input())
    print(pi * pow(radius, 2))
elif figure == "triangle":
    base = float(input())
    height = float(input())
    print(base * height / 2)
