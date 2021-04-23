flower = input()
amount = int(input())
budget = int(input())
price = 0

if flower == "Roses":
    if amount > 80:
        price = (5 * amount) * 0.9
    else:
        price = 5 * amount
elif flower == "Dahlias":
    if amount > 90:
        price = (3.8 * amount) * 0.85
    else:
        price = 3.8 * amount
elif flower == "Tulips":
    if amount > 80:
        price = (2.8 * amount) * 0.85
    else:
        price = 2.8 * amount
elif flower == "Narcissus":
    if amount < 120:
        price = (3 * amount) * 1.15
    else:
        price = 3 * amount
elif flower == "Gladiolus":
    if amount < 80:
        price = (2.5 * amount) * 1.2
    else:
        price = 2.5 * amount

if budget >= price:
    print(f"Hey, you have a great garden with {amount} {flower} and {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(price - budget):.2f} leva more.")
