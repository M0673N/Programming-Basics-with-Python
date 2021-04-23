budget = int(input())
season = input()
fishermen = int(input())

if season == "Spring":
    rent = 3000
    if fishermen <= 6:
        rent *= 0.9
    elif 7 <= fishermen <= 11:
        rent *= 0.85
    elif fishermen >= 12:
        rent *= 0.75
    if fishermen % 2 == 0:
        rent *= 0.95
elif season == "Summer" or season == "Autumn":
    rent = 4200
    if fishermen <= 6:
        rent *= 0.9
    elif 7 <= fishermen <= 11:
        rent *= 0.85
    elif fishermen >= 12:
        rent *= 0.75
    if season == "Summer" and fishermen % 2 == 0:
        rent *= 0.95
else:
    rent = 2600
    if fishermen <= 6:
        rent *= 0.9
    elif 7 <= fishermen <= 11:
        rent *= 0.85
    elif fishermen >= 12:
        rent *= 0.75
    if fishermen % 2 == 0:
        rent *= 0.95

if budget >= rent:
    print(f"Yes! You have {(budget - rent):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - rent):.2f} leva.")
