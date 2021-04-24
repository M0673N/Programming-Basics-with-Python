budget = float(input())
fuel_l = float(input())
day = input()
total = fuel_l * 2.1 + 100
if day == "Saturday":
    total *= 0.9
else:
    total *= 0.8
if budget >= total:
    print(f"Safari time! Money left: {(budget - total):.2f} lv.")
else:
    print(f"Not enough money! Money needed: {(total - budget):.2f} lv.")
