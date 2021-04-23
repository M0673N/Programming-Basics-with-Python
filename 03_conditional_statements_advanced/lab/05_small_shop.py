product_name = input()
city = input()
amount = float(input())

if city == "Sofia":
    coffee = 0.5
    water = 0.8
    beer = 1.2
    sweets = 1.45
    peanuts = 1.60
elif city == "Plovdiv":
    coffee = 0.4
    water = 0.7
    beer = 1.15
    sweets = 1.30
    peanuts = 1.50
else:
    coffee = 0.45
    water = 0.7
    beer = 1.1
    sweets = 1.35
    peanuts = 1.55

if product_name == "coffee":
    print(coffee * amount)
elif product_name == "water":
    print(water * amount)
elif product_name == "beer":
    print(beer * amount)
elif product_name == "sweets":
    print(sweets * amount)
else:
    print(peanuts * amount)
