budget = float(input())
extras = int(input())
outfits = float(input())

decor = budget * 0.10
if extras > 150:
    outfits -= outfits * 0.10

outfits = extras * outfits

if outfits + decor > budget:
    print("Not enough money!")
    print(f"Wingard needs {((outfits + decor) - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - (decor + outfits)):.2f} leva left.")
