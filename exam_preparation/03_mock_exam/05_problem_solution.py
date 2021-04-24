budget = float(input())
number_of_series = int(input())
total_price = 0
for i in range(number_of_series):
    name = input()
    price = float(input())
    if name == "Thrones":
        price *= 0.5
    elif name == "Lucifer":
        price *= 0.6
    elif name == "Protector":
        price *= 0.7
    elif name == "TotalDrama":
        price *= 0.8
    elif name == "Area":
        price *= 0.9
    total_price += price
if total_price > budget:
    print(f"You need {total_price - budget:.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget - total_price:.2f} lv.")
