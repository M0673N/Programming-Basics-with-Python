type_of_projection = input()
rows = int(input())
columns = int(input())
price = rows * columns

if type_of_projection == "Premiere":
    price = price * 12
elif type_of_projection == "Normal":
    price = price * 7.5
else:
    price *= 5

print(f"{price:.2f} leva")
